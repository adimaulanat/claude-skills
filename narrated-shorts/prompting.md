# Prompting HyperFrames for better videos

Condensed from the HyperFrames docs (hyperframes.heygen.com/prompting/*, checked 7 Nov 2026). Use it when writing beats, briefing a video agent, or giving feedback on a render.

## Prompt skeleton

Every part removes a decision an agent usually gets wrong.

```
[route]      /hyperframes            (own agent only; without it the agent guesses HTML video conventions)
[spec]       45-second 1080x1920 video.      (defaults: 30 fps; do not ask for 4K/60fps on social clips)
[beats]      Beat 1 (0-4s): ...  Beat 2 (4-9s): ...      (timestamps + pacing, e.g. "then hold")
[copy]       exact on-screen text in quotes, "/" for a line break
[technique]  Adapt the `code-typing` and `vfx-shatter` registry blocks.   (starting points, not drop-ins)
[negatives]  No image or media files.   ("no narration" is not silence; say "no audio at all")
```

## Five slots per beat element

One sentence per element, any order: **element** (what is on screen) · **motion** (what it does) · **layout** (where it sits) · **style** (how it looks) · **timing** (when, inside the beat). An element you do not describe is designed by the agent.

## Specification dial

1. Mood words ("warm, minimal"): fast, the agent owns the look.
2. Style tokens (exact hex, named texture, type direction): cheap precision, no downside.
3. Full visual spec per element: use when recreating a specific look.

Density never hurts. Always pin two things: **3D** ("Three.js via the adapter"; CSS perspective reads flat) and **sequencing** (write it out: "counter fully out by 4.2 s; at 4.2 s READY stamps in", never "fades out and READY stamps in").

## Iteration

- One variable per edit. Give timestamps.
- Layer one element type at a time: subject and its motion, then camera, then background motion, then style.
- Strip, then re-layer when a scene keeps misfiring.
- Absolute targets, not relative fixes: "glow at ~35% peak opacity, always subtler than the orb", not "glow too strong"; "dot radius = 25% of row spacing", not "2x finer".
- Freeze what works: "framing and motion are right, do not touch them; only change the dot size."
- Never paste raw error logs; say what `check` reports. Name assets by path (`use assets/logo.svg`).

## Motion

| Symptom | Say |
|---|---|
| too fast | "Too fast. Slow the zooms and pans." |
| drags | "Speed this up." |
| titles keep moving | "Land the titles, then hold them still." |
| feels like slides | "Carry one thing across each cut." |
| all at once | "Bring things in one after another, on the voice." |
| bouncy, cheap | "No bounce on text or UI." |
| jump at a cut | "There is a jump at 4.2 s." |
| dead scene | "Scene 3 is dead. Give it something to do." |

- Move only what is live: once landed, hold still, and only what the data changes moves. Never ask for "subtle breathing" to fill time. Every second needs a job.
- A camera move must travel between things; a push-in for its own sake does not earn its place.
- Overlap sequential events (stagger), existing things appear together. One idea per move.
- Overshoot (weight) only for physical objects (cards, flaps), never text, UI or numbers.
- Depth: far layers slower, near faster; one blurred foreground object is the strongest cue.
- Randomness is seeded; hold positions in frames ("exactly two frames"), not seconds.
- Ease words: smooth `power2.out`, snappy `power4.out`, bouncy `back.out`, springy `elastic.out`, dramatic `expo.out`, dreamy `sine.inOut`. Duration: 0.2 s energy, 0.4 s professional, 0.6 s luxury, 1-2 s cinematic.

## Transitions

Use 3-5 kinds per film, each where it fits. Never a dissolve between unrelated scenes. Name the block and the seam ("`cross-warp-morph` from scene 1 to scene 2"). Never fade one scene out and the next in (reads as a jump cut with a dip).

| Energy | Shader blocks | CSS blocks | Duration |
|---|---|---|---|
| Calm | `cross-warp-morph`, `light-leak` | `transitions-blur` | 0.5-0.8 s |
| Medium | `whip-pan`, `cinematic-zoom` | `transitions-push`, `transitions-cover` | 0.3-0.5 s |
| High | `ridged-burn`, `glitch`, `chromatic-radial-split` | `transitions-scale`, `transitions-light` | 0.15-0.3 s |

Shader transitions and VFX beats (`vfx-shatter`, `vfx-portal`, ...) are for two or three beats, not a whole video. Name the exact effect ("explode", "burst" do not map).

## Voice, music, sound

- Narration: describe the voice ("warm, unhurried female narration of the quoted script"), never "add a voice". New narration means new timings; reveals land on the spoken cues, the narration never waits for visuals.
- Music: mood plus loudness, "subtle electronic BGM, under -18 dB" or "ducked ~12 dB under the voice". Never "add background music".
- SFX: cue them to moments ("a whoosh on each of the three transitions"), do not sprinkle.
- Silence: "no narration" keeps music and SFX; say "no audio at all".
- Mix problems: describe the symptom ("narration sounds muffled, like behind cardboard"), not the filter. Check levels first (the voice may just be quieter than the bed). Fade as envelopes ("fade the music out over the last 3 s"). Finish with an audio-only pass.
- No de-esser, no noise removal (use a better source).

## Captions and on-screen text

| Tone | Caption blocks |
|---|---|
| Hype | `caption-kinetic-slam`, `caption-highlight`, `caption-particle-burst`, `caption-emoji-pop` |
| Clean | `caption-clip-wipe`, `caption-weight-shift` |
| Elegant | `caption-editorial-emphasis`, `caption-gradient-fill` |
| Neon / music | `caption-neon-glow`, `caption-neon-accent` |
| Tech | `caption-glitch-rgb`, `caption-matrix-decode` |
| Karaoke | `caption-pill-karaoke`, `caption-highlight` |

- Captions come from word-level timestamps. Say "vertical" or "9:16" for safe areas.
- One caption style per section. No heavy effect on every word. Do not match hype styles to calm content. Do not put composition captions over a talking-head MP4.
- Overlays and lower thirds: a track above footage, with a timestamp, duration and quoted copy; at least the block's own length (~5 s).
- Code on screen: name the block (`code-typing`, `code-diff`, `code-highlight`, `code-scroll`), paste the code in a fence, name the target line and the theme.

## Brand and determinism

- Brand truth lives in one spec file (palette, fonts, Do/Don't). Colours, fonts and background are strict; sizes, decorative opacity and border weight scale up for video. "Pin the palette and typography, delegate the frame." Provide palette, fonts and logo up front; do not restyle afterwards.
- A series shares one source and changes only the variable parts (headline, stat). Declare variables up front (`string`, `number`, `color`, `boolean`, `enum`, `font`, `image`); duration, size and fps are not variables.
- No live data at render time ("count up to $67,400", not "fetch the current price"). Say "seeded random layout".
- Generated art: solid contrasting background (magenta), key it out with `colorkey`; Lottie files are played, not redrawn. Background removal is person-only.
- Compositions are plain HTML with `data-*` attributes and a GSAP timeline; do not ask for React or Vue components. Do not hard-time a verbatim script ("a ~60-second explainer from this script").

## Storyboard (when the story is not settled)

Four lines first: **Message** (one-sentence thesis), **Arc** (hook, substance, landing), **Audience**, **Mood**. Then per frame: `type` (hook, benefit, proof, cta), `persuasion`, `beat`, `focal`, `roles`. Plant a motif early and return it denser, stating it is the same element. Add one breather frame and a short list of banned clichés.
