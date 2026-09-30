# REPORT-formats (4x5 / 1x1 / 16x9, 60 s) — formats agent
Pipeline copy: `/home/user/workspace/ugc-prod-fmt` (assemble.py / render_zoom.py / render_offer.py take `FMT=4x5|1x1|16x9|9x16`; qc.py = whisper+captions+loudnorm+tile; publish.sh copies to final-versions). Master v8 patch applied (hard-cut captions, 54px strap scaled per canvas, offer 5.0 s, xfade joins, TP −2.0). Speeds 1.04 / 1.04 / 1.14.

| file | dur | LUFS | TP | whisper | captions | QC |
|---|---|---|---|---|---|---|
| ad1-man42__4x5__60.mp4 | 59.10 | −14.2 | −2.3 | en 1.00 | 52/56* | PASS (tile eyeballed) |
| ad2-woman42__4x5__60.mp4 | 59.10 | −14.0 | −2.3 | en 1.00 | 53/55* | PASS (tile eyeballed) |
| ad3-woman51__4x5__60.mp4 | 59.80 | −14.4 | −2.0 | en 1.00 | 52/56* | PASS (tile eyeballed) |

*unmatched/“SYNC?” entries are matcher artefacts (repeated phrases, whisper splitting MASTERCLASS / FULL-TIME / 38-YEAR-OLD); no real drift (consistent onset offset ≤0.5 s). Whisper hears the final “I'm in” as “you” on ad1 (also on the master) — VERIFIED artefact, audio is intact.

## Format decisions (VERIFIED on frame tiles)
- 4x5: 1080x1350 band cropped from the 9:16 source at y0 = 190 / 290 / 130 (ad1/ad2/ad3; eyes at ~38% height). Captions Inter Black 88, MarginV 120 (lower third, inside frame); strap 50 px, MarginV 165 (12% from top, same ratio as master 235/1920).
- Opener / closer ring: crop-to-fill (no bars). Closer "by eTeacher Group" text spans 52.7% of the film width → scaled to 1860 px and set on the sting's own flat navy backdrop (blur of the same dark frame — no visible bars). ASSUMED acceptable; it is not a letterbox look.
- PR pop-up: full-height crop with slow pan; Zoom B-roll and offer card recomposed per canvas (8x7 grid, hero Julie; card fully visible, no letterboxing).
- Limiter tightened to 0.75 (−2.5 dB) in my copy: with the master's 0.794 the ad2 4x5 measured −1.48 dBTP (over spec by 0.02 dB).

## Bug found in the MASTER (ugc-prod) — see NOTE-formats-caption-highlight-bug.md
`" ".join(parts).upper()` uppercases `{\c&H…}` to `{\C&H…}`; libass ignores `\C`, so the yellow keyword highlight never rendered in any 9x16 master output (checked frame: "$49." white). Also the "38 YEAR OLD"→"38-YEAR-OLD" replacement can't match with tags between words. Fixed in ugc-prod-fmt only (highlight VERIFIED yellow in the 4x5 files).
Also: my first copy of w42_v2.mp4 was taken while the master was rewriting it (17:58 vs 18:05) → truncated; re-copied (md5 verified) and re-rendered.

## NOT done yet
1x1 (in progress: ad1) and 16x9 for all three ads.
