# Fact-check before building

Run this after the brief and before scaffolding. Output: a rulings table at the top of `beats.md`.

## Steps

1. List every number, rank, date, "first/only/best" and cause-and-effect claim in the VO.
2. Find the primary document first (regulation, filing, official match report), then two independent news sources. Read the article, not the snippet.
3. Recompute every total yourself and write the formula in the sources ("300 + 4 x 50 + 80 = 580"). Say in the copy when a figure is your own calculation, never "official".
4. Check who does the action. "The league pays the club" may really be "paid to the national association".
5. Mark volatile facts (standings, prices, dates) with the check date; re-check on posting day.

## Rulings table

| # | Original line | New line | Why | Source |
|---|---|---|---|---|

Rules for the table:
- The user's original VO file is never edited. Changes live in the script copy.
- Each row has a reason and a source or "unsourced".
- The user approves the table at the script checkpoint. Not-yet-answered rows stay as the original.

## Typical softenings

| Original | Safer line | Reason |
|---|---|---|
| "dominating every match" | "consistent" | scores were 1-0, 1-0, 2-1 |
| "the top spot now officially belongs to them" | "they lead the group table" | games remain |
| "goes into the club's coffers to strengthen the team" | "the total is for the club" | paid via the association; purpose unsourced |
| "a hot topic among local fans" | cut | no source |
| "this season" | "season 2026 to 2027" | year spoken, stays true later |

## Two cases that happen a lot

- **Sources disagree** (for example on a point total): show no number, label the visual as an illustration.
- **A figure matches no combination in the source**: report it, propose the nearest sourced figure, keep the VO unchanged until the user answers.

## Reading a PDF without poppler

On macOS, PDFKit works from a short Swift or Python (PyObjC) script: open the document, loop over pages, print `page.string`. Search the output for the article numbers.
