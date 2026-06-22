#!/usr/bin/env python3
"""Validate content-first Markmap Markdown and optionally render HTML."""

from __future__ import annotations

import argparse
import os
import re
import shutil
import subprocess
import sys
from dataclasses import dataclass, field
from pathlib import Path


MEMORY_HOOK_RE = re.compile(r"(类比|Analogy)\s*[:：]\s*\S+", re.IGNORECASE)
HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*$")
LIST_RE = re.compile(r"^(\s*)[-*+]\s+(.+?)\s*$")
GENERIC_LABEL_RE = re.compile(
    r"^(项目定位|核心概念|运行机制|运行与存储|开发版图|技术架构|主要模块|关键流程|使用场景|"
    r"架构总览|系统概览|内容结构|主题类别|概念分类|Overview|Core Concepts|Architecture|"
    r"Runtime|Workflow|Use Cases|Main Modules|Key Flow|Category|Categories)$",
    re.IGNORECASE,
)
ASCII_RE = re.compile(r"[A-Za-z0-9]")
CJK_RE = re.compile(r"[\u4e00-\u9fff]")


@dataclass
class Node:
    text: str
    line: int
    level: int
    kind: str
    children: list["Node"] = field(default_factory=list)

    @property
    def label(self) -> str:
        compact = re.sub(r"\s+", " ", self.text).strip()
        return compact[:90] + ("..." if len(compact) > 90 else "")

    @property
    def content_label(self) -> str:
        before_memory_hook = MEMORY_HOOK_RE.split(self.text, maxsplit=1)[0]
        before_detail = re.split(r"[:：。.!?]", before_memory_hook, maxsplit=1)[0]
        cleaned = re.sub(r"[`*_#\[\]（）()]+", "", before_detail)
        return re.sub(r"\s+", " ", cleaned).strip()

    @property
    def has_substantive_content_label(self) -> bool:
        label = self.content_label
        ascii_count = len(ASCII_RE.findall(label))
        cjk_count = len(CJK_RE.findall(label))
        return ascii_count >= 2 or cjk_count >= 2 or len(label) >= 4


def parse_markdown(path: Path) -> Node:
    root = Node(text=str(path), line=0, level=0, kind="root")
    stack: list[Node] = [root]

    for line_no, raw in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        heading = HEADING_RE.match(raw)
        if heading:
            level = len(heading.group(1))
            node = Node(text=heading.group(2), line=line_no, level=level, kind="heading")
            while stack and stack[-1].level >= level:
                stack.pop()
            stack[-1].children.append(node)
            stack.append(node)
            continue

        item = LIST_RE.match(raw)
        if item:
            spaces = item.group(1).replace("\t", "    ")
            level = 7 + (len(spaces) // 2)
            node = Node(text=item.group(2), line=line_no, level=level, kind="list")
            while stack and stack[-1].level >= level:
                stack.pop()
            stack[-1].children.append(node)
            stack.append(node)

    return root


def walk(node: Node) -> list[Node]:
    nodes = [node]
    for child in node.children:
        nodes.extend(walk(child))
    return nodes


def validate(root: Node) -> list[str]:
    errors: list[str] = []
    visible_roots = root.children
    if len(visible_roots) != 1:
        errors.append(f"line 0: expected exactly one root heading, found {len(visible_roots)}")

    for node in walk(root):
        if node.kind == "root":
            continue
        if node.level != 1:
            content_label = node.content_label
            if not node.has_substantive_content_label:
                errors.append(f"line {node.line}: missing substantive content in '{node.label}'")
            if GENERIC_LABEL_RE.fullmatch(content_label):
                errors.append(
                    f"line {node.line}: generic category label; lead with source content in '{node.label}'"
                )
        if node.children and len(node.children) > 7 and all(not child.children for child in node.children):
            errors.append(
                f"line {node.line}: leaf-detail group has {len(node.children)} children, expected at most 7 in '{node.label}'"
            )

    return errors


def render_markmap(input_path: Path, output_path: Path) -> tuple[bool, str]:
    commands: list[list[str]] = []
    markmap_bin = shutil.which("markmap")
    if markmap_bin:
        commands.append([markmap_bin, "--no-open", "--offline", "-o", str(output_path), str(input_path)])

    npx_bin = shutil.which("npx")
    if npx_bin:
        commands.append([npx_bin, "--yes", "markmap-cli", "--no-open", "--offline", "-o", str(output_path), str(input_path)])

    local_cli = Path("/root/markmap/packages/markmap-cli/bin/cli.js")
    if local_cli.exists() and Path("/root/markmap/node_modules").exists():
        commands.append(["node", str(local_cli), "--no-open", "--offline", "-o", str(output_path), str(input_path)])

    if not commands:
        return False, "No markmap renderer found on PATH, npx unavailable, and /root/markmap is not built."

    env = os.environ.copy()
    env.setdefault("PLAYWRIGHT_SKIP_BROWSER_DOWNLOAD", "1")

    messages: list[str] = []
    for cmd in commands:
        try:
            proc = subprocess.run(
                cmd,
                cwd=str(input_path.parent),
                text=True,
                capture_output=True,
                timeout=180,
                env=env,
            )
        except Exception as exc:  # pragma: no cover - defensive CLI wrapper
            messages.append(f"{' '.join(cmd)} -> {exc}")
            continue
        if proc.returncode == 0 and output_path.exists() and output_path.stat().st_size > 0:
            return True, f"Rendered with: {' '.join(cmd)}"
        detail = (proc.stderr or proc.stdout or "").strip()
        messages.append(f"{' '.join(cmd)} -> exit {proc.returncode}: {detail[:500]}")

    return False, "\n".join(messages)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path, help="Markdown mind map to validate")
    parser.add_argument("-o", "--output", type=Path, help="HTML output path")
    parser.add_argument("--validate-only", action="store_true", help="Only validate structure")
    args = parser.parse_args()

    if not args.input.exists():
        print(f"Input not found: {args.input}", file=sys.stderr)
        return 2

    input_path = args.input.resolve()
    root = parse_markdown(input_path)
    errors = validate(root)
    if errors:
        print("Validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print(f"Validation passed: {args.input}")
    if args.validate_only:
        return 0

    output = (args.output or args.input.with_suffix(".html")).resolve()
    ok, message = render_markmap(input_path, output)
    print(message)
    if not ok:
        return 3
    print(f"HTML written: {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
