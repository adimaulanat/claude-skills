---
name: cafe-review-video
description: Turn cafe/place footage + a Google Maps link into a CSI- and CapCut-backed review script and per-platform copy for confirmation, then render the vertical video after approval.
---

# Cafe / place review video (TikTok, Reels, FB Pro, Shorts)

Input from the user: footage (videos .mov/.mp4 and/or photos) + a Google Maps link to the place.
Output, phase 1: a brief + script + copywriting per platform for confirmation (⏸ stop). Phase 2 (only after the user approves): the rendered 1080×1920 video + final copy kit.

Read the project's own instruction files first (CLAUDE.md, project instructions, copy-style docs); their rules win over this skill. Write everything to the user in casual Indonesian ("kamu"). Never invent facts, prices, wifi/AC claims or affiliate links; every claim on screen or in a caption needs a named source (Google Maps, official menu, a named Google review, or the user's own footage). Ignore attachments the user says were picked by mistake.

## Phase 1 — Research, script and copy (stop for approval)

### 1. Inventory the footage
- `ffprobe` each video: resolution, fps, duration. Make a 4-frame contact sheet per clip (`fps=4/<dur>,scale=216:384,tile=4x1`) and look at every sheet.
- Photos: note size (iPhone 3:4 = 1932×2576). Map photo names to files by the order the user attached them (attached display order = order of the saved `image.jpg` paths). Double-check by viewing; a wrong mapping happened before.
- Label each clip: what it shows (facade, interior zone, outdoor, mushola, bar, drinks…), usable seconds, people with visible faces (to blur).
- List what's missing (typically: drinks/food, facade/signage).

### 2. Google Maps (in the user's Chrome)
- Open the Maps link. Read with get_page_text: name, rating + review count, price per person (+ "reported by N people"), address, Menu & highlights items, and the review snippets.
- Expand the hours (find the "Show open hours for the week" button; per-day buttons list the hours).
- Pick 2–3 reviews with useful facts (location hint, facilities, parking). Keep reviewer names for the source column.
- Official menu: follow the Menu link (often linktr.ee → a flipbook). Flipbooks are images; search won't work, so page through and zoom. Only use prices you can read clearly; if an item's price is not found, show it without a price.
- Missing footage: Maps photos can't be downloaded into the workspace (googleusercontent is blocked). Offer the user: (a) save "By owner" photos / a highlight photo themselves with a credit line, (b) film it themselves, or (c) replace with existing footage. Default if they skip: replace with their own footage.

### 3. TikTok Creator Search Insights (CSI)
- Web URL: `https://www.tiktok.com/csi/search?keyword=<kw>` (wait ~5 s, then get_page_text). `/tiktokstudio/inspiration` is a different page.
- Search 4–6 keywords: `cafe <city>`, `coffee shop <city>`, `tempat nongkrong <city>`, `cafe aesthetic <city>`, `<area/landmark>`, `<cafe name>`, and an angle that fits the place (e.g. `coffee shop hidden gem <city>`, `wfc cafe <city>`, `library cafe <city>`).
- Record popularity + growth %. Choose the angle where the phrase matches the place AND has growth (a source must back the angle, e.g. a review saying the place is hidden).
- Open the 1–2 best topics (click the topic name) → read Locations, Age, and **Related videos**. Get links with JS: `[...document.querySelectorAll('a')].filter(a=>a.href.includes('/video/')).map(a=>a.href)`.
- Watch the top 3–4 related videos: open each, pause, seek (`v.currentTime=…`) and zoom on the player at ~0.5 s, middle, end. Note: duration, VO or not, title style at frame 0, per-clip text, end card, sound link (`a[href*="/music/"]`), likes/saves/shares.
- **Caption style (for the copy):** from each top related video (and 2–3 more from the main topics), read the full caption (click "more" / get_page_text) and record in a table: opening phrase, how the search phrase is placed, words/slang used (e.g. "hidden gem", "syahdu", "adem", "save dulu", "wajib cobain", "pewe"), emoji (which ones, where, how many), CTA, 📍 location format, hashtags (count + which), caption length. Also note which CSI phrases rank as search terms to put in hashtags.

### 4. CapCut templates
- capcut.com web search for cafe terms returns mostly unrelated templates. Check the known cafe template and record its current uses: **Cafe Visit Vlog** — 8 clips, 0:30, 9:16: https://www.capcut.com/template-detail/aesthetic-cinematic-8clip/7571775010994539829 . Also try 1–2 searches (`cafe vlog`, `hidden gem cafe`) and note any relevant template with clips/duration/uses.
- Blend: clip structure/pacing from the CapCut template (≈8 clips × 3.5–4 s) + hook and text style from the top CSI videos.

### 5. Brief + script + copy ⏸
Save to the project as `claude/brief-review-<slug>.md` with sections: CSI data table · reference videos table · caption-style table · CapCut template table · facts + source table (plus a ❌ do-not-use row) · footage gaps · script table `# | sec | footage | on-screen text (| VO if used)` · **copy per platform** (below) · sound suggestion (sound from the top reference video; added in-app, never rendered).

