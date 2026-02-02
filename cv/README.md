# CV (PDF)

This folder contains two ways to produce a polished CV PDF:

1) **Typst (recommended)** — fast, modern, no multi‑GB TeX toolchain.
2) **LaTeX** — traditional workflow (kept for compatibility).

## Typst (recommended)

### Option A: Web (fastest)

- Open `cv/Leandro_Di_Bella_CV.typ` in https://typst.app
- Export as PDF
- Save as `files/cv.pdf` (so it’s served by GitHub Pages)

### Option B: Local build (macOS)

```bash
brew install typst
chmod +x cv/build_typst.sh
./cv/build_typst.sh
```

This produces `files/cv.pdf`.

## LaTeX

### Build (Docker)

From the repo root:

```bash
docker run --rm -v "$PWD":/work -w /work texlive/texlive:latest \
  pdflatex -interaction=nonstopmode -halt-on-error -output-directory cv cv/Leandro_Di_Bella_CV.tex

docker run --rm -v "$PWD":/work -w /work texlive/texlive:latest \
  pdflatex -interaction=nonstopmode -halt-on-error -output-directory cv cv/Leandro_Di_Bella_CV.tex
```

Then copy to the website download location:

```bash
cp cv/Leandro_Di_Bella_CV.pdf files/cv.pdf
```

### Build (local TeX)

If you have TeX Live installed:

```bash
pdflatex -interaction=nonstopmode -halt-on-error -output-directory cv cv/Leandro_Di_Bella_CV.tex
pdflatex -interaction=nonstopmode -halt-on-error -output-directory cv cv/Leandro_Di_Bella_CV.tex
cp cv/Leandro_Di_Bella_CV.pdf files/cv.pdf
```
