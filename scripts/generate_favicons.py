from __future__ import annotations

from pathlib import Path

from PIL import Image


def main() -> None:
    repo_root = Path(__file__).resolve().parents[1]
    src = repo_root / "images" / "profile_picture.png"

    if not src.exists():
        raise SystemExit(f"Source image not found: {src}")

    img = Image.open(src).convert("RGBA")

    # Ensure square crop (safe even if the source changes later)
    size = min(img.size)
    left = (img.size[0] - size) // 2
    top = (img.size[1] - size) // 2
    img = img.crop((left, top, left + size, top + size))

    outputs: dict[Path, tuple[int, int]] = {
        repo_root / "images" / "favicon-32x32.png": (32, 32),
        repo_root / "images" / "favicon-192x192.png": (192, 192),
        repo_root / "images" / "favicon-512x512.png": (512, 512),
        repo_root / "images" / "apple-touch-icon-180x180.png": (180, 180),
    }

    for out_path, (w, h) in outputs.items():
        resized = img.resize((w, h), Image.Resampling.LANCZOS)
        out_path.parent.mkdir(parents=True, exist_ok=True)
        resized.save(out_path, format="PNG", optimize=True)

    ico_path = repo_root / "images" / "favicon.ico"
    ico_sizes = [(16, 16), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)]
    img_ico = img.resize((256, 256), Image.Resampling.LANCZOS)
    img_ico.save(ico_path, format="ICO", sizes=ico_sizes)

    print("Wrote favicons:")
    for out_path in outputs:
        print(f"- {out_path.relative_to(repo_root)}")
    print(f"- {ico_path.relative_to(repo_root)}")


if __name__ == "__main__":
    main()
