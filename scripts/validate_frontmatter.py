#!/usr/bin/env python3
"""
Validate markdown frontmatter for YAML-breaking double quotes.

Problem: YAML fields wrapped in "..." that contain literal ASCII " characters
inside will break the YAML parser (e.g., title: "foo "bar" baz").
Fix: Use Japanese 「」 quotes or escape properly instead.

Exit code 1 if any issues found (blocks git commit).
"""

import sys
import os
import re
import glob

DOUBLE_QUOTED_FIELD_RE = re.compile(r'^(\w[\w\-]*)\s*:\s*"(.*)"$')


def check_file(path):
    issues = []
    with open(path, encoding="utf-8") as f:
        content = f.read()

    if not content.startswith("---"):
        return issues

    end = content.find("\n---", 3)
    if end == -1:
        return issues
    frontmatter = content[3:end]

    for lineno, line in enumerate(frontmatter.splitlines(), start=2):
        m = DOUBLE_QUOTED_FIELD_RE.match(line.strip())
        if not m:
            continue
        field_name, field_value = m.group(1), m.group(2)
        if '"' in field_value:
            issues.append((lineno, field_name, line.strip()))

    return issues


def main():
    base = os.path.join(os.path.dirname(os.path.dirname(__file__)), "src", "content", "articles")
    patterns = [os.path.join(base, "**", "*.md")]

    staged_files = None
    if os.environ.get("GIT_INDEX_FILE"):
        import subprocess
        result = subprocess.run(
            ["git", "diff", "--cached", "--name-only", "--diff-filter=ACM"],
            capture_output=True, text=True
        )
        staged_files = set(result.stdout.strip().splitlines())

    all_issues = {}
    for pattern in patterns:
        for path in glob.glob(pattern, recursive=True):
            rel = os.path.relpath(path)
            if staged_files is not None and rel not in staged_files:
                continue
            issues = check_file(path)
            if issues:
                all_issues[path] = issues

    if not all_issues:
        return 0

    print("YAML frontmatter validation FAILED", file=sys.stderr)
    print("=" * 60, file=sys.stderr)
    print("Found ASCII double quotes inside double-quoted YAML fields.", file=sys.stderr)
    print("Replace inner \" characters with 「」 Japanese quotes.", file=sys.stderr)
    print("=" * 60, file=sys.stderr)
    for path, issues in sorted(all_issues.items()):
        print(f"\n{path}", file=sys.stderr)
        for lineno, field, line in issues:
            print(f"  line ~{lineno}: {field}: → {line}", file=sys.stderr)
    print(file=sys.stderr)
    return 1


if __name__ == "__main__":
    sys.exit(main())
