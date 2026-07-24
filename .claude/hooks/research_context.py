"""UserPromptSubmit hook — injects research file inventory into context.

On every prompt in the investment-research-notes project, lists the markdown
files in the current working directory so Claude immediately knows what's
already been researched without requiring an explicit !ls. Output is injected
into the session context before Claude sees the user's message.

Exits silently when the current directory has no research files (e.g. the
repo root, a non-research subdirectory).

Tested standalone: echo '{"cwd":"/path/to/dir"}' | python3 .claude/hooks/research_context.py
"""

from __future__ import annotations

import json
import os
import sys
from pathlib import Path

# Skip navigation / config files — not research content
_SKIP_NAMES = frozenset({
    "CLAUDE.md", "README.md", "README.html",
    "CODEBASE_MAP.md", "AI-LAYER.md", "VALIDATION.md",
})
_SKIP_SUFFIXES = frozenset({".html", ".css", ".py", ".sh", ".json", ".lock", ".png"})


def main() -> int:
    try:
        raw = sys.stdin.read()
        payload = json.loads(raw) if raw.strip() else {}
    except (OSError, ValueError, json.JSONDecodeError):
        payload = {}

    cwd = Path(payload.get("cwd", os.getcwd()))

    # Collect markdown research files in cwd
    try:
        entries = list(cwd.iterdir())
    except OSError:
        return 0

    md_files = sorted(
        [
            f for f in entries
            if f.is_file()
            and f.suffix == ".md"
            and f.name not in _SKIP_NAMES
        ],
        key=lambda f: f.name,
    )

    if not md_files:
        return 0

    sub_dirs = sorted(
        d.name for d in entries
        if d.is_dir() and not d.name.startswith(".")
    )

    lines = [f"Existing files in {cwd.name}/:"]
    for f in md_files[:25]:
        try:
            kb = f.stat().st_size / 1024
            lines.append(f"  {f.name} ({kb:.0f} KB)")
        except OSError:
            lines.append(f"  {f.name}")
    if len(md_files) > 25:
        lines.append(f"  ... +{len(md_files) - 25} more .md files")

    if sub_dirs:
        shown = sub_dirs[:8]
        suffix = f" (+{len(sub_dirs) - 8} more)" if len(sub_dirs) > 8 else ""
        lines.append(f"Subdirectories: {', '.join(shown)}{suffix}")

    # stdout is injected into Claude's context by UserPromptSubmit
    print("\n".join(lines))
    return 0


if __name__ == "__main__":
    sys.exit(main())
