---
name: mirroring-reference-video
description: Use when someone shares a reference video, ad, Reel, Short or TikTok (link or file) and wants their own video to follow its structure, pacing or visual style
---

# Mirroring a reference video

Copy the reference's structure and visual grammar, never its content. Everything about the project is discovered or asked, never assumed.

## 0. Discover first

Read the project's instruction files (CLAUDE.md, AGENTS.md, README, docs). Note what they define: design system and default look, scaffold command, lint/render commands, voice tool and its cost rule, git-ignored folders for raw media, language, format, length, CTA, publishing rules. Each item not found goes on the question list. Never fill it from memory, another project or a "sensible default".

## Steps

1. **Reference.** If the link needs a login, ask for the file. Keep the file and its contact sheets only in a git-ignored folder the project names (or ask which). Probe length, size and frame rate, then make a contact sheet with the project's tools. Never upload the reference anywhere without explicit consent; describe it in words.
2. **Beat map.** Fill the tables in `beat-map.md`: time, layout, text pattern, motion, job of each beat. List what is borrowed and what is not (its text, logo, footage, music, handle, product).
3. **Decision round.** Ask only what step 0 did not answer, at most 4 questions per round, as many rounds as needed (use the harness's ask tool if it has one): restructure or restyle; new sibling video or in place; format, length, language and CTA if undefined; new script or reuse an existing voice-over. **Always ask: "Make a design concept board for the look?"** No → use the project's default look, named as the project names it; if there is none, ask. Yes → step 5b.
4. **Scaffold** with the project's command, or ask how new videos are made.
5. **Brief and script.** In the project's files: why this version exists, the borrowed grammar, dated decisions, then the voice and beats tables from `beat-map.md`.
   **5b. Board.** Confirm every input in `opendesign-inputs.md` before starting the run. A blank input is a question, never a gap you fill. Then follow that file's run steps.
6. **Approval.** Stop until the person approves the script wording, the voice (confirm its name read-only from the voice tool when possible), the cost estimate by the project's cost rule, and the concept pick if 5b ran.
7. **Voice-over.** Generate with the project's tool, or reuse the existing one. Set beat times from the word timings.
8. **Screen clips.** Crop each to its card region. Scan every crop for leaked data (counters, emails, account names, stale text, labels that contradict the voice) and report findings.
9. **Compose.** Load the project's video-framework skill or docs, then build from the project's kit and design system.
10. **Lint and check** with the project's commands. Fix warnings. Snapshot the middle of every beat and fix layout bugs.
11. **Render and review** frame by frame (leaks, typos, safe areas, numbers); check the audio does not clip. Move bad renders where the project says, or ask. Never delete.
12. **Handover** by the project's definition of done: post copy if it uses any, an AI-content label reminder when synthetic voice or footage was used, open issues. Never publish.

A longer cut of the same video: reuse the full voice-over, add beats, repeat from step 5.

## Red flags: stop and ask

| Thought | Reality |
|---|---|
| "I'll use the look from last time" | The project's files name the look, or you ask |
| "Vertical, 30 s, English is the usual" | Format, length and language come from the project or the person |
| "The credits are small, generate now" | Not before the approval step |
| "Uploading the reference is faster" | Needs explicit consent |
| "I'll fill the board gap myself" | A gap is a question |

## Common mistakes

- An emoji wraps onto a line by itself: glue it to the last word.
- A count-up shows a static "0" before it starts: hide it until it counts.
- Muted text on a light card is unreadable: use the card's ink colour.
- A joining word ("or") overlaps two cards: make it a small badge between them.
- A fixed-length background ends before the video does: size it to the full length.
