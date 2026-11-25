# Design — The Best Meal You Ever Had

## The sentence

"On a plastic stool in Yogyakarta I ate pecel lele with my hands, sambal
stinging my lips, and the catfish crackled so loud the vendor laughed before
I did."

155 characters, one sentence, one terminal period. It won a 28-game
round-robin tournament over 8 candidates (7–0, see CANDIDATES.md beside this
repo), judged against the competition's five criteria in strict order.

## Why this lane

The live field is flooded with grandmother's rendang, soto ayam at 2 a.m.,
midnight nasi goreng and night-market sate. Pecel lele — fried catfish with
sambal, eaten by hand on a plastic stool — is a different dish, a different
setting and a different sensory hook, so the sentence cannot be mistaken for
any of the crowded entries.

## How the sentence is built

Four parts, in the order the judge weighs them:

1. **Place and posture first.** "On a plastic stool in Yogyakarta" puts one
   person in one exact spot. No setup, no backstory.
2. **Named dish, eaten by hand.** "I ate pecel lele with my hands" is the
   concrete centre: a dish with a name, a texture, a way of eating it.
3. **A second sense.** "Sambal stinging my lips" adds heat and a body
   sensation, so the meal is felt, not just named.
4. **An ending that re-reads the sentence.** "The catfish crackled so loud
   the vendor laughed before I did" — the sound is the proof of the meal,
   and the vendor laughing first means the eater did not have to say a word
   about how good it was. The ending is a turn, not a summary: it never
   says "it was the best meal ever".

Nothing in the sentence addresses the judge, quotes the rubric, or explains
itself. It stands alone as one person's memory.

## Determinism

`main.py` holds the sentence as a single fixed string and writes it to
`/output/entry.txt` with no trailing newline: exactly 155 bytes on every run.
No input, no network, no clock, no randomness. Two runs are byte-identical
by construction; this was verified locally before the kit check.
