# <slug>: script + beats

Voice, length, language, CTA and checkpoints come from the project's files. Mode, look and sources go here.

## Beats

| # | cue (spoken word) | type | on screen (element · motion · layout · style · timing; copy quoted) | seam | hold (2nd change if > 3 s) | sound |
|---|---|---|---|---|---|---|
| 1 | | HOOK | | frame 0 | | |

`type`: HOOK · EXPLAIN · STEP · PROOF · TURN · CTA (rename to the project's style sheet).
`cue`: the spoken word only (occurrence if repeated); `~s` estimates go in notes.
`seam`: `<block> 0.4 s` (for example `whip-pan 0.4 s`), `carry: <element>` or `continuous`.
Write sequencing out in `on screen`: "X fully out by <cue>+0.2 s; at <cue>+0.2 s Y lands".

## Spec line (top of the file)

`<duration> <width>x<height> @ <fps>` · captions: <one style + why> · music: <mood, level> · negatives: <for example "no image files", "no audio at all">

## Self-check

- [ ] hook lands in the first ~2 s, subject on screen at frame 0
- [ ] every cue word exists in the word timestamps
- [ ] every beat > 3 s has a second change in `hold`
- [ ] 3–5 transition kinds, none a fade-out then fade-in
- [ ] on-screen copy quoted exactly; sequencing written out
- [ ] music has a level; SFX sit on named moments
- [ ] overshoot only on in-scene objects, never on text, icons, chips, buttons or numbers
