#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
OUT_ROOT="$ROOT_DIR/docx"

if ! command -v pandoc >/dev/null 2>&1; then
  echo "Error: pandoc is required but not found in PATH." >&2
  exit 1
fi

mkdir -p "$OUT_ROOT"

find "$ROOT_DIR" -type f -name "*.md" ! -path "$OUT_ROOT/*" | while IFS= read -r src; do
  rel="${src#$ROOT_DIR/}"
  out="$OUT_ROOT/${rel%.md}.docx"
  mkdir -p "$(dirname "$out")"
  pandoc "$src" -o "$out"
  echo "Converted: $rel -> ${out#$ROOT_DIR/}"
done

echo "Done. DOCX files are in: ${OUT_ROOT#$ROOT_DIR/}/"
