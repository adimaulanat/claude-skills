#!/usr/bin/env python3
# Example build from the Tedja Coffee Kiara Artha review (21 Nov 2026). Edit U (footage folder), PHOTO and segs.
"""Build review-tedja-kiara-artha v1 (no VO, no music). 1080x1920, 30 fps."""
import subprocess, os, re
from PIL import Image, ImageDraw, ImageFont, ImageFilter

U = "/mnt/user-data/uploads"
W = "/home/claude/w"
OUT = f"{W}/seg"; os.makedirs(OUT, exist_ok=True)
os.makedirs(f"{W}/txt", exist_ok=True)

def src(name):
    for f in os.listdir(U):
        if name in f: return f"{U}/{f}"
    raise FileNotFoundError(name)

PHOTO = {"IMG_0105": "e29eb37c-image.jpg", "IMG_0107": "1bb5c661-image.jpg"}

FB = "/usr/share/fonts/truetype/google-fonts/Poppins-Bold.ttf"
FM = "/usr/share/fonts/truetype/google-fonts/Poppins-Medium.ttf"
FE = "/usr/share/fonts/truetype/noto/NotoColorEmoji.ttf"
EMO = re.compile("[\U0001F300-\U0001FAFF☀-➿⭐️]+")

def runs(s):
    out, i = [], 0
    for m in EMO.finditer(s):
        if m.start() > i: out.append(("t", s[i:m.start()]))
        e = m.group().replace("️", "")
        if e: out.append(("e", e))
        i = m.end()
    if i < len(s): out.append(("t", s[i:]))
    return out

def emoji_img(ch, size):
    f = ImageFont.truetype(FE, 109)
    im = Image.new("RGBA", (140, 140), (0, 0, 0, 0))
    ImageDraw.Draw(im).text((0, 0), ch, font=f, embedded_color=True)
    im = im.crop(im.getbbox())
    return im.resize((int(im.width * size / im.height), size), Image.LANCZOS)

def line_img(s, font, size):
    f = ImageFont.truetype(font, size)
    parts, w, h = [], 0, int(size * 1.35)
    for kind, t in runs(s):
        if kind == "t":
            tw = int(f.getlength(t)); parts.append((kind, t, tw)); w += tw
        else:
            for ch in t:
                e = emoji_img(ch, int(size * 0.95)); parts.append(("e", e, e.width + 6)); w += e.width + 6
    im = Image.new("RGBA", (max(w, 1), h), (0, 0, 0, 0)); d = ImageDraw.Draw(im); x = 0
    for kind, t, tw in parts:
        if kind == "t": d.text((x, int(size * 0.12)), t, font=f, fill="white")
        else: im.alpha_composite(t, (x + 3, int((h - t.height) / 2)))
        x += tw
    return im

