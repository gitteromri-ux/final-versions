# AUDIT — Julie Masterclass UGC ads · full-history instruction audit
Auditor: independent subagent · 2026-09-30 18:10 UTC · read-only (no video/pipeline touched)

Evidence audited: `ugc-prod/build/ad1-man42.mp4` (v5, 60.22 s), `ad2-woman42.mp4` (v7, 60.23 s), `ad3-woman51.mp4` (v6, 60.80 s), their `captions.ass`, `transcript.txt`, `build/audit_ad1_v5.log`, `build/audit_ad3_v6.log`, ebur128 run by me, frame tiles in `final-versions/audit_frames/` (1.5 s tiles + 3–4 fps close-ups of 0–3 s, PR pop-up, Zoom shot, end card).
**Ad 2 (ad2-woman42)**: v6 (`ad2_v6.log`) was a broken 36.82 s master; the source was rebuilt and **v7 finished 18:10 UTC: FINAL 60.23 s** (`ad2_v7.log`, `audit_ad2_v7.log`). All Ad 2 findings below are on v7 (tiles `ad2_tile_1p5.png`, `ad2_seam_22-27s.png`).

Legend: PASS / FAIL / PARTIAL / NOT YET. Timestamps are ad time (opener included). Claims are VERIFIED unless marked ASSUMED.

## A. Omri's instructions (chronological, quoted)

