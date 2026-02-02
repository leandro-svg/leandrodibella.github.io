#!/usr/bin/env bash
set -euo pipefail

root_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$root_dir"

image="texlive/texlive:latest"
tex="cv/Leandro_Di_Bella_CV.tex"

mkdir -p cv files

docker run --rm -v "$PWD":/work -w /work "$image" \
  pdflatex -interaction=nonstopmode -halt-on-error -output-directory cv "$tex"

docker run --rm -v "$PWD":/work -w /work "$image" \
  pdflatex -interaction=nonstopmode -halt-on-error -output-directory cv "$tex"

cp cv/Leandro_Di_Bella_CV.pdf files/cv.pdf

echo "Wrote files/cv.pdf"
