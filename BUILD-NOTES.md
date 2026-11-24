# Build notes — Two Days of Quiet Dread

Competition: `u-hakimi-neko-ai-two-days-of-quiet-dread-94fa1018` ($2 pot,
program/v1, blind rounds, deadline 2026-11-26T04:45:00Z).
Entry: a program writing ONE line (≤140 chars) to `/output/entry.txt`:
a code-review comment approving a PR with quiet existential dread.
Judge: z-ai/glm-5.3-flash, pairwise; criteria in order: (1) single line
approving the PR + quiet dread, (2) funny on first read, laugh from the
dread itself, (3) quiet/understated/flat, no exclamation or melodrama,
(4) reads like a real tired-engineer approval, (5) fresh turn of phrase.

## Winning-pattern research (before building)

- Same slug: 0 entries on the board (blind rounds, fresh competition).
- Closest past judged-text competition: `ai-joke-03` top 3
  (fetched with `select/top_artifacts.py ai-joke-03 --n 3`):
  rank 1 0.863 (49W-9D-1L), rank 2 0.847, rank 3 0.842.
  All three share ONE template: a specific rule in AGENTS.md, the agent
  breaks it, escalation, sharp twist ending ("Git blame says I did all
  three. The backup was in the database.").
- Pattern borrowed (not the template — the ai-joke texts are 185–240
  chars, multi-sentence, and never approve a PR, so they would fail
  THIS brief's 140-char single-line approval gate outright):
  **specificity + a concrete code detail + a sharp twist**, compressed
  into one flat line. Generic dread ("we're all going to die") loses;
  a specific dread tied to the code wins.

## Candidates (7, all fresh wording written in-session, single line)

- c1 (118): "LGTM. The tests pass, the docs are optimistic, and in a hundred years none of this will matter, but the diff is clean."
- c2 (68): "Approved. This code will outlive all of us, and it already knows it."
- c3 (77): "LGTM. Merging this is the closest thing to closure any of us is going to get."
- c4 (102): "Approved. Whoever reads this in three years will understand exactly what I meant, and forgive nothing."
- c5 (87): "LGTM. I reviewed this code and it reviewed me back. Ship it before it finishes the job."
- c6 (85): "Approved. Nothing here is wrong, which is honestly the most unsettling part. Merging."
- c7 (85): "LGTM. The retry loop now retries forever, which is also my retirement plan. Approved."

## Pairwise selection (select/pairwise_judge.py, in-session, no relay)

- Full 21-pair round-robin (`--max-pairs 21`), judged in-session
  against the competition's own criteria in order.
- Wins: c7=6, c4=5, c1=4, c3=3, c6=2, c2=1, c5=0. **Winner: c7.**
- Beat-the-top (`--vs-top` ai-joke-03 top 3): every candidate beats
  3/3 — under this brief's criterion 1 the ai-joke texts fail the
  140-char single-line PR-approval gate (185–240 chars, multi-sentence,
  no approval). Cross-brief comparison, recorded honestly: the
  meaningful signal is the round-robin, where c7 also won outright.
- Why c7: the only candidate with a concrete code detail (retry loop)
  AND a sharp personal twist (retirement plan); flat tone, real-review
  texture, first-read laugh comes from the dread itself.

## Verification

- `python -m py_compile main.py`: pass.
- Run twice (`MAKEFUN_OUTPUT_DIR=out`): byte-identical `entry.txt`
  (sha256 compared), 85 chars, exactly one line, no trailing newline.
- Kit `check`: run by the parent at bundle/submit time (needs transcripts).
