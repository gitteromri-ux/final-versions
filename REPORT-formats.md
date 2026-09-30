# REPORT-formats (4x5 / 1x1 / 16x9, 60 s) — formats agent

Pipeline copy: `/home/user/workspace/ugc-prod-fmt` — `assemble.py`, `render_zoom.py`, `render_offer.py` take `FMT=4x5|1x1|16x9|9x16` (env var); `qc.py` = whisper small.en + caption alignment + loudnorm/ebur128 + fps=1/2.5 frame tile; `publish.sh` copies to final-versions with the .qc.json. Master v8 patch applied (hard-cut captions, 54-px strap scaled per canvas, offer card 5.0 s, xfade 0.30/0.40/0.40 + acrossfade, PR/Zoom alpha fades, loudnorm TP −2.0). Speeds 1.04 / 1.04 / 1.14. Tiles eyeballed for every file: `ugc-prod-fmt/build/insp/<ad>_<fmt>_tile.png`.

| file | dur | LUFS | dBTP | whisper | captions* | QC |
|---|---|---|---|---|---|---|
| ad1-man42__4x5__60.mp4 | 59.10 | −14.2 | −2.25 | en 1.00 | 52/56 | PASS |
| ad2-woman42__4x5__60.mp4 | 59.10 | −14.0 | −2.31 | en 1.00 | 53/55 | PASS |
| ad3-woman51__4x5__60.mp4 | 59.80 | −14.4 | −2.03 | en 1.00 | 52/56 | PASS |
| ad1-man42__1x1__60.mp4 | 59.10 | −14.2 | −2.25 | en 1.00 | 52/56 | PASS |
| ad2-woman42__1x1__60.mp4 | 59.10 | −14.0 | −2.31 | en 1.00 | 53/55 | PASS |
| ad3-woman51__1x1__60.mp4 | 59.80 | −14.4 | −2.03 | en 1.00 | 52/56 | PASS |
| ad1-man42__16x9__60.mp4 | 59.10 | −14.2 | −2.25 | en 1.00 | 52/56 | PASS, caveat below |
| ad2-woman42__16x9__60.mp4 | 59.10 | −14.0 | −2.31 | en 1.00 | 53/55 | PASS |
| ad3-woman51__16x9__60.mp4 | 59.80 | −14.4 | −2.03 | en 1.00 | 52/56 | PASS |

All: H.264 High, yuv420p, 30 fps, CRF 17, AAC 192k 48 kHz stereo, +faststart (VERIFIED via ffprobe in each .qc.json).
*Unmatched / "SYNC?" entries are matcher artefacts (repeated phrases match the first occurrence; whisper splits MASTERCLASS / FULL-TIME / 38-YEAR-OLD); onset offset otherwise ≤0.5 s. Whisper hears ad1's final "I'm in" as "you" and adds a phantom "Thank you" on ad2 (same as on the 9x16 masters) — audio is intact (VERIFIED by word timings of the source).

## Format decisions (VERIFIED on frame tiles)
- UGC crop bands from the 1080x1920 source, y0 per ad (ad1/ad2/ad3, eyes at y≈700/800/640): 4x5 190/290/130 · 1x1 300/400/240 · 16x9 540/600/450 (1080x608 band → 1920x1080 lanczos + unsharp 0.45).
- Captions Inter Black: 4x5 88 px MarginV 120 · 1x1 80 px MarginV 90 · 16x9 84 px MarginV 70 (lower third, fully inside frame). Top strap 50/46/50 px at MarginV 165/130/110 (4x5 keeps the master's 12 %-from-top ratio).
- Opener + closer ring: crop-to-fill, no bars. Closer "by eTeacher Group" text spans 52.7 % of the film width, so on 4x5/1x1 it is scaled to 1860 px and set on the sting's own flat navy backdrop (blur of the same dark frame; no visible bars — ASSUMED acceptable, not a letterbox look). 16x9 uses the film natively.
- PR pop-up: full-height crop + slow pan (4x5/1x1), native frame + 7 % push-in (16x9). Zoom B-roll re-gridded per canvas (8x7 / 8x7 / 14x4 tiles, hero Julie re-positioned). Offer card recomposed per canvas (16x9 = two-column); all text visible, no letterboxing.
- Limiter tightened to 0.75 (−2.5 dB) in my copy: with the master's 0.794 the ad2 4x5 measured −1.48 dBTP (0.02 dB over spec). All files now ≤ −2.0 dBTP.

## Caveats
- 16x9 from a 9:16 selfie source is inherently an extreme close-up; ad1 (largest face in frame) shows eyebrows-to-chin and the strap sits on his forehead. ad2/ad3 are tighter than ideal but readable. Recommend 16x9 only where placement requires it; ad1 16x9 is the weakest asset (ASSUMED — judgement call).
- Bug found in the MASTER (ugc-prod/assemble.py), see `NOTE-formats-caption-highlight-bug.md`: `.upper()` turns `{\c&H…}` into `{\C&H…}`, which libass ignores, so the yellow keyword highlight never rendered in the 9x16 masters (VERIFIED on a frame: "$49." white), and the "38 YEAR OLD"→"38-YEAR-OLD" replacement cannot match. Fixed in ugc-prod-fmt only (highlight VERIFIED yellow in all 9 files here). The 9x16 files should be re-rendered with the same fix.
- My first copy of w42_v2.mp4 was taken while the master rewrote it (truncated at ~29 s); re-copied (md5 verified) and ad2 re-rendered.

## NOT done
Nothing outstanding for this task (9 files delivered). 9x16 highlight fix in the master pipeline is out of my scope (do-not-touch).
