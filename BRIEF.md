# LLA · Julie Masterclass UGC ads — FINAL VERSIONS shared brief (read fully before working)

Owner: Omri (gitter.omri@gmail.com). Rules from his Operator OS apply: never lie, label VERIFIED / ASSUMED,
no purchases, no touching anything Julie-tracking related (GOLDEN CAPI), no progress narration, short reports.
Never buy anything, never use paid APIs. Work only in your own folder. Do not edit `/home/user/workspace/ugc-prod/`
(the master pipeline — copy it: `cp -r /home/user/workspace/ugc-prod /home/user/workspace/<your-folder>`).
The sandbox has 2 CPU cores; other agents render too — run at most ONE ffmpeg/whisper job at a time (use `-threads 1` where sensible), no `-preset veryslow`.

## Product facts (VERIFIED 2026-09-29, use exactly)
The Longevity Masterclass of the Year with Julie Gibson Clark · Longevity Life Academy (by eTeacher Group).
Live on Zoom, 60 min. Tue Oct 27 2026 7 PM ET or Sat Nov 14 2026 1 PM ET. $49. VIP $79 (+30-min private Q&A, $249 credit
toward the Longevity Blueprint course). 14-day refund. URL https://www.longevitylifeacademy.com/julie-masterclass/
Julie: #2 slowest-aging person on Earth 2023 (Rejuvenation Olympics), ahead of Bryan Johnson ($2M/yr); ~$100/month; ages ~6.5 yrs per decade;
single mom, full-time job; founding faculty at LLA.

## Master sources (do not modify)
- `/home/user/workspace/ugc-prod/src/man_v2.mp4`  — Ad 1, 42M, 1080x1920, 53.99 s, one continuous UGC take (seam 23.95 s is seamless)
- `/home/user/workspace/ugc-prod/src/w42_v2.mp4`  — Ad 2, 42F, 1080x1920, 54.02 s (seam at 24.0 s has a 1.06 punch-in baked in)
- `/home/user/workspace/ugc-prod/src/w51_v2.mp4`  — Ad 3, 51F, 1080x1920, 59.92 s
- `/home/user/workspace/ugc-prod/src/julie-film-full.mp4` — Julie film (opener 1.6–2.8 s, PR/press pop-up from 9.0 s, closer 128.6 s+2.0 s, offer audio 131.4 s)
- Pipeline: `assemble.py <ugc.mp4> <slug> [speed]` → `build/<slug>.mp4` (9:16 1080x1920). Steps: whisper word timestamps (cached in build/<slug>/words.json — delete when source changes),
  opener film, UGC main with DOAC-style captions (ASS, Inter Black, yellow keyword highlight, top strap "THE LONGEVITY MASTERCLASS OF THE YEAR"),
  PR press pop-up cut-in over "In 2023 … Earth", Zoom power B-roll (`render_zoom.py`) over "live on Zoom … one hour", closer film, offer card (`render_offer.py`),
  music bed `src/music_lastdawn.mp3` −13 dB, loudnorm −14 LUFS / −1.5 dBTP. `audit.py <slug>` = whisper on the final + caption alignment check.
- Script spoken in every ad (exact): opener "People born the same year can be 33 years apart in biological age. 954 38 year old New Zealanders were tested
  to measure how old their bodies actually were. The youngest in the room was 28. The oldest? 61. Same birth year. Thirty-three years apart. That gap is why I'm going
  to the Longevity Masterclass of the Year on October 27th." then "Everyone is talking about longevity right now, and almost nobody can prove it. Julie Gibson Clark can.
  In 2023 she was the second slowest aging person on Earth, ahead of Bryan Johnson and his two million dollars a year. She spends about a hundred dollars a month.
  Her body ages six and a half years every decade. Single mom with a full-time job. She's one of the founding teachers at Longevity Life Academy, and she's teaching
  her exact protocol live, on Zoom, for one hour. VIP stays for a private Q and A about your own goals. Forty-nine dollars. I'm in."

## Output contract (everyone)
Final files go to `/home/user/workspace/final-versions/videos/` named `<slug>__<fmt>__<dur>.mp4`
slug ∈ ad1-man42 | ad2-woman42 | ad3-woman51; fmt ∈ 9x16 (1080x1920) | 4x5 (1080x1350) | 1x1 (1080x1080) | 16x9 (1920x1080); dur ∈ 45 | 60 | 75 (seconds, target ±1.5 s, NEVER above 75.0).
H.264 High, yuv420p, 30 fps, CRF ≤18, AAC 192k 48 kHz stereo, +faststart, loudness −14 LUFS ±1, true peak ≤ −1.5 dBTP.
Next to each mp4 write `<same-name>.qc.json`: {duration, lufs, true_peak, lang, transcript, captions_matched, notes, verified_by}.
Quality bar (Omri): premium, human, never AI-looking; huge readable captions (Diary-of-a-CEO style: bold, 2–4 words, keyword highlight) that stay inside the safe area of the
format; smooth transitions; any cut from UGC to LLA material must feel motivated by what the person is saying; no blurred-fill letterboxing; no cheap effects.
Everything must be machine-audited (whisper language + transcript, ebur128, caption alignment) AND eyeballed via frame tiles before you say it is done. Label claims VERIFIED / ASSUMED.
When finished: write a short `REPORT-<yourname>.md` in `/home/user/workspace/final-versions/` listing each file with duration/LUFS/QC status, and what is NOT done.
