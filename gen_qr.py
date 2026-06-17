#!/usr/bin/env python3
"""Generate QR SVG files for each language audio and embed them in the card HTML files."""

import io
import re

import qrcode
import qrcode.image.svg

BASE = "https://lazy-language-club-belgrade.netlify.app/materials/audio/"

# (lang_code, audio_file, card_file, svg_size_px)
# size = box_px - 2*padding_px: A6 box=36 pad=2 → 32; A3 box=58 pad=4 → 50
cards = [
    ("en", "en_full.mp3", "card-EN-A6.html", 32),
    ("it", "it_full.mp3", "card-IT-A3.html", 50),
    ("fr", "fr_full.mp3", "card-FR-A3.html", 50),
    ("es", "es_full.mp3", "card-ES-A3.html", 50),
    ("sr", "sr_full.mp3", "card-SR-A3.html", 50),
    ("tr", "tr_full.mp3", "card-TR-A3.html", 50),
    ("ru", "ru_full.mp3", "card-RU-A3.html", 50),
]

for code, mp3, card_file, size in cards:
    url = BASE + mp3

    # Generate QR as SVG
    img = qrcode.make(
        url,
        image_factory=qrcode.image.svg.SvgPathImage,
        error_correction=qrcode.constants.ERROR_CORRECT_M,
    )
    buf = io.BytesIO()
    img.save(buf)
    svg_str = buf.getvalue().decode("utf-8")

    # Save standalone SVG file (for manual use / PDF redesign)
    with open(f"materials/qr-{code}.svg", "w", encoding="utf-8") as f:
        f.write(svg_str)

    # Prepare inline SVG: strip XML declaration, set explicit pixel size
    inline = re.sub(r"<\?xml[^>]*\?>\s*", "", svg_str).strip()
    inline = re.sub(r'(<svg\b[^>]*?)\s+width="[^"]*"', r"\1", inline)
    inline = re.sub(r'(<svg\b[^>]*?)\s+height="[^"]*"', r"\1", inline)
    inline = inline.replace("<svg ", f'<svg width="{size}" height="{size}" ', 1)

    # Read card HTML
    with open(f"materials/{card_file}", encoding="utf-8") as f:
        html = f.read()

    # Replace placeholder div content with inline SVG
    html = re.sub(
        r'<div class="qr">[^<]*(?:<br>[^<]*)?</div>',
        f'<div class="qr" style="padding:2px;overflow:hidden;">{inline}</div>',
        html,
    )

    with open(f"materials/{card_file}", "w", encoding="utf-8") as f:
        f.write(html)

    print(f"OK  qr-{code}.svg  +  {card_file}")

print("QR generation complete.")