def card(lines, path, center_y, box=False):
    """lines: list of (text, font, size, gap_after)"""
    canvas = Image.new("RGBA", (1080, 1920), (0, 0, 0, 0))
    imgs = [(line_img(t, f, s), g) for t, f, s, g in lines]
    total = sum(i.height + g for i, g in imgs)
    y = int(center_y - total / 2)
    layer = Image.new("RGBA", canvas.size, (0, 0, 0, 0))
    for im, g in imgs:
        layer.alpha_composite(im, ((1080 - im.width) // 2 - 20, y)); y += im.height + g
    if box is True:
        bb = layer.getbbox(); pad = 34
        bx = Image.new("RGBA", canvas.size, (0, 0, 0, 0))
        ImageDraw.Draw(bx).rounded_rectangle((bb[0]-pad, bb[1]-pad, bb[2]+pad, bb[3]+pad), 28, fill=(0, 0, 0, 120))
        canvas.alpha_composite(bx)
    if box is False:
        bb = layer.getbbox(); band = Image.new("RGBA", canvas.size, (0, 0, 0, 0))
        ImageDraw.Draw(band).rounded_rectangle((bb[0]-70, bb[1]-50, bb[2]+70, bb[3]+50), 60, fill=(0, 0, 0, 105))
        canvas.alpha_composite(band.filter(ImageFilter.GaussianBlur(38)))
    a = layer.split()[3]
    sh = Image.new("RGBA", canvas.size, (0, 0, 0, 0)); sh.putalpha(a.point(lambda v: v * 0.55))
    sh = sh.filter(ImageFilter.GaussianBlur(8 if box is not None else 5))
    canvas.alpha_composite(sh, (0, 4)); canvas.alpha_composite(layer)
    canvas.save(path)

TXT = 1190  # ~62% from top
segs = [
  # id, kind, source, start, dur, speed, text lines, center_y, box
  ("01", "v", "IMG_0106", 0.0, 3.5, 3.2/3.5,
   [("COFFEE SHOP", FB, 96, 0), ("HIDDEN GEM", FB, 96, 0), ("DI BANDUNG", FB, 96, 18),
    ("Tedja Coffee x Invalogi, dekat Kiara Artha Park", FM, 38, 0)], 780, False),
  ("02", "p", "IMG_0105", 0, 3.0, 1, [("agak ngumpet, depan pintu masuk", FM, 50, 0), ("Kiara Artha Park 📍", FM, 50, 0)], TXT, False),
  ("03", "v", "IMG_0116", 0.4, 4.0, 1, [("dinding cermin = spot foto 🪞", FM, 52, 0)], TXT, False),
  ("04", "v", "IMG_0113", 0.0, 3.5, 1, [("semi-outdoor garis kuning 💛", FM, 52, 0)], TXT, False),
  ("05a", "v", "IMG_0108", 0.0, 2.3, 1, [("ruang bundar buat kerja", FM, 52, 0), ("colokan di bangku 🔌", FM, 52, 0)], TXT, False),
  ("05b", "p", "IMG_0107", 0, 1.7, 1, [("ruang bundar buat kerja", FM, 52, 0), ("colokan di bangku 🔌", FM, 52, 0)], TXT, False),
  ("06a", "v", "IMG_0118", 0.0, 1.9, 1, [("outdoor-nya ijo & adem 🌿", FM, 52, 0)], TXT, False),
  ("06b", "v", "IMG_0119", 0.0, 1.6, 1, [("outdoor-nya ijo & adem 🌿", FM, 52, 0)], TXT, False),
  ("07", "v", "IMG_0117", 0.0, 2.45, 1, [("mushola ✔", FM, 56, 0)], TXT, False),
  ("08", "v", "IMG_0109", 0.0, 3.6, 1, [("indoor buat laptopan 💻", FM, 52, 0)], TXT, False),
  ("09", "v", "IMG_0114", 0.0, 4.4, 1,
   [("Tedja Coffee Kiara Artha", FB, 58, 14), ("kopi mulai Rp20 rb", FM, 42, 4), ("±Rp25–50 rb/orang", FM, 42, 4),
    ("buka tiap hari 07.00–22.00", FM, 42, 4), ("📍Jl. Banten No.10a, Bandung", FM, 42, 30),
    ("kamu tim indoor", FB, 62, 0), ("atau outdoor?", FB, 62, 0)], 900, None),
]

GRADE = "eq=contrast=1.06:saturation=1.12:brightness=0.01,unsharp=5:5:0.6:5:5:0.0"

def sh(cmd):
    r = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if r.returncode: print(r.stderr[-2000:]); raise SystemExit(cmd)

for sid, kind, name, ss, dur, speed, lines, cy, box in segs:
    png = f"{W}/txt/{sid}.png"; card(lines, png, cy, box)
    out = f"{OUT}/{sid}.mp4"
    fade = "format=rgba,fade=t=in:st=0:d=0.25:alpha=1" if sid not in ("01", "05b", "06b") else "format=rgba"
    if kind == "v":
        f = src(name); srcdur = dur * speed
        trf = f"{W}/{sid}.trf"
        sh(f"ffmpeg -v error -y -ss {ss} -t {srcdur+0.2} -i '{f}' -vf vidstabdetect=shakiness=6:result={trf} -f null -")
        vf = (f"[0:v]vidstabtransform=input={trf}:smoothing=18:optzoom=1:interpol=bicubic,"
              f"scale=1080:1920:flags=lanczos,setpts=PTS/{speed},{GRADE}{',eq=brightness=-0.09,vignette=PI/4' if sid=='09' else ''},fps=30,format=yuv420p[v];"
              f"[1:v]{fade}[t];[v][t]overlay=0:0:shortest=1,format=yuv420p[o]")
        sh(f"ffmpeg -v error -y -ss {ss} -t {srcdur} -i '{f}' -loop 1 -t {dur} -i {png} "
           f"-filter_complex \"{vf}\" -map [o] -an -t {dur} -r 30 -c:v libx264 -preset veryfast -crf 16 {out}")
    else:
        f = f"{U}/{PHOTO[name]}"; n = int(dur * 30)
        # 1932x2576 -> 9:16 crop 1449x2576, upscale for smooth Ken Burns, zoom 1.00 -> 1.07
        vf = (f"[0:v]crop=1449:2576:(iw-1449)/2:0,scale=2160:3840:flags=lanczos,"
              f"zoompan=z='1+0.07*on/{n}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d={n}:s=1080x1920:fps=30,"
              f"{GRADE},format=yuv420p[v];[1:v]{fade}[t];[v][t]overlay=0:0:shortest=1,format=yuv420p[o]")
        sh(f"ffmpeg -v error -y -i '{f}' -loop 1 -t {dur} -i {png} -filter_complex \"{vf}\" "
           f"-map [o] -frames:v {n} -r 30 -c:v libx264 -preset veryfast -crf 16 {out}")
    print("ok", sid)

with open(f"{W}/list.txt", "w") as fh:
    for s in segs: fh.write(f"file '{OUT}/{s[0]}.mp4'\n")
sh(f"ffmpeg -v error -y -f concat -safe 0 -i {W}/list.txt -c copy {W}/video_noaudio.mp4")
# silent stereo track so every platform accepts the upload; sound is added in-app
sh(f"ffmpeg -v error -y -i {W}/video_noaudio.mp4 -f lavfi -i anullsrc=r=48000:cl=stereo -shortest "
   f"-c:v copy -c:a aac -b:a 128k -movflags +faststart {W}/review-tedja-kiara-artha-v1.mp4")
print("done")
