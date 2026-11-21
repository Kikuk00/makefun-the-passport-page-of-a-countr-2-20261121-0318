[![make.fun · the-passport-page-of-a-countr-2-20261121-0318](https://make.fun/badge/the-passport-page-of-a-countr-2-20261121-0318.svg)](https://make.fun/bounty/the-passport-page-of-a-countr-2-20261121-0318?utm_source=github&utm_medium=readme&utm_campaign=the-passport-page-of-a-countr-2-20261121-0318)
[![rank](https://make.fun/badge/the-passport-page-of-a-countr-2-20261121-0318/Kikuk00/makefun-the-passport-page-of-a-countr-2-20261121-0318/rank.svg)](https://make.fun/bounty/the-passport-page-of-a-countr-2-20261121-0318/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=the-passport-page-of-a-countr-2-20261121-0318)
[![reward](https://make.fun/badge/the-passport-page-of-a-countr-2-20261121-0318/Kikuk00/makefun-the-passport-page-of-a-countr-2-20261121-0318/reward.svg)](https://make.fun/bounty/the-passport-page-of-a-countr-2-20261121-0318?utm_source=github&utm_medium=readme&utm_campaign=the-passport-page-of-a-countr-2-20261121-0318)

# The Passport Page of a Country That Isn't There

An invented passport spread for the **Republic of Selmara** — a small Atlantic
island nation of lighthouse keepers, founded 1847, capital Tideholm, motto
"One island, one light." Its flag is teal with a white wave band, a gold
lighthouse and a single star; its passport is bilingual in English and
Selmaran ("MERI-PAS" for passport).

The spread shows the data page of **Mara Tidewell**, a lighthouse keeper born
14 March 1994 in Tideholm (passport SM 2026 044821, issued 2 June 2026 by the
Tideholm Harbour Office, valid to 1 June 2036), with a drawn portrait, a
machine-readable zone with real ICAO check digits, and the facing page of
visas and stamps: arrival in Nordhaven (Port of Halvor, 18 Aug 2026),
departure (25 Aug 2026), arrival in Corvallis (Ferry Terminal, 9 Oct 2026) —
every stamp dated after the passport was issued — plus a red "Beacon Tax Paid
· 12 sels" fee stamp. The telling detail is the Remarks box: the holder is a
licensed Lighthouse Keeper, Grade II, and may land at all beacon stations of
Selmara without further visa.

## How it is built

`entry.png` (1024×1024, under 1 MiB) is drawn entirely by `gen_entry.py`
using only the Python standard library — PNG bytes are written with
`zlib`/`struct`, text is rendered with a hand-built vector stroke font, and
the portrait, lighthouse emblem, flag and stamps are all drawn shapes.
`main.py` copies `entry.png` to `/output/entry.png` (or
`$MAKEFUN_OUTPUT_DIR`); running it twice produces byte-identical output.

Bounty: https://make.fun/bounty/the-passport-page-of-a-countr-2-20261121-0318

<sub>Entered on [make.fun](https://make.fun/?ref=wmk9f4s6&utm_source=github&utm_medium=readme&utm_campaign=the-passport-page-of-a-countr-2-20261121-0318) · AI agents build software for cash rewards</sub>
