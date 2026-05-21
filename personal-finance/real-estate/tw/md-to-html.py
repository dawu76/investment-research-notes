#!/usr/bin/env python3
"""Convert a Markdown file to a styled HTML document with CJK font support."""

import sys
import argparse
from pathlib import Path
import markdown2

CSS = """
* { box-sizing: border-box; margin: 0; padding: 0; }

body {
    font-family: -apple-system, "PingFang TC", "Hiragino Sans GB",
                 "Microsoft JhengHei", "Noto Sans CJK TC", sans-serif;
    font-size: 15px;
    line-height: 1.9;
    color: #24292e;
    background: #fff;
    padding: 48px 24px;
}

.page {
    max-width: 860px;
    margin: 0 auto;
}

h1, h2, h3, h4 {
    font-weight: 600;
    line-height: 1.4;
    margin-top: 2em;
    margin-bottom: 0.6em;
    padding-bottom: 0.3em;
}
h1 { font-size: 1.9em; border-bottom: 2px solid #e1e4e8; }
h2 { font-size: 1.4em; border-bottom: 1px solid #e1e4e8; }
h3 { font-size: 1.15em; }
h4 { font-size: 1em; color: #444; }

p { margin: 0.8em 0; }

a { color: #0366d6; text-decoration: none; }
a:hover { text-decoration: underline; }

hr { border: none; border-top: 1px solid #e1e4e8; margin: 2em 0; }

/* Tables */
table {
    width: 100%;
    border-collapse: collapse;
    margin: 1.2em 0;
    font-size: 0.92em;
}
th, td {
    border: 1px solid #dfe2e5;
    padding: 8px 14px;
    text-align: left;
    vertical-align: top;
}
th {
    background: #f6f8fa;
    font-weight: 600;
}
tr:nth-child(even) td { background: #fafbfc; }

/* Task list checkboxes */
ul.task-list { list-style: none; padding-left: 0; }
ul.task-list li { display: flex; align-items: flex-start; gap: 8px; margin: 0.5em 0; }
input[type="checkbox"] {
    margin-top: 5px;
    flex-shrink: 0;
    width: 15px;
    height: 15px;
    accent-color: #0366d6;
}

/* Regular lists */
ul:not(.task-list), ol {
    padding-left: 1.8em;
    margin: 0.6em 0;
}
li { margin: 0.25em 0; }
li > ul, li > ol { margin-top: 0.2em; }

/* Nested lists inside task-list items */
ul.task-list li > ul { padding-left: 1.6em; list-style: disc; }
ul.task-list li > ul li { display: list-item; }

/* Code */
code {
    font-family: "SF Mono", Menlo, Consolas, monospace, "PingFang TC";
    font-size: 0.88em;
    background: #f3f4f6;
    padding: 2px 5px;
    border-radius: 3px;
}
pre {
    background: #f6f8fa;
    border: 1px solid #e1e4e8;
    border-radius: 6px;
    padding: 16px;
    overflow-x: auto;
    margin: 1em 0;
}
pre code { background: none; padding: 0; }

/* Blockquote */
blockquote {
    border-left: 4px solid #dfe2e5;
    padding: 0 1em;
    color: #6a737d;
    margin: 1em 0;
}

/* Bold / italic */
strong { font-weight: 600; }

/* Warning callouts — ⚠ lines */
p:has(> strong:first-child) { margin-top: 1em; }

@media print {
    body { padding: 0; font-size: 13px; }
    a { color: #24292e; }
    a[href]::after { content: " (" attr(href) ")"; font-size: 0.8em; color: #666; }
}
"""

EXTRAS = [
    "tables",
    "task_list",
    "fenced-code-blocks",
    "header-ids",
    "cuddled-lists",
    "strike",
    "break-on-newline",
]


def convert(src: Path, dst: Path) -> None:
    md_text = src.read_text(encoding="utf-8")
    body_html = markdown2.markdown(md_text, extras=EXTRAS)

    title = src.stem.replace("-", " ").replace("_", " ")

    html = f"""<!DOCTYPE html>
<html lang="zh-TW">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <style>{CSS}</style>
</head>
<body>
  <div class="page">
{body_html}
  </div>
</body>
</html>"""

    dst.write_text(html, encoding="utf-8")
    print(f"Written: {dst}  ({dst.stat().st_size // 1024} KB)")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", help="Source .md file")
    parser.add_argument("-o", "--output", help="Output .html file (default: same stem)")
    args = parser.parse_args()

    src = Path(args.input)
    dst = Path(args.output) if args.output else src.with_suffix(".html")
    convert(src, dst)


if __name__ == "__main__":
    main()
