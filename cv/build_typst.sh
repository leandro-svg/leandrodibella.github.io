#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
CV_DIR="$ROOT_DIR/cv"
OUT_DIR="$ROOT_DIR/files"

mkdir -p "$OUT_DIR"

if ! command -v typst >/dev/null 2>&1; then
  echo "typst is not installed."
  echo "Options:"
  echo "  - Install locally (macOS): brew install typst"
  echo "  - Or open $CV_DIR/Leandro_Di_Bella_CV.typ in https://typst.app and export PDF"
  exit 1
fi

typst compile --root "$ROOT_DIR" "$CV_DIR/Leandro_Di_Bella_CV.typ" "$OUT_DIR/cv.pdf"

echo "Wrote: $OUT_DIR/cv.pdf"