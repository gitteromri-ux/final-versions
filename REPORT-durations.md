# REPORT-durations — 45 s and 75 s 9:16 cuts (pipeline copy: /home/user/workspace/ugc-prod-dur, v8 patch applied)

| file | dur (s) | LUFS | dBTP | lang | captions | QC |
|---|---|---|---|---|---|---|
| ad1-man42__9x16__45.mp4 | 45.10 | -14.0 | -1.6 | en | 40/41 | PASS |
| ad2-woman42__9x16__45.mp4 | 45.00 | -13.8 | -1.8 | en | 39/40 | PASS |
| ad3-woman51__9x16__45.mp4 | 44.93 | -14.2 | -1.6 | en | 39/41 | PASS |
| ad1-man42__9x16__75.mp4 | 67.40 | -14.1 | -1.9 | en | 55/56 | PASS, short of 68 (see below) |
| ad2-woman42__9x16__75.mp4 | 67.43 | -13.9 | -1.8 | en | 55/55 | PASS, short of 68 |
| ad3-woman51__9x16__75.mp4 | 71.70 | -14.4 | -1.8 | en | 53/56 | PASS |

All: H.264 High 1080x1920 30 fps yuv420p CRF 17, AAC 192k 48 kHz stereo, +faststart. `.qc.json` sidecar next to each file (ffprobe, ebur128, faster-whisper small.en language+transcript, caption alignment, notes). Frame tiles: `ugc-prod-dur/build/<slug>__<dur>/tile.jpg` (+ `cutA/cutB.jpg` for the 45 s files).

## 45 s (VERIFIED)
- Removed exactly the two sentences ("The youngest … Thirty-three years apart." and "She spends … full-time job."); whisper on the finals confirms they are gone and nothing else is missing.
- Cut points sit inside the silences around the sentences (RMS-verified, `ugc-prod-dur/silences.py`): ad1 [10.75,18.80)+[35.42,42.15), ad2 [11.25,18.68)+[35.92,42.45), ad3 [13.75,24.05)+[41.75,48.12) (orig-take seconds). Each jump hidden with a 1.06 punch-in (cumulative 1.12 after the second cut). 20 ms tri acrossfade at each join; max sample jump at cuts ≤0.08 vs p99.99 of the whole track ≈0.2–0.27 → no click. Cut frames eyeballed (cuts.jpg): read as intentional jump-cuts.
- Speeds: ad1 1.02, ad2 1.045, ad3 1.13. Offer card 4.5 s with build-up 1.25x faster ($49 / SIGN UP NOW / URL hold ≈2 s; visible in tiles). "954 38-YEAR-OLD" caption glue applied (master block).
- Unmatched captions are matcher artefacts ("LONGEVITY MASTERCLASS" heard as "master class"; ad3 "AHEAD OF" heard "the head of"). Caption onsets otherwise within 0.5 s.

## 75 s
- Closer breathes 3.6 s (film 127.8–131.4 at 1.0x: sting + eTeacher), offer card 8.0 s, xfades 0.3/0.4/0.4.
- ad3 at 1.0x → 71.7 s (in range). ad1/ad2 at 0.97x (brief floor) → 67.4 s. The 54.0 s takes cannot reach 68 s without slowing voices below 0.97 or padding the end card beyond 8 s. ASSUMED acceptable as the "75" deliverable; if a hard ≥68 is required, options are speed 0.95 (voice noticeably slow) or a 9 s card — neither applied.
- ad2 sources: master `w42_v2.mp4` was re-encoded at 18:05 (my 17:58 copy decoded only 31 s); re-copied master file + master words.json before rendering both ad2 versions.

## Not done / notes
- 60 s versions and 4x5 / 1x1 / 16x9 formats: not in this task.
- ad2 45 s true peak first measured -1.5 dBTP with the 3.5 s card build; final 4.5 s build measures -1.8. All finals ≤ -1.6 dBTP.
- assemble.py in ugc-prod-dur is resumable (`<out>.ok` markers) and takes `<ugc> <slug> <speed> <45|60|75>`; qc.py `<build-slug> <final-name>` writes the sidecar.
