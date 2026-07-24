"""SessionStart hook — dynamic per-module orientation.

Prints a short orientation block at the start of every Claude Code session.
Claude Code injects this stdout into the session context, so Claude starts
already knowing which part of the codebase has active work — and the recent
direction of travel from git history — without spending a turn re-exploring.

Tested standalone: `python3 .claude/hooks/session_start_context.py`
"""

from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path

_EXCLUDE_DIRS = frozenset({
    ".git", ".venv", "venv", "env", "node_modules", "__pycache__",
    ".pytest_cache", ".mypy_cache", ".ruff_cache", "build", "dist",
})


def _project_root() -> Path:
    project = os.environ.get("CLAUDE_PROJECT_DIR")
    return Path(project) if project else Path(__file__).resolve().parents[2]


def _claude_md_areas(root: Path) -> set[str]:
    """Every directory (relative posix) that carries its own CLAUDE.md, except
    the repo root — the areas the CLAUDE.md hierarchy governs."""
    areas: set[str] = set()
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in _EXCLUDE_DIRS]
        if "CLAUDE.md" in filenames:
            rel = Path(dirpath).relative_to(root).as_posix()
            if rel != ".":
                areas.add(rel)
    return areas


def _area_of(changed: str, areas: set[str]) -> str | None:
    """The nearest CLAUDE.md-governed directory containing a changed file."""
    parts = changed.split("/")
    for depth in range(len(parts) - 1, 0, -1):
        candidate = "/".join(parts[:depth])
        if candidate in areas:
            return candidate
    return None


def _force_utf8() -> None:
    for stream in (sys.stdout, sys.stderr):
        reconfigure = getattr(stream, "reconfigure", None)
        if callable(reconfigure):
            try:
                reconfigure(encoding="utf-8")
            except (OSError, ValueError):
                pass


def _working_tree_changes() -> list[str]:
    """Return changed/untracked file paths via `git status --porcelain`."""
    try:
        result = subprocess.run(
            ["git", "status", "--porcelain"],
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            timeout=5,
        )
    except (OSError, subprocess.SubprocessError):
        return []
    paths: list[str] = []
    for line in result.stdout.splitlines():
        if len(line) > 3:
            paths.append(line[3:].strip().replace("\\", "/"))
    return paths


def _active_areas(root: Path, paths: list[str]) -> list[str]:
    """Map changed paths to the CLAUDE.md-governed areas they belong to."""
    governed = _claude_md_areas(root)
    found: set[str] = set()
    for path in paths:
        area = _area_of(path, governed)
        if area is not None:
            found.add(area)
    return sorted(found)


def _recent_commits(limit: int = 5) -> list[str]:
    """Return the last few commit subjects, newest first — recent direction."""
    try:
        result = subprocess.run(
            ["git", "log", f"-{limit}", "--pretty=format:%h %s"],
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            timeout=5,
        )
    except (OSError, subprocess.SubprocessError):
        return []
    return [line.strip() for line in result.stdout.splitlines() if line.strip()]


def main() -> None:
    _force_utf8()

    try:
        sys.stdin.read()
    except (OSError, ValueError):
        pass

    lines = ["## Session orientation", ""]
    changes = _working_tree_changes()
    areas = _active_areas(_project_root(), changes)

    if areas:
        lines.append(f"Active area(s) this session: **{', '.join(areas)}**.")
        lines.append("Load the matching `CLAUDE.md` in each before editing.")
    else:
        lines.append("Working tree is clean — no area has pending work.")

    commits = _recent_commits()
    if commits:
        lines.append("")
        lines.append("Recent commits (newest first):")
        lines.extend(f"- {commit}" for commit in commits)

    lines.append("")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
