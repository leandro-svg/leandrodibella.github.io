from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


def main() -> None:
    repo_root = Path(__file__).resolve().parents[1]

    out_path = repo_root / "images" / "og-image.png"
    avatar_path = repo_root / "images" / "profile_picture.png"

    W, H = 1200, 630

    # Colors
    bg1 = (15, 23, 42)  # slate-900
    bg2 = (19, 78, 74)  # teal-900
    accent = (45, 212, 191)  # teal-400
    text = (248, 250, 252)  # slate-50
    muted = (203, 213, 225)  # slate-300

    img = Image.new("RGBA", (W, H), bg1)
    draw = ImageDraw.Draw(img)

    # Vertical gradient
    for y in range(H):
        t = y / (H - 1)
        r = int(bg1[0] * (1 - t) + bg2[0] * t)
        g = int(bg1[1] * (1 - t) + bg2[1] * t)
        b = int(bg1[2] * (1 - t) + bg2[2] * t)
        draw.line([(0, y), (W, y)], fill=(r, g, b, 255))

    # Avatar
    avatar = Image.open(avatar_path).convert("RGBA")
    avatar = avatar.resize((260, 260), Image.Resampling.LANCZOS)

    mask = Image.new("L", (260, 260), 0)
    ImageDraw.Draw(mask).ellipse((0, 0, 259, 259), fill=255)
    avatar.putalpha(mask)

    ax, ay = 80, (H - 260) // 2
    img.alpha_composite(avatar, (ax, ay))

    ring = Image.new("RGBA", (280, 280), (0, 0, 0, 0))
    rd = ImageDraw.Draw(ring)
    rd.ellipse((5, 5, 275, 275), outline=accent + (200,), width=6)
    img.alpha_composite(ring, (ax - 10, ay - 10))

    # Fonts (fallback to default)
    def _font(path: str, size: int) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
        try:
            return ImageFont.truetype(path, size)
        except Exception:
            return ImageFont.load_default()

    title_font = _font("/System/Library/Fonts/SFNSDisplay.ttf", 72)
    subtitle_font = _font("/System/Library/Fonts/SFNSDisplay.ttf", 34)
    small_font = _font("/System/Library/Fonts/SFNSDisplay.ttf", 26)

    tx = ax + 320
    ty = 180

    draw.text((tx, ty), "Leandro Di Bella", fill=text, font=title_font)
    draw.text((tx, ty + 92), "Computer vision & generative AI", fill=muted, font=subtitle_font)
    draw.text((tx, ty + 140), "Detection • Tracking • VLMs • Forecasting", fill=muted, font=small_font)
    draw.rounded_rectangle((tx, ty + 210, tx + 520, ty + 218), radius=4, fill=accent + (230,))

    out_path.parent.mkdir(parents=True, exist_ok=True)
    img.convert("RGB").save(out_path, format="PNG", optimize=True)
    print(f"Wrote {out_path.relative_to(repo_root)}")


if __name__ == "__main__":
    main()