Default script pattern (≈30–32 s):
1. Frame 0: big 2–3 line uppercase title with the CSI phrase (e.g. "COFFEE SHOP HIDDEN GEM DI BANDUNG") + small subtitle (name, landmark).
2. Location hint (from a review).
3–7. One zone per clip with a short lowercase label + emoji (photo spot, work area + sockets, outdoor, mushola, indoor/bar, drinks if available).
8. End info over footage: name · "kopi mulai RpX rb" · "±RpX–Y rb/orang" · hours · 📍address · one genuine question (e.g. "kamu tim indoor atau outdoor?").

### 6. Copywriting per platform
Write in the voice found in the caption-style table: same kind of opening, the same slang and emoji style (pick emoji the reference captions actually use; don't add emoji they never use; keep to roughly their count). First person "aku" for a personal account. Every fact must be in the facts table. No engagement bait ("like kalau setuju"), no hashtag walls, no unrelated tags. Under each platform block, add one line "Gaya dari: @akun1, @akun2" naming the reference captions it follows.

- **TikTok:** title/hook line (≤ ~60 chars, the CSI phrase first) · caption: sentence 1 = CSI phrase + place hint, then 2–3 highlights, price + hours, a save/visit CTA in the reference style, 📍name + street · 3–5 hashtags mixing the top CSI phrases (e.g. #hiddengembandung #cafebandung #tempatnongkrongbandung) · cover text (≤ 5 words).
- **Instagram Reels:** first ~125 chars carry the hook + CSI phrase (that's what shows before "more") · rest of the caption · 📍 line · ≤ 5 hashtags · cover title · location tag suggestion.
- **Facebook Pro:** sentence 1 = place name + main keyword + hook, keyword appears twice naturally · ≤ ~5 lines · one genuine question · 3 hashtags · native upload of the rendered mp4.
- **YouTube Shorts** (if the account posts there): title ≤ 100 chars with the CSI phrase in the first ~40 chars and 2–3 hashtags at the end of the title · description: first sentence = main keyword in a normal sentence, address + hours, no hashtags in the description · pinned comment = one genuine question.
- Per platform note: AI label ON only if an AI voice-over or AI visuals were used; credit line in the caption if a Maps photo is used ("foto: Google Maps / <nama>").

Then ask with AskUserQuestion (max 3): which account (personal is the default for place reviews) · VO or text + music (top CSI hidden-gem videos usually have no VO) · how to fill missing footage. Stop and wait for approval of the script and the copy.

## Phase 2 — Render (only after approval)

Build with Python + Pillow + ffmpeg in the workspace. `build-example.py` in this folder is the working build from the first video (Tedja Coffee Kiara Artha): copy it, then change the `segs` table (footage, seconds, text) and the photo map.
- Per video clip: `vidstabdetect=shakiness=6` → `vidstabtransform=smoothing=18:optzoom=1:interpol=bicubic`, `scale=1080:1920:flags=lanczos`, grade `eq=contrast=1.06:saturation=1.12:brightness=0.01,unsharp=5:5:0.6:5:5:0.0`, 30 fps. Short clips: slow slightly with `setpts=PTS/<speed>` (keep speed ≥ ~0.9) or pair with a photo.
- Per photo: crop 3:4 → 9:16 (1449×2576 centered), upscale to 2160×3840, `zoompan` 1.00→1.07 over the segment, same grade.
- Text: render PNG overlays with Pillow — Poppins Bold (titles, 96 px) and Poppins Medium (labels 50–52 px, info 42 px), emoji from NotoColorEmoji (size 109, crop + resize), soft drop shadow. Labels centred at y≈1190; title around y≈780. Keep out of the bottom 15% and right 12%.
- Readability: soft blurred dark band behind labels (alpha ~105, blur 38). **No solid black card** — the user rejected it; for the end info darken the clip instead (`eq=brightness=-0.09,vignette=PI/4`) and keep the shadow.
- Labels fade in 0.25 s, but the **title on segment 1 has no fade** (must be fully visible at frame 0). Continuation segments of the same label don't fade again.
- Encode each segment `libx264 -preset veryfast -crf 16`, concat with `-c copy`, add a silent AAC stereo track (`anullsrc`) + `-movflags +faststart`. No music, no VO rendered unless the user chose VO.

QA before sending: contact sheet at each segment (`select=eq(n,…)`, tile) and look at it — title visible at frame 0, every label readable over bright skies/busy walls, correct footage per label, no unblurred faces, 1080×1920 30 fps, ≤ 35 s. Re-check the copy against the final cut: anything replaced or cut from the video (e.g. a drink shot) is also removed from the captions.

Deliver: the mp4 with SendUserFile + the final copy kit (all platforms) in the reply or the brief doc, a short summary of what was replaced and the HD steps, and upload notes (sound in-app at 10–15%; AI label only if AI VO or AI visuals are used). Update the brief doc status in the project (decisions, what was replaced, final copy).