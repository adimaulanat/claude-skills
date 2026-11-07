---
name: narrated-shorts
description: Use when making or revising a narrated vertical (9:16) Short, Reel or TikTok explainer in HyperFrames, from beats table to render, or when feedback on a render says a scene is dead, too fast, jumps at a cut, or looks like AI slop
---

# Narrated Shorts

A voice-led 9:16 video where the voice sets the clock and the picture follows it. The project owns its process; this skill adds the prompt-level detail agents leave out.

## 0. Discover first

Read the project's instruction files (CLAUDE.md, AGENTS.md, README, docs) for: look and design system, scaffold/check/render commands, voice tool and cost rule, language, length, CTA, checkpoints, QA gates. What they define wins over this skill. A gap becomes a question, never a guess. Never skip a checkpoint the project defines, whatever the deadline.

## 1. Beats table (the deliverable)

Write beats with `beats-template.md`; every column is required. Copy the columns exactly:

- **cue**: the spoken word that starts the beat (add the occurrence if the word repeats). Times come from word timestamps, never typed seconds; a `~s` length estimate belongs in a note, never in the cue cell.
- **on screen**: one sentence per element with five slots: element · motion · layout · style · timing. On-screen text is quoted exactly, `/` for a line break.
- **seam**: how this beat replaces the last. A named transition block + duration, `carry: <element>` when one element stays across the cut, or `continuous` when the same shot runs on.
- **hold**: what keeps the beat alive. Any beat longer than 3 s lists a second change inside it.
- **sound**: SFX on this beat's moments, or `-`.

The HOOK beat's subject is already in frame at 0.0 s with `seam` = `frame 0`: animate what happens to it, never its arrival.

Sequencing is written out: "the counter is fully out by 4.2 s; at 4.2 s READY stamps in", never "fades out and READY stamps in".

## 2. Choose once per video

| Decision | Rule |
|---|---|
| Transitions | 3–5 kinds in the whole film; energy matches the beat (calm 0.5–0.8 s, medium 0.3–0.5 s, high 0.15–0.3 s). Never fade out then fade in; never a dissolve between unrelated beats. |
| Captions | One style, chosen by tone (hype, clean, elegant, tech, karaoke), built from word timestamps, kept inside the safe zone. |
| Audio | Voice first. Music named with a level ("under -18 dB", "ducked ~12 dB under the voice"), SFX cued to moments, never sprinkled. "No narration" is not silence; say "no audio at all". |
| Overshoot | Only on an object that exists in the scene (phone, card, sticker). Never on text, labels, icons, chips, buttons, counters or numbers: a drawn button is UI even if it looks physical, and lands with `power4.out`. |

Details and phrase tables: `prompting.md`.

## 3. Build and check

Scaffold, voice, transcribe, cue, scenes, captions, outro, check, snapshot the middle of every beat, render, all with the project's commands. Stop at each project checkpoint. Never publish.

## 4. Feedback on a render

Turn the feedback into an edit list before touching anything. One row per edit:

`target (beat, timestamp) | current value | new absolute value | frozen`

- One variable per row; apply and check one row at a time.
- New values are absolute ("glow at 35% peak opacity"), never "less" or "half".
- Every list ends with a **frozen** line naming what must not change.
- A mismatch between feedback and the table (cut at 4.2 s, table says 4.0 s) is diagnosed with snapshots before any fix.
- "Dead scene" means: what changes every 2–3 s in this beat? Add that, nothing else.

## Red flags

| Thought | Reality |
|---|---|
| "The beat is clear enough in prose" | Fill all five slots or the agent designs the rest |
| "It cross-fades fine" | A fade-out then fade-in reads as a jump cut with a dip |
| "Subtle breathing keeps it alive" | Give the second change a job or shorten the beat |
| "Fix all three notes in one pass" | One variable per edit, or you cannot tell what broke |
| "Make it less strong" | State the absolute number |
| "It's a physical button / chip" | Drawn UI is UI: no overshoot |
| "Deadline, skip the checkpoint" | The project's checkpoints stay |
