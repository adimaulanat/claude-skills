# OpenDesign concept board: inputs to confirm

Use only when the person said yes to a board. Every row must be confirmed by the person (or read from a project file they pointed you to) before the run starts. A blank row is a question, not a gap you fill. Ask in rounds of up to 4 questions with the harness's ask tool; if it has none, ask in plain text. Do not start the run while a row is open.

| # | Input | Ask | Confirmed value |
|---|-------|-----|-----------------|
| 1 | Scope | Whole-video look, cover only, or both? | |
| 2 | Concept count | How many concepts? Is the project's current default look one of them, for comparison? | |
| 3 | Direction per concept | For each: dark or light, palette mood, card treatment, one-line name | |
| 4 | Tokens that must stay | Any colours, fonts or layout rules every concept must keep? | |
| 5 | Design-system file | May the chosen look change the project's design-system file? (If not, the pick is used for this video only.) | |
| 6 | Limits | Font, number of colours per frame, forbidden colours, safe areas | |
| 7 | Reference | A description in words of the grammar to borrow. No image upload unless the person explicitly agrees to it | |
| 8 | Script and beats | The approved or draft script and the beat list every concept shows (same for all concepts) | |
| 9 | Frames per concept | Which beats to draw, plus the end card | |
| 10 | Target | Which OpenDesign agent runs it (list what is available; for the cloud agent check sign-in first), the project name, design system on or off | |

## Prompt outline (fill from the confirmed values, nothing else)

```text
Make a concept board (HTML: index.html + one page per concept) for a <format, size, fps, length>
video for <account or brand, language, audience>.
Board only: static mockups plus written motion notes.

REFERENCE (grammar only, described in words): <row 7>
Borrow structure and visual grammar only. Do not copy any text, logo, handle, product or footage.

TOPIC: <topic>. SCRIPT AND BEATS (same for every concept): <row 8>

FIXED (every concept): <row 6, row 4>

CONCEPTS: <row 2 and row 3, one paragraph each>

FOR EACH CONCEPT PAGE: frames for <row 9>, the end card, the token list (hex values with role names),
the motion vocabulary (timings in frames), one sentence on sound-off readability.

INDEX PAGE: the hook frames side by side, a comparison table (closeness to the reference, fit with the
brand, hook strength in the first 2 seconds, readability sound-off, effort to build, main risk),
one recommendation with three reasons, and the beat map.
```

## After the run

1. Check the files with the file listing, not with the run status.
2. Show the person the index page and ask which concept to use.
3. Record the pick in the project's script file as `Design: <concept name> (chosen <date>)`.
4. If the pick is not the project's default look and row 5 allows it, ask once more before writing its tokens into the design-system file.
