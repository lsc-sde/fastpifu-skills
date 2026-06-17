#!/usr/bin/env python3
"""Reformat markdown files so each sentence is on its own line.

Joins hard-wrapped paragraph lines, then re-splits by sentence boundaries.
Preserves YAML front matter, code blocks, tables, list structure, and headings.

Usage:
    python3 _authoring/unwrap_sentences.py              # process skills/*.md
    python3 _authoring/unwrap_sentences.py <glob>       # process custom paths
"""

import re
import sys
from pathlib import Path


SENTENCE_SPLIT = re.compile(r'(?<=[.!?])\s+(?=[A-Z"\'(\(\[]|(?:\d+[.)]\s*[A-Za-z]))')

# Abbreviations ending with period that should NOT trigger sentence split
ABBREVIATIONS = {
    'e.g.', 'i.e.', 'etc.', 'vs.', 'viz.', 'al.',
    'p.', 'pp.', 'vol.', 'no.',
    'Fig.', 'Table.', 'Eq.',
}


def protect_abbreviations(text: str) -> tuple[str, list[tuple[str, str]]]:
    protected = []
    result = text
    for abb in ABBREVIATIONS:
        ph = f'\x00ABB_{len(protected)}\x00'
        protected.append((ph, abb))
        result = result.replace(abb, ph)
    return result, protected


def restore_abbreviations(text: str, protected: list[tuple[str, str]]) -> str:
    for ph, abb in protected:
        text = text.replace(ph, abb)
    return text


def split_sentences(text: str) -> list[str]:
    text = text.strip()
    if not text:
        return []
    protected_text, protected = protect_abbreviations(text)
    parts = SENTENCE_SPLIT.split(protected_text)
    parts = [restore_abbreviations(p, protected) for p in parts]
    return [p.strip() for p in parts if p.strip()]


def is_list_marker(line: str) -> bool:
    return bool(re.match(r'^\s*[-*+]\s', line)) or bool(re.match(r'^\s*\d+[.)]\s', line))


def is_continuation(line: str) -> bool:
    """Check if line is a continuation of previous list item (indented text)."""
    return bool(re.match(r'^\s{2,}\S', line)) and not is_list_marker(line) and not line.strip().startswith('|')


def process_file(filepath: str) -> None:
    with open(filepath, 'r') as f:
        content = f.read()

    lines = content.split('\n')
    result = []
    i = 0
    n = len(lines)

    while i < n:
        line = lines[i]

        # YAML front matter
        if line.strip() == '---' and (i == 0 or (result and result[-1] == '')):
            result.append(line)
            i += 1
            while i < n and lines[i].strip() != '---':
                result.append(lines[i])
                i += 1
            if i < n:
                result.append(lines[i])
                i += 1
            continue

        # Fenced code block
        if line.strip().startswith('```'):
            result.append(line)
            i += 1
            while i < n and not lines[i].strip().startswith('```'):
                result.append(lines[i])
                i += 1
            if i < n:
                result.append(lines[i])
                i += 1
            continue

        # HTML comment
        if line.strip().startswith('<!--'):
            result.append(line)
            i += 1
            while i < n and '-->' not in lines[i]:
                result.append(lines[i])
                i += 1
            if i < n:
                result.append(lines[i])
                i += 1
            continue

        # Blank line
        if line.strip() == '':
            result.append('')
            i += 1
            continue

        # Heading
        if line.strip().startswith('#'):
            result.append(line.rstrip())
            i += 1
            continue

        # Table row / separator
        if '|' in line and line.strip().startswith('|'):
            result.append(line.rstrip())
            i += 1
            continue

        # Thematic break
        if re.match(r'^---+\s*$', line) or re.match(r'^\*\*\*+\s*$', line):
            result.append(line.rstrip())
            i += 1
            continue

        # List item with continuation lines
        if is_list_marker(line):
            item_lines = [line]
            i += 1
            while i < n and is_continuation(lines[i]):
                item_lines.append(lines[i])
                i += 1

            first = item_lines[0]
            m = re.match(r'^(\s*[-*+]\s)', first)
            if not m:
                m = re.match(r'^(\s*\d+[.)]\s)', first)
            prefix = m.group(1) if m else '- '
            indent = re.match(r'^(\s*)', first).group(1)

            clean_parts = []
            clean_parts.append(first[len(prefix):].strip())
            for cl in item_lines[1:]:
                clean_parts.append(cl.strip())
            clean_text = ' '.join(clean_parts)
            clean_text = re.sub(r'\s+', ' ', clean_text).strip()

            if not clean_text:
                result.append(first.rstrip())
                continue

            sentences = split_sentences(clean_text)
            for idx, s in enumerate(sentences):
                if idx == 0:
                    result.append(prefix + s)
                else:
                    result.append(' ' * len(prefix) + s)
            continue

        # Regular paragraph — collect contiguous non-blank, non-special lines
        para_lines = [line]
        i += 1
        while i < n:
            ln = lines[i]
            cond = (
                ln.strip() == ''
                or ln.strip().startswith('#')
                or ln.strip().startswith('```')
                or ln.strip().startswith('<!--')
                or is_list_marker(ln)
                or is_continuation(ln)
                or ('|' in ln and ln.strip().startswith('|'))
                or re.match(r'^\s*---+\s*$', ln)
                or re.match(r'^\s*\*\*\*+\s*$', ln)
            )
            if cond:
                break
            para_lines.append(ln)
            i += 1

        if para_lines:
            joined = ' '.join(l.strip() for l in para_lines)
            joined = re.sub(r'\s+', ' ', joined).strip()
            if joined:
                sentences = split_sentences(joined)
                result.extend(sentences)

    # Trim trailing blank lines, but keep one
    while result and result[-1] == '':
        result.pop()
    result.append('')

    output = '\n'.join(result)

    with open(filepath, 'w') as f:
        f.write(output)

    print(f"  ✓ {filepath}", flush=True)


def main() -> None:
    args = sys.argv[1:]

    if args:
        files = []
        for pattern in args:
            files.extend(sorted(Path.cwd().glob(pattern)))
    else:
        skills_dir = Path(__file__).parent.parent / 'skills'
        if not skills_dir.exists():
            print("Error: skills directory not found")
            sys.exit(1)
        files = sorted(skills_dir.rglob('*.md'))

    if not files:
        print("No markdown files found.")
        sys.exit(0)

    print(f"Found {len(files)} markdown files\n")
    for fpath in files:
        process_file(str(fpath))
    print(f"\nDone. Processed {len(files)} files.")


if __name__ == '__main__':
    main()
