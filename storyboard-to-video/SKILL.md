---
name: storyboard-to-video
description: Use when someone hands over a storyboard, scene-by-scene image or video generation prompts, or a scene list plus a voice-over script, and wants one narrated video (Short, Reel, TikTok, explainer) built from them, drawn in code instead of AI-generated footage
---

# Storyboard to Video

Turn scene prompts plus a voice-over (VO) script into one narrated 9:16 explainer video, drawn in code (HyperFrames: HTML + GSAP). The voice sets the clock; the prompts supply the pictures. Beats, seams, captions and motion come from `narrated-shorts`; copy from `writing-platform-copy`. This skill covers what happens before and after the build.

## 0. Discover first

Read the project's instruction files for look, commands, voice tool, language, length, checkpoints and QA gates. They win over this skill. A gap becomes a question. A deadline never removes a checkpoint. If an earlier session left a plan, follow it.

## 1. One concept from the prompts

Prompt timecodes are hints; the VO sets timing through cue words. Fill in `concept-sheet.md`: palette, characters, props per scene, layout, motion, bans. Take the brand palette from a brand-data tool if one exists and note the date. The user's font choice overrides the brand font. Use no official crest, logo or real photo unless the channel is the official account; draw stand-ins and write the name as text.

## 2. Fact-check before scaffolding

Source every number and claim, primary document first, and show the arithmetic. Write the rulings table (`fact-check.md`). The user's VO file stays untouched and no wording changes without their OK. Keep every scene the user asked for: when a visual lacks data, label it ("illustration, not to scale", no number) instead of cutting it.

## 3. Script slots

- First sentence is the hook (≤ 8 words); offer alternatives as variants.
- If the VO ends without a specific reason to follow, propose one.
- Spell numbers and years as spoken; respell acronyms a TTS may misread.
- Captions use a display map (capitalised names, highlight words) apart from the spoken text.
- Changing one word means a new take; cues re-time and the user listens again.

## 4. Build and QA

Build with the project's commands, then run its critique loop: fix the three worst problems per round, up to the cap. Report the score history as it is. At the cap, the user decides. Fixes by symptom: `qa-fixes.md`.

## 5. Copy and repurpose

Write copy after the cut is approved. Prefer a sourced title over a higher-scoring one that implies an unsourced claim. Re-check volatile facts (standings, prices) on posting day. Never publish.

## Red flags

| Thought | Reality |
|---|---|
| "No time to ask, I'll rewrite the VO" | Table every change, keep the original, user approves |
| "Unsourced, so cut the scene" | Keep it, label it |
| "Add the crest so it looks official" | Only on an official account |
| "Pad the VO to the prompt's 90 s" | Time follows the VO |
| "Dominant / officially / jackpot" | Say what the source says |
| "89 is basically 90" | Report 89; the user decides |
