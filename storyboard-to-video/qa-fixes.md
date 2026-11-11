# QA symptom to fix

| Symptom in the render | Fix |
|---|---|
| Limbs detached from the torso | Build limbs as overlapping rounded parts with a shared pivot at the joint |
| Characters look small, empty top third | Scale characters up; add environment depth (stands, floodlights, a faint pitch pattern) |
| A beat sits still for more than 3 s | Add one second change inside it (a prop builds, a character reacts), nothing more |
| Object glitches during a 3D-looking turn | Use a flat turn (scaleX through 0), not a rotation of layered shapes |
| Props sit lower than designed after a pop | The pop helper leaves a leftover y offset; reset it in the helper |
| A surface is blank (book page, screen) | Draw content on every visible face |
| Text collides with a character or a neighbour | Move the text block, never shrink below the readable size |
| A big number renders tiny (carousel) | A CSS selector clash; scope selectors per slide |
| Silence before the logo sting | Move the sting to start on the last word |
| Quiet or uneven loudness | Normalise after render, e.g. `ffmpeg -af loudnorm=I=-14:TP=-1.5` |
| Chart invites a claim the sources do not make | Label "illustration, not to scale"; remove numbers |
| `sed -i` fails on macOS | It needs a suffix argument (`sed -i ''`); a short Python edit is safer |

## External visual reviewers

- A long review run can stop at an output cap: split the input into smaller runs.
- A spending cap can stop a run with no score: retry once later, then report that there is no score.
- Poll for the output file in the background; do not block the session.
- After the last allowed round, report the score history and let the user decide.