| # | Instruction (turn) | Status | Evidence | Fix needed |
|---|---|---|---|---|
| 1 | T1 "mind-blowing stat about the ability to slow down aging … simple and bold and clear" opens the ad | PASS | Ad1 1.25–20.2 s / Ad3 1.25–23.3 s: Dunedin 954 / 28 vs 61 / 33 years apart, captioned in 2–4-word chunks | — |
| 2 | T16/T17 "This is approved as one script opener worded EXACTLY IN THESE WORDS … 954 38 year old **Americans** … " + "YOU FORGOT … sentence one main claim" | PARTIAL | Spoken/captioned: "954 38 year old **New Zealanders**" (assistant's own factual fix proposed in T16 reply; never explicitly approved by Omri, never objected to in T17–T22). Sentence-one claim present at 1.25 s in both ads. Whisper hears Ad2/Ad3 voice as "New Zealand**ans**" (audit_ad3_v6.log, ad2_v6.log) while Ad1 = "New Zealanders" → possible mispronunciation in the female voices (ASSUMED; needs ear check). Captions are spelled correctly (pipeline maps ZEALANDANS→ZEALANDERS). | Tell Omri the one-word change explicitly; listen to Ad2/Ad3 at ~7.5 s; re-voice if "Zealandans". |
| 3 | T3 "you must position this as the masterclass of the year on longevity" + T22 "PPL ARE GONNA SKIP. YOU NEED LONGEVITY MASTERCLASS OF THE YEAR TO APPEAR BEFORE" | PARTIAL | Spoken "Longevity Masterclass of the Year" first at **21.2 s** (Ad1) / **24.3 s** (Ad3) — after the whole 19–22 s hook. Only earlier appearance = top strap "THE LONGEVITY MASTERCLASS OF THE YEAR" from 1.4 s, Inter ExtraBold **42 px** on a 1920 px frame (2.2 % height), sits in the Reels top-UI zone (MarginV 120). Claude P2-13 unchanged. | Enlarge/lower the strap (≥ 64 px, y ≈ 300–400) or add a 1-s title card/lower-third at the first "33 years apart" (≈3.2 s). |
| 4 | T18 "CLARIFY WHO THE FUCK JULIE IS" + T3 must-haves: 2023 #2 slowest ager, almost no money, 6.5 yrs/decade, founding faculty LLA, Q&A | PASS | Transcript (audit logs): "In 2023 she was the second slowest aging person on Earth, ahead of Bryan Johnson and his $2 million a year. She spends about $100 a month. Her body ages six and a half years every decade. Single mom with a full-time job. She's one of the founding teachers at Longevity Life Academy … VIP stays for a private Q&A about your own goals." Ad1 29.3–46 s, Ad3 32–47 s. | — (Claude P2-11/12 qualifiers still absent, see C-11/12) |
| 5 | T20 "EVERYONE IS TALKING ABOUT LONGEVITY, ITS EVERYWHERE. VERY HARD TO KNOW WHO HAS IT RIGHT … AND THEN JULIE" | PASS | "Everyone is talking about longevity right now, and almost nobody can prove it. Julie Gibson Clark can." Ad1 23.7–28.4 s | — |
| 6 | T3 "no radio-commercial talk … nobody speaks this way in a UGC", T15 "why do u always name drop words" | PASS (subjective) | Script is first-person, short sentences, no jargon ("clock", "speed", "clinical" absent). Only name drop = Bryan Johnson, which Omri asked for in T3. | — |
| 7 | T3 "scarce opportunity … used to be accessible only to the well-connected … we make longevity accessible" ; "refund / cash back card at the end" | PARTIAL | Scarcity/accessibility angle is NOT in the spoken script (dropped during T18–T22 rewrites for length). Refund: offer card line "14-day full refund on both seats" at 34 px, visible last ~1.3 s only. | Accept as a length trade-off, or add refund/scarcity to the end card in ≥ 48 px. |
| 8 | T3 "Metalegion … huge captions and bold, one-line bold graphics … throughout the video" + T45 "DIARY OF CEO TYPE OF CAPTIONS FOR MAIN MESSAGING ESPECIALLY ON THE POWER HOOK" | PARTIAL | Cap style: Inter Black 94 px (4.9 % of height), 2–4 words, yellow keyword highlight, 7 px outline, safe zone (MarginV 470) → good, but not DOAC-size (DOAC ≈ 7–8 % height). Defects: (a) chunks overlap 0.05 s + 40 ms fades → **two lines stacked** — Ad1 7.5 s "NEW ZEALANDERS" over "954 38 YEAR OLD", 25.5 s "CAN PROVE IT." over "ALMOST NOBODY" (tile ad1_tile_1p5.png); (b) **no captions for ~5 s during the Zoom shot** except the static "LIVE ON ZOOM" — "for one hour. VIP stays for a private Q&A about your own goals" is uncaptioned (assemble.py skips chunks inside zoom window); (c) "954 38 YEAR OLD" still unreadable as a number pair (Claude P1-7); (d) Ad1 47.3 s caption "HER EXACT PROTOCOL" hangs over an empty dark frame at the start of the Zoom shot. | Hard cuts between chunks (end = next start − 1 frame, drop \fad); caption the VIP/Q&A line inside the Zoom shot; bump Cap to ≥ 110 px; "954 PEOPLE · ALL 38". |
| 9 | T22 "ADD JULIE'S VIDEO OPENER AND CLOSER FOUND ON PAGES.DEV" | PARTIAL | Opener = film 1.6–2.8 s = **LLA logo on black, 1.23 s, audio silent (ebur128 −∞ until 1.2 s)**; no Julie in it. Closer = film 128.6 s: eTeacher swirl ~1 s + black "by eTeacher Group" card ~1 s, 16:9 inside 9:16 with **gaussian-blur fill** (BRIEF: "no blurred-fill letterboxing"). Ad1 54.2–56.2 s, Ad3 54.8–56.8 s. | Either use a Julie shot from the film as opener, or drop the logo opener (Claude P0-2) and start on face at 0.0 s; replace blur-fill closer with the 9:16 offer card directly (logo can live on the card). |
| 10 | T22 "ADD THAT PR THING OF HER IN THE VIDEO WHERE ALL ARTICLES POP UP" | PARTIAL | Present: Ad1 30.3–32.9 s, Ad3 33.0–35.8 s, native-vertical crop of film 9.0 s+, motivated by "In 2023 she was the second slowest…". BUT it is the same **fake press-card collage** Claude flagged P0-1: at Ad1 31.5 s the card "A 56-year-old recruiter sets aside $12 a day for her longevity routine" is legible, contradicting "$100 a month" spoken 4 s later; outlet-styled mock-ups. Hard cut in/out, no transition. | Replace with real article screenshots (Fortune/BI/AP/Yahoo) before launch; soft 6-frame dissolve. |
| 11 | T22 "ADD THE SIGN UP NOW AND MASTERCLASS REAL INFO, DATES AND PRODUCT … VERY LARGE FONTS … CAN'T LOOK LIKE THE BANNERS" | PARTIAL | Offer card (render_offer.py; Ad1 56.2–60.2 s, Ad3 56.8–60.8 s): "THE LONGEVITY MASTERCLASS OF THE YEAR / with Julie Gibson Clark / #2 slowest aging person on Earth, 2023 / LIVE ON ZOOM · 60 MIN / TUE OCT 27 · 7 PM ET / SAT NOV 14 · 1 PM ET / $49 / VIP $79 private Q&A + $249 Blueprint credit / SIGN UP NOW / URL / 14-day refund" — all facts match BRIEF (VERIFIED). Headline large; but button + URL + refund only appear at ~58.9 s → **on screen ≈ 1.3 s**; URL 42 px, refund 34 px (small). Full card total 4.0 s. | Hold complete card ≥ 3 s (start build-in earlier or extend card to 5–6 s and trim swirl/eTeacher 2 s). |
| 12 | T22 "JULIE ON ZOOM WITH 50 PPL MOCKUP ANIMATED WITH POWER BEFORE ENDING FRAME WITH THE CTA" | PASS | Ad1 46.9–51.8 s, Ad3 47.9–52.4 s: ~60 participant tiles fly in, Julie host tile scales up, "LIVE ON ZOOM" headline + "OCT 27 · 7 PM ET / or NOV 14 · 1 PM ET", music swell timed to it (t_music = zoom − 12 s). Placed before "$49. I'm in" → closer → CTA card. | Minor: first 0.5 s is an almost-empty dark frame under a leftover caption (see 8d). |
| 13 | T22 "MUST FEEL LARGER THAN LIFE WITHOUT FEELING LIKE AN AD AND NOT A UGC" | PARTIAL (subjective) | UGC body is a single close-up take, natural kitchen/bookshelf light; music bed −13 dB from ~35 s; Zoom power shot and offer card add scale. Working against it: 1.12× speed-up on Ad1/Ad3 speech (atempo, pitch kept — ASSUMED audible as slightly rushed), logo-on-black open, blur-fill swirl. | Consider 1.06–1.08× and fixing rows 9/10. |
| 14 | T22 "EACH UGC HAS ONE PERSON SPEAKING LIKE A UGC SO CLOSE UP … 42 white male in good shape, healthy, relatable / woman same age / 51-year-old woman, white American" | PASS | Tiles: Ad1 one male, close-up, grey tee, kitchen; Ad2 one female ~40, green sweater, living room; Ad3 one female ~50, white blouse, bookshelf; one speaker each, no second person. Ages are ASSUMED from appearance. | — |
| 15 | T22 "SCENES CONSISTENCY" · T42 "MAINTAIN PERFECT SCENE CONSISTENCY" | PASS (Ad1, Ad3) · PARTIAL (Ad2) | Ad1: continuous take, seam at 23.95 s invisible in 1.5 s tiles and 3 fps PR tile. Ad3: no visible framing/skin change across 0–54 s. **Ad2: visible jump at 24.5 s** (ad2_seam_22-27s.png, 4 fps): framing tightens (baked 1.06 punch-in), head position and hands change, background/skin tone shift slightly, caption "ON OCTOBER 27TH." straddles the seam then a 0.5 s caption gap. Sharpness/skin now consistent (Claude P1-8 largely fixed) but it still reads as a cut, not one take. | Cover the seam with B-roll (e.g., a 1-s title/strap card on "Masterclass of the Year") or a 0.3 s whip/zoom transition. |
| 16 | T22 "FINAL FILES DELIVERED ON A GITHUB OPEN LINK, VIDEOS EMBEDDED, DOWNLOAD BUTTONS, AUTOPLAY WITH SOUND, PAGE PER VIDEO" | PARTIAL | REPORT-site.md: live at https://gitteromri-ux.github.io/final-versions/ (HEAD baa0424, VERIFIED 200 by site agent, not re-checked by me). Per-video page has `<video autoplay controls>`, unmute-tap overlay, Download MP4. Only **2/36** videos in `final-versions/videos/` (ad1 & ad3, 9x16, 60 s); index shows 34 "rendering…" cells. | Re-run deploy.sh after each master lands. |
| 17 | T22 "DO NOT MISS … CONSISTENCY, CAPTIONS, OUTROS, INTROS, CTA'S" | PARTIAL | See rows 8, 9, 11. Intros/outros identical across ads (good consistency), but intro is a silent logo and outro carries blur-fill. | — |
| 18 | T31 "you used other fonts, other cards, wrong syncs, bad timing, music doesn't work, clunky, jumps" (things not to repeat) | PARTIAL | Fonts consistent (Inter). Sync: audit logs show constant +1.24 s caption-vs-whisper offset = opener length (expected); no drift (max deviation ≈ 0.02 s over 53 s). Music: enters at ~35 s (Ad1 34.9 s, Ad3 35.9 s), swells on Zoom, fades before closer — fine. "Jumps": hard cuts at PR in/out, Zoom in/out, UGC→swirl, swirl→black card→offer card = 6 hard cuts in the last 30 s. | Add 4–8-frame dissolves at overlay boundaries. |
| 19 | T32 "rule that you have to audit everything … what if it's in Chinese, no sound, wrong words, music doesn't match" | PASS (Ad1, Ad3) | audit_ad1_v5.log / audit_ad3_v6.log: LANG en p=1.0, transcript = script word-for-word, 57/59 and 54/58 captions matched; ebur128 by me; frame tiles by me. Caveat 1: whisper also hears "**Thank you.**" (Ad1) / "**Thank you for watching.**" (Ad3) after "I'm in" — on the closer/offer film audio (131.4 s). Either a real film VO tail or a whisper hallucination on music — nobody has confirmed by ear. Caveat 2: ad1 qc.json says "2 unmatched = top strap" — wrong: the unmatched lines are "LONGEVITY MASTERCLASS" (20.2 s) and "A FULL-TIME" (40.2 s); the strap lines matched. | Listen to 54–60 s once; correct the qc.json note. |
| 20 | T36 "NOTHING CAN BE OPEN THIS IS GOING LIVE IN PERFECT FORMAT" · BRIEF output contract | PARTIAL | 9x16 masters: H.264 High, yuv420p, 30 fps, AAC 192 k 48 kHz stereo, faststart, CRF 17, duration 60.22 / 60.23 / 60.80 (target 60 ± 1.5 ✔). Loudness −14.0 / −13.8 / −14.3 LUFS ✔. **True peak −1.2 / −1.4 / −1.4 dBTP → all three exceed the −1.5 dBTP limit** (alimiter set to 0.891 = −1.0 dBFS sample peak, no oversampling). | Set `alimiter=limit=0.76` (≈ −2.4 dB) or `loudnorm` two-pass with TP −2.0; re-mux audio only (no video re-encode needed). |
| 21 | T45 "vertical, horizontal, square, landscape … 60 sec, 45 sec cuts as well as 75 seconds. no longer" | NOT YET | Delivered: 9x16 × 60 s for Ad1, Ad3 (2 of 36). No 45 s or 75 s cut, no 4x5/1x1/16x9 exists yet in final-versions/videos. | In progress by other agents. |
| 22 | T45 "SMOOTH TRANSITIONS" | FAIL | Every section boundary is a hard cut (opener fade-to-black → hard cut to face at 1.23 s; PR overlay in/out; Zoom in/out; UGC→swirl; swirl→card). Only the opener has fades. | Dissolves (0.2 s) on overlay enable windows via `xfade`/alpha ramp; fade swirl→card. |
| 23 | T45 "IF U CUT FROM A UGC TO OUR MATERIALS, IT MUST MAKE SENSE AS A UGC" (motivated cuts) | PASS | PR pop-up lands exactly on "In 2023 she was the second slowest aging person on Earth"; Zoom shot on "live on Zoom for one hour … Q&A"; card after "I'm in". No "watch this" gesture. | — |
| 24 | T45 "LARGE GRAPHICS FONTS … UTMOST CLARITY OF MESSAGE AND OFFERING. THE CLOSERS" | PARTIAL | Offer clear and correct; Zoom shot dates 60 px+; but strap 42 px, URL 42 px, refund 34 px, button visible 1.3 s. | See rows 3, 11. |
| 25 | T45 "SOUND, LIGHTING, CAPTIONS, MUSIC, NARRATORS SUPER PREMIUM, SUPER HUMAN NOT AI" | PARTIAL (subjective, ASSUMED) | Lighting/talent read natural in tiles; no lip/hand artefacts seen at 1.5 s sampling (not frame-exact). Speech at 1.12× (Ad1/Ad3) is the main "not human" risk; silent first 1.2 s. | Ear check by a human; consider lower speed. |
| 26 | T45 "I WANT CLAUDE TO AUDIT … AFTER FULL AUDIT OF YOUR OWN … AGAINST MY INSTRUCTIONS FROM WHEN WE BEGAN" | PARTIAL | This document. Claude's P0/P1/P2 re-check below: of 16 UGC items, **2 fixed, 3 partial, 10 unchanged, 1 N/A**. | — |
| 27 | BRIEF "no test data" | PASS | No lorem/placeholder in videos; site "rendering…" cells are honest status, manifest lists only real files. | — |
| 28 | BRIEF "captions stay inside the safe area of the format" | PASS (9x16) | Cap MarginV 470 px from bottom (bottom 24 % clear of Reels UI), L/R margins 40 px; Zoom-shot headline at y≈60–110 px sits in the top-UI zone (risk on Reels), strap at 120 px likewise. | Move strap/Zoom headline below ~250 px. |

## B. Ad-by-ad measurements

| Item | Ad1 man42 (v5) | Ad2 woman42 | Ad3 woman51 (v6) |
|---|---|---|---|
| Duration | 60.22 s | 60.23 s (v7) | 60.80 s |
| Segments | opener 1.23 / main 52.90 / closer 2.02 / offer 4.00 | 1.23 / 52.93 / 2.02 / 4.00 | 1.23 / 53.48 / 2.02 / 4.00 |
| LUFS / true peak | −14.0 / **−1.2** | −13.8 / **−1.4** | −14.3 / **−1.4** |
| Whisper lang / transcript | en 1.0 / = script (+"Thank you." tail) | en 1.0 / = script ("New Zealandans" heard) | en 1.0 / = script (+"Thank you for watching." tail) |
| Captions matched | 57/59 (unmatched: "LONGEVITY MASTERCLASS", "A FULL-TIME") | 56/57 v7 (unmatched: "NEW ZEALANDERS" — voice says "Zealandans") | 54/58 (unmatched: "954 38-YEAR-OLD", "NEW ZEALANDERS", "LONGEVITY MASTERCLASS", "A FULL-TIME JOB.") |
| Speed | 1.12× | 1.02× | 1.12× |
| Face first visible | 1.25 s | 1.25 s | 1.25 s |
| "Masterclass of the Year" spoken | 21.2 s | 22.5 s | 24.3 s |
| PR pop-up | 30.3–32.9 s | 30.2–33.8 s | 33.0–35.8 s |
| Zoom shot | 46.9–51.8 s | 47.1–52.1 s | 47.9–52.4 s |
| Swirl + eTeacher card | 54.2–56.2 s | 54.2–56.2 s | 54.8–56.8 s |
| Offer card / button visible | 56.2–60.2 s / ≈1.3 s | 56.2–60.2 s / ≈1.3 s | 56.8–60.8 s / ≈1.3 s |
| Stacked-caption frames seen | 7.5 s, 25.5 s | 10.5 s, 25.5 s | (chunks overlap identically; same engine) |

## C. Claude audit (docx, v2 scored 5/10) — item-by-item on current masters

| Claude # | Item | Now | Evidence |
|---|---|---|---|
| P0-1 | Fake press cards (BI/Daily Mail/NOVOS look-alikes, "$12 a day") | **NOT FIXED** | Same collage, Ad1 31.5 s card "56-year-old recruiter sets aside $12 a day" legible (audit_frames/ad1_pr_29-33s.png). Still P0. |
| P0-2 | First second is a logo on black | **NOT FIXED** | 0–1.23 s LLA logo, black, silent (ad1_open_0-3s.png). (Conflicts with Omri's T22 "Julie's video opener" — but the current opener isn't Julie either.) |
| P0-3 | Confirm end-card URL loads | N/A here | BRIEF lists URL as VERIFIED 2026-09-29; not re-checked by me. |
| P0-4 | "$49. I'm in." right after VIP line → sounds like VIP is $49 | **NOT FIXED** in audio; mitigated on card | Script unchanged ("VIP stays … goals. $49. I'm in."). Offer card shows $49 and VIP $79 separately. |
| P0-5 | Synthetic endorser / AI disclosure | **NOT FIXED** | No disclosure in video or on the delivery page. Decision needed by Omri (Meta AI-label at upload is the minimum). |
| P1-6 | CTA on screen ~1.5 s; swirl + eTeacher card | **PARTIAL** | Swirl cut from ~2.5 s to 1 s, eTeacher card 1 s still there, card now 4 s but the button/URL only for ≈1.3 s. |
| P1-7 | "954 38 YEAR OLD" unreadable | **NOT FIXED** | Ad1 5.5–7.0 s "954 38 YEAR OLD"; Ad3 "954 38-YEAR-OLD". |
| P1-8 | Ad2 face changes at 30 s join | **PARTIAL** | v7: sharpness/skin consistent across the take, but a visible framing/position jump at 24.5 s (punch-in seam). |
| P1-9 | Captions stack two lines at crossfades | **NOT FIXED** | ASS chunks overlap 0.05 s with 40 ms fades; stacked lines at Ad1 7.5 s and 25.5 s. |
| P1-10 | Ad1 "She's at Longevity Life Academy" | **FIXED** | Now "She's one of the founding teachers at Longevity Life Academy" (single continuous take, no jump cut). |
| P2-11 | "6.5 years every decade" vs site "8 months a year" | **NOT FIXED** | Script keeps 6.5/decade (matches BRIEF product facts, so arguably by design). |
| P2-12 | No qualifier on "second slowest aging person on Earth" | **NOT FIXED** | Offer card says "#2 slowest aging person on Earth, 2023" — no "Rejuvenation Olympics". |
| P2-13 | Top strap tiny, in top UI zone, fades at cuts | **NOT FIXED** | 42 px, MarginV 120, fades out before Zoom and back after. |
| P2-14 | Ad1 pinch gesture on "single mom" | **FIXED** | New Ad1 take; 39–41 s shows no pinch gesture (ad1_tile_1p5.png). |
| P2-15 | "SIGN UP NOW" vs site "Enroll now" | **NOT FIXED** | render_offer.py still "SIGN UP NOW". (Omri asked for "SIGN UP NOW" in T22 — keep, but note.) |
| P2-16 | Same script in every ad, only actor varies | **NOT FIXED** | All three use the identical script (by Omri's choice, T22). |

Score movement (my estimate on Claude's scale): Ad1 v5 ≈ 6/10, Ad2 v7 ≈ 5.5/10 (seam), Ad3 v6 ≈ 6/10 — gains from continuous takes, correct offer card, 4-s end card, timed music; held back by unchanged P0-1/P0-2/P0-5, stacked captions, true-peak miss, hard cuts.

## D. Priority fix list (all ads, in order)
1. Replace fake press collage (P0-1) — legal/Meta risk, contradicts "$100 a month".
2. True peak → ≤ −1.5 dBTP (audio-only remux).
3. Caption engine: hard cuts, no overlap; caption the VIP/Q&A line inside the Zoom shot; ≥ 110 px; "954 PEOPLE · ALL 38".
4. Open on the face (or a real Julie shot with sound); drop blur-fill swirl/eTeacher card; hold full offer card ≥ 3 s.
5. Strap: bigger, lower, steady (also carries "Masterclass of the Year" before the 21-s spoken mention).
6. Dissolves at overlay boundaries; keep cuts motivated as they already are.
7. Ear-check: "New Zealandans" (Ad2/Ad3), "Thank you for watching" tail, 1.12× pacing.
8. Ad2: cover the 24.5 s seam; true peak −1.4 dBTP also fails there.
9. Then the 45/75 s cuts and 4x5/1x1/16x9 (row 21) with the same checks per file.

---
# v8 RE-CHECK (2026-09-30 19:25 UTC) — `final-versions/videos/*__9x16__60.mp4`
Evidence: `audit_ad{1,2,3}_v8.log` (LANG en 1.0, transcript = script; 54/58, 55/57, 53/58 captions matched — the "unmatched" lines are spelling normalisations 38-YEAR-OLD / ZEALANDERS / MASTERCLASS / BRYAN / FULL-TIME, all present on screen), my ebur128, tiles `audit_frames/v8_*.png`.
Measured: ad1 59.10 s · −14.3 LUFS · TP −2.8 | ad2 59.10 s · −14.0 · TP −2.9 | ad3 59.80 s · −14.6 · TP −2.8. Sizes local = live (36247752 / 39602281 / 38993312 bytes, HTTP 200 for index and all three mp4s at https://gitteromri-ux.github.io/final-versions/).

| Row | Item | v5–v7 | v8 | Evidence |
|---|---|---|---|---|
| A-2 | Opener wording / "Zealandans" voice (ad2, ad3) | PARTIAL | PARTIAL (unchanged) | audit_ad2/3_v8 still transcribe "New Zealandans"; captions correct. Ear check still owed. |
| A-3 | "Masterclass of the Year" visible early / strap | PARTIAL | PASS | Strap now 54 px two-line at MarginV 235, steady from 1.4 s, below top-UI zone (v8_ad1_tile.png). Spoken mention still ~20/22/23 s (by script). |
| A-7 | Scarcity / refund line | PARTIAL | PARTIAL | Refund still 34 px, but now on screen ≈2.3 s. |
| A-8 | DOAC captions | PARTIAL | PARTIAL→ mostly PASS | Hard cuts, no stacked lines at 7.5/10.5/25.5 s; "954 38-YEAR-OLD" highlighted (still numeric pair, Claude P1-7 wording not adopted); size still 94 px; VIP/Q&A line still uncaptioned inside the Zoom shot (v8_ad1_zoom.png 1.5–5.5 s); leftover-caption-on-dark-frame fixed. |
| A-9 | Julie opener / closer, blur-fill | PARTIAL | PARTIAL | Opener still LLA logo on black, silent, 0–~1.0 s; swirl still blur-filled (52.5–53.5 s ad1) but now dissolved in/out and eTeacher card cut to ~0.5 s. |
| A-10 | PR pop-up | PARTIAL | PARTIAL | Now alpha-faded in/out (smooth). Content still the fake press collage — Claude P0-1 unchanged. |
| A-11 | Offer card hold | PARTIAL | PASS | Card 5.0 s (54.1–59.1 ad1); SIGN UP NOW visible ≈2.9 s, URL ≈2.5 s (v8_ad1_end.png). |
| A-13/25 | Larger-than-life / human | PARTIAL | PARTIAL | Speed still 1.12× on ad1/ad3 (subjective, ASSUMED). |
| A-15 | Scene consistency ad2 | PARTIAL | PARTIAL (unchanged) | Visible framing/head-position jump at ~23.5 s (v8_ad2_seam.png 2.25→2.50). |
| A-16 | GitHub page | PARTIAL | PASS for the 3 masters | 200 + Content-Length match; page also lists 4x5/75-s files now present (not audited here). |
| A-18/22 | Smooth transitions | FAIL | PASS | 0.3–0.4 s dissolves opener→UGC, UGC→swirl→card; overlays alpha-faded. |
| A-19 | Audit completeness | PASS | PASS | v8 logs exist for all three; "Thank you" tail no longer in transcripts (ad1) — still listen once. |
| A-20 | Output contract / true peak | FAIL (TP) | PASS | TP −2.8/−2.9/−2.8 dBTP, LUFS −14.0…−14.6, durations 59.1/59.1/59.8 (60 ± 1.5 ✔). |
| A-21 | 45/60/75 × 4 formats | NOT YET | NOT YET | 9 of 36 files exist (3×9x16-60, 3×9x16-75, 2×4x5-60 …); 45-s, 1x1, 16x9 missing. |
| A-28 | Safe area | PASS | PASS | Strap moved down; Zoom headline still at y≈60–110 (top-UI risk). |
| C P0-1 | Fake press cards | not fixed | **NOT FIXED** | ad1 30–32 s, ad3 33–35 s. Still the launch blocker. |
| C P0-2 | Logo-on-black open | not fixed | NOT FIXED | 0–1.0 s. |
| C P0-4 | "$49. I'm in." after VIP | not fixed | NOT FIXED (audio) | Card clarifies. |
| C P0-5 | AI disclosure | not fixed | NOT FIXED | Omri decision. |
| C P1-6 | CTA hold / swirl | partial | PASS | 5-s card, ~2.9 s button. |
| C P1-7 | "954 38" readability | not fixed | PARTIAL | Highlighted, hyphenated; wording not changed. |
| C P1-8 | Ad2 join | partial | PARTIAL | Seam at 23.5 s. |
| C P1-9 | Stacked captions | not fixed | **FIXED** | No double lines in 1.5-s or 4-fps tiles. |
| C P2-13 | Strap | not fixed | **FIXED** | 54 px, lower, steady. |
| C P2-11/12/15/16 | numbers / qualifier / "Enroll" / same script | not fixed | NOT FIXED | Deliberate per BRIEF/T22. |

**v8 score (Claude scale):** ad1 ≈ 7/10, ad3 ≈ 7/10, ad2 ≈ 6.5/10 (seam). Remaining blockers before "live": P0-1 fake press collage, AI-disclosure decision, ear-check of "Zealandans" (ad2/ad3) and 1.12× pacing; then the missing 27 format/duration files.
