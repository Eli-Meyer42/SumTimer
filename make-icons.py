"""Regenerate the app icons. Edit the drawing, then: python3 make-icons.py"""
from PIL import Image, ImageDraw

BG = (21, 33, 42, 255)        # ink
RING = (237, 240, 234, 255)   # light
CD = (194, 76, 112, 255)      # cooldown pink
OK = (63, 164, 119, 255)      # ready green

def icon(size, maskable=False):
    S = size * 4                                   # draw big, shrink for smooth edges
    img = Image.new('RGBA', (S, S), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    if maskable:
        d.rectangle([0, 0, S, S], fill=BG); pad = S * 0.27
    else:
        d.rounded_rectangle([0, 0, S, S], radius=S * 0.22, fill=BG); pad = S * 0.17
    w = S - pad * 2
    cx, cy, r = S / 2, pad + w * 0.56, w * 0.40
    # stopwatch button on top
    d.rounded_rectangle([cx - w*0.07, pad + w*0.02, cx + w*0.07, pad + w*0.14], radius=w*0.03, fill=RING)
    # face
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=RING)
    ri = r * 0.80
    # cooldown wedge (most of the face) and the ready slice
    d.pieslice([cx - ri, cy - ri, cx + ri, cy + ri], -90, 200, fill=CD)
    d.pieslice([cx - ri, cy - ri, cx + ri, cy + ri], 200, 270, fill=OK)
    # hand
    d.line([cx, cy, cx, cy - ri * 0.95], fill=RING, width=int(w * 0.05))
    d.ellipse([cx - w*0.05, cy - w*0.05, cx + w*0.05, cy + w*0.05], fill=RING)
    return img.resize((size, size), Image.LANCZOS)

for s in (192, 512):
    icon(s).save(f'icon-{s}.png')
icon(512, maskable=True).save('icon-maskable-512.png')
icon(180).save('apple-touch-icon.png')
print('icons written')
