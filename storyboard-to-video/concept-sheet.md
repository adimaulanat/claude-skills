# Concept sheet

Fill this in once, before scaffolding. Every later choice (build, captions, thumbnail, carousel) reads from it.

| Slot | What to write |
|---|---|
| Name + style | One line, e.g. "Tactics Board: flat, block colour, thick outlines" |
| Palette tokens | `--ink`, `--bg`, `--accent`, `--surface`, plus one per prop colour the prompts ask for. Source + check date. Contrast of text on its background (aim ≥ 4.5:1). |
| Type | One family, weights per job (display 800/900 on objects, 700 captions). Tabular numerals for scoreboards and money. |
| Characters | One SVG function per character (`coach()`, `player()`): head, torso, limbs as separate joined parts. Head outline = ink, dot eyes. Idle: breathing sine + blink. No lip-sync when the narrator is off-screen. |
| Props per scene | One row per prompt scene: prop, what it does, the VO cue word that triggers it. |
| Layout zones | Characters and props in the middle band; captions inside the platform safe zone (about y 1250 to 1650 of 1920). |
| Motion tokens | Pop `back.out(1.4)`, enter `power3.out`, stagger 0.06 s, exit 60 to 70 % of enter. 3 to 5 seam types for the whole film. |
| Bans | Official logos and crests, real player photos, emoji, text overshoot, any number without a source. |

## Worked example (a football explainer, abridged)

- Palette from the team's public brand data: ink `#171B87`, accent `#FFF200`, pitch `#179E3C`, background a 5 % tint of the ink. The yellow is a highlight block behind dark text, never yellow text on a light background.
- Characters: coach (vest with white stripes) and player (jersey, yellow boots), both round white heads.
- Scene 3 prop: a brown safe (the prompt asked for brown), "$580.000" printed on it, green coins falling in on the cue "uang".
- Scene 4 prop: a rising line chart labelled "Illustration of the trend, not to scale", no numbers, because the sources disagreed on the totals.
- Ban: the real crest was available but the channel is not the club, so shirts are plain ink and the name appears as text.
