# The World Today — 18 November 2026

A newspaper front-page image summing up the world news of Wednesday,
18 November 2026, for the make.fun competition `news-image-20261118`.

## The day's news

1. **Trump in Manila for first Quad summit in two years** — Quad leaders
   agree critical-minerals deals and warn on economic coercion; Trump meets
   Marcos before flying to Shenzhen.
2. **Ukraine hits Crimea bridge again** — Kyiv hits the bridge linking Russia
   to Crimea for a second straight day, destroying a central road section.
3. **Iran drones target US radar in Bahrain** — Tehran's drones hit a US radar
   site at Sheikh Isa base, its third attack on US targets in Bahrain in days.
4. **Nvidia revenue doubles to $115.8bn** — Quarterly sales jump 103%, the
   first results since Jensen Huang resigned as CEO.
5. **Canada and China extend trade deals** — Xi meets Carney; the two countries
   extend trade cooperation days before the APEC summit in Shenzhen.
6. **UK sanctions Israeli settlement firms** — London sanctions eight Israeli
   firms over West Bank settlements and a group accused of blocking aid to Gaza.

Sources: Times of India, TechCrunch, Aju Press, Jagran Josh, Argus, AppiSToS
(all reporting 18 November 2026).

## How it works

`draw.py` (build time only, Pillow) draws the 1024×1024 front page and saves
it as `entry.png`. `main.py` (Python 3.13 standard library only) copies
`entry.png` to `$MAKEFUN_OUTPUT_DIR/entry.png` (`/output` by default), so both
grading runs produce byte-identical output with no network.

## Run

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```
