# META UPLOAD SPEC · LLA Julie Masterclass UGC ads (v5)

Status: DRAFT FOR OMRI'S APPROVAL. Nothing here is uploaded or changed in Ads Manager until Omri says go.

## 0. Hard rules (read first)

- GOLDEN CAPI FREEZE until 2026-10-26: do NOT touch the pixel, Conversions API, events, datasets, domain verification, existing ad sets, budgets, audiences, or existing ads.
- These are NEW ADS ONLY, added to the existing standard-video test ad set **03**. No new campaign, no new ad set, no edits to ad set 03 settings.
- Every ad is created as "Create new ad" inside ad set 03, status **Paused** until Omri approves.
- No purchases, no new tools. Label claims VERIFIED / ASSUMED.
- VERIFIED from handover-master `_today-log.md` (2026-09-30 19:40 IDT): ad set 03 is now Highest volume, 35–65+, broad, **Facebook feed + Facebook reels overlay only**, and the standing rule is **NO edit of any kind on sets 01/03 until 7 Oct 19:40 IDT except pausing an ad with Omri's approval**. Adding new ads to set 03 counts as an edit under that rule → needs Omri's explicit lift. With the current placement set, only the **4x5** (feed) and **9x16** (reels overlay) files will actually serve; 1x1/16x9 are prepared for later use only.

## 1. Destination

- URL (exact, no trailing changes): `https://www.longevitylifeacademy.com/julie-masterclass/`
- VERIFIED 2026-09-30 17:59 UTC: `curl -sS -o /dev/null -w "%{http_code}" -A "Mozilla/5.0" https://www.longevitylifeacademy.com/julie-masterclass/` → **200**, no redirect.
- UTM suggestion (append to the URL in the "URL parameters" field, not in the Website URL field, so the pixel/URL match is untouched):
  `utm_source=facebook&utm_medium=paid&utm_campaign=julie-masterclass&utm_content=<slug>__<fmt>__<dur>`
  Example: `utm_content=ad1-man42__9x16__60`. ASSUMED: current ad set 03 ads use another UTM scheme — check before adding so attribution reports stay comparable.
- CTA button: **Sign Up**.

## 2. File → placement matrix

Files: `/home/user/workspace/final-versions/videos/<slug>__<fmt>__<dur>.mp4` (slug ∈ ad1-man42 | ad2-woman42 | ad3-woman51; dur ∈ 45 | 60 | 75). Upload each ad with placement asset customisation (one ad, four crops) so the Meta learning phase is not split across four ads.

| Format | Resolution | Placements (asset customisation) | File |
|---|---|---|---|
| 9x16 | 1080x1920 | Facebook Reels, Facebook Stories, Instagram Reels, Instagram Stories, Messenger Stories, Ads on Reels | `<slug>__9x16__<dur>.mp4` |
| 4x5 | 1080x1350 | Facebook Feed, Facebook Video Feeds, Marketplace, Instagram Explore, Instagram Explore home | `<slug>__4x5__<dur>.mp4` |
| 1x1 | 1080x1080 | Instagram Feed, Instagram Profile feed, Facebook right column, Search results | `<slug>__1x1__<dur>.mp4` |
| 16x9 | 1920x1080 | Facebook In-stream video, Audience Network native/banner/interstitial, Audience Network rewarded video | `<slug>__16x9__<dur>.mp4` |

Duration per placement (recommendation): 60 s as the default on all placements; 45 s for Reels/Stories if the 60 s Reels hook-rate is weak; 75 s only in Feed/In-stream. In-stream requires ≥ 5 s and ≤ 10 min, Stories/Reels accept up to 60 s without splitting into cards; 75 s Stories will be split into cards — do not use the 75 s files on Stories.

Start with 3 ads (one per slug), 60 s, all four crops. That is 12 files. Add 45/75 variants as separate ads only after the first read.

## 3. Meta video spec compliance

Files produced per BRIEF.md output contract: H.264 High, yuv420p, 30 fps, CRF ≤ 18, AAC 192 kbps 48 kHz stereo, +faststart, −14 LUFS ±1, TP ≤ −1.5 dBTP. Meta requirements and how we meet them:

| Meta requirement | Our file | Status |
|---|---|---|
| Codec H.264 (or H.265), progressive, square pixels | H.264 High, yuv420p, progressive | OK |
| Container MP4/MOV, moov atom at start | MP4 +faststart | OK |
| File size ≤ 4 GB | ~10–60 MB per file | OK |
| Frame rate ≤ 30 fps | 30 fps constant | OK |
| Audio AAC stereo ≥ 128 kbps, 48 kHz | AAC 192 kbps 48 kHz stereo | OK |
| Loudness: no hard requirement; Meta normalises, −14 LUFS is fine | −14 LUFS / −1.5 dBTP | OK |
| Min width 1080 px for Reels/Stories, 1080x1080 feed | per matrix | OK |
| Length: Feed ≤ 241 min, Stories/Reels ≤ 60 s recommended, In-stream 5 s–10 min | 45/60/75 s | OK (75 s not for Stories) |
| Safe zones: Reels/Stories keep text out of top ~14% (250 px) and bottom ~35% (~340 px of 1920) | Captions are placed inside the safe area by the pipeline; eyeball tiles before upload | VERIFY per file (qc.json) |
| Captions | Burned in (open captions), so no SRT is required | OK — but still upload captions (see below) |

Captions recommendation: also upload the transcript as a caption file (SRT, en_US) per ad or use Meta auto-captions and review. Reason: closed captions feed Meta's accessibility/relevance signals and remain usable if a placement crops the burned-in text. Source: the whisper transcript in each `<name>.qc.json`. Never rely on burned-in captions alone for 16x9 In-stream, where the player UI overlaps the bottom.

Thumbnail: pick a frame from the UGC talking head (not the opener statistics card) at ~3–5 s. Text on the thumbnail is fine (no 20% rule anymore) but keep it minimal.

## 4. Copy (Omri's rules: name product, provider, price, dates explicitly; short sentences; no hype words; cynical audience)

Product line to use verbatim: **The Longevity Masterclass of the Year with Julie Gibson Clark** · **Longevity Life Academy by eTeacher Group** · **$49 / VIP $79** · **Tue Oct 27, 7 PM ET or Sat Nov 14, 1 PM ET** · **60 min live on Zoom** · **14-day refund**.

All facts below are VERIFIED per BRIEF.md (2026-09-29). Forbidden words: unlock, transform, journey, secret, hack, revolutionary, game-changer.

### Ad 1 · ad1-man42 (man, 42)

Primary text A
Julie Gibson Clark was the #2 slowest-aging person on Earth in 2023. Ahead of Bryan Johnson and his $2M a year. She spends about $100 a month.
She teaches her exact protocol live on Zoom. 60 minutes. Tue Oct 27, 7 PM ET or Sat Nov 14, 1 PM ET.
The Longevity Masterclass of the Year. Longevity Life Academy by eTeacher Group. $49. VIP $79 (private Q&A + $249 course credit). 14-day refund.

Primary text B
954 people, all 38 years old, were tested. Biologically, the youngest was 28. The oldest was 61. Same birth year.
Julie Gibson Clark ages about 6.5 years per decade. Measured, not claimed. Rejuvenation Olympics, 2023, #2 worldwide.
One live class, 60 min on Zoom: The Longevity Masterclass of the Year, Longevity Life Academy by eTeacher Group. $49, VIP $79. Oct 27 7 PM ET or Nov 14 1 PM ET. 14-day refund.

Primary text C
Everyone sells longevity. Almost nobody can prove it. Julie Gibson Clark can. Single mom, full-time job, ~$100 a month.
Live on Zoom, 60 min, she shows what she actually does. Questions answered.
The Longevity Masterclass of the Year, Longevity Life Academy by eTeacher Group. Tue Oct 27 7 PM ET or Sat Nov 14 1 PM ET. $49 / VIP $79. Refund within 14 days, no questions.

Headlines (≤ 40 chars)
1. Julie Gibson Clark, live on Zoom. $49
2. #2 slowest-aging person on Earth. $49
3. Longevity Masterclass · Oct 27 or Nov 14

Description (≤ 30 chars recommended)
60 min live · $49 · 14-day refund

### Ad 2 · ad2-woman42 (woman, 42)

Primary text A
Bryan Johnson spends $2M a year. Julie Gibson Clark spends about $100 a month and ranked ahead of him. 2023 Rejuvenation Olympics, #2 on Earth.
Her protocol, live on Zoom, 60 minutes, with Q&A. The Longevity Masterclass of the Year, Longevity Life Academy by eTeacher Group.
Tue Oct 27, 7 PM ET or Sat Nov 14, 1 PM ET. $49. VIP $79. 14-day refund.

Primary text B
Same birth year, 33 years apart in biological age. That was the result of a real study of 954 38-year-olds.
Julie Gibson Clark's body ages 6.5 years per decade. She has a full-time job and a kid. No lab, no staff.
She teaches it once, live: The Longevity Masterclass of the Year, Longevity Life Academy by eTeacher Group. 60 min on Zoom. $49 / VIP $79. Oct 27 or Nov 14. 14-day refund.

Primary text C
No supplements to buy. No app. One 60-minute live class on Zoom with the woman who out-ranked Bryan Johnson in 2023.
The Longevity Masterclass of the Year with Julie Gibson Clark. Longevity Life Academy by eTeacher Group.
Tue Oct 27 7 PM ET or Sat Nov 14 1 PM ET. $49, VIP $79 includes a 30-min private Q&A. 14-day refund.

Headlines
1. Julie Gibson Clark's protocol. Live. $49
2. Ahead of Bryan Johnson at $100/month
3. Live on Zoom · Oct 27 or Nov 14 · $49

Description
Longevity Life Academy · 14-day refund

### Ad 3 · ad3-woman51 (woman, 51)

Primary text A
I am 51. I do not want promises. I want the numbers.
Julie Gibson Clark: #2 slowest-aging person on Earth, 2023. Ages 6.5 years per decade. About $100 a month.
She teaches her exact protocol live on Zoom, 60 min. The Longevity Masterclass of the Year, Longevity Life Academy by eTeacher Group. Tue Oct 27 7 PM ET or Sat Nov 14 1 PM ET. $49 / VIP $79. 14-day refund.

Primary text B
Two people born the same year can be 33 years apart biologically. The study tested 954 people at 38. Youngest body: 28. Oldest: 61.
Which side of that gap you land on is mostly what you do daily. Julie Gibson Clark does it on a single mom's budget and time.
60 min live on Zoom: The Longevity Masterclass of the Year, Longevity Life Academy by eTeacher Group. $49, VIP $79. Oct 27 or Nov 14. 14-day refund.

Primary text C
$49. 60 minutes. One live class on Zoom. Full refund within 14 days if it was not worth it.
Teacher: Julie Gibson Clark, ranked #2 in the world for slowest aging in 2023, ahead of Bryan Johnson. Founding faculty at Longevity Life Academy by eTeacher Group.
The Longevity Masterclass of the Year. Tue Oct 27, 7 PM ET or Sat Nov 14, 1 PM ET. VIP $79 adds a 30-min private Q&A and a $249 credit toward the Longevity Blueprint course.

Headlines
1. 60 min with Julie Gibson Clark. $49
2. Longevity, measured. Not promised.
3. Oct 27 or Nov 14 · Live on Zoom · $49

Description
$49 · VIP $79 · 14-day refund

## 5. Ad build checklist (per ad, inside ad set 03)

1. Ad name: `v5__<slug>__<dur>` (e.g. `v5__ad1-man42__60`).
2. Identity: existing LLA Facebook Page + Instagram account already used in ad set 03 (do not change).
3. Format: Single video. Upload 9x16 file, then "Edit placement" → replace with 4x5, 1x1, 16x9 files per the matrix.
4. Primary text: add all 3 variants (Meta multiple text options). Headlines: all 3. Description: 1.
5. Captions: upload SRT built from the qc.json transcript, or auto-generate and review.
6. CTA: Sign Up. Website URL: exact URL from section 1. URL parameters: the UTM string with the correct `utm_content`.
7. Tracking section: leave exactly as inherited (pixel already selected at ad set/account level). Do not add or remove anything.
8. Advantage+ creative enhancements: turn OFF (music, visual touch-ups, text improvements) — burned-in captions and loudness are final.
9. Save as Paused. Send Omri the preview links. Publish only after approval.

## 6. Not done / open

- Video files are still being rendered (matrix in progress); this spec references the naming contract, not verified files. Check each `.qc.json` for duration, LUFS, captions_matched before upload.
- ASSUMED: ad set 03 uses placement asset customisation and the Sign Up CTA is enabled for its objective. Confirm in Ads Manager before creating ads.
- No SRT files generated yet; build from qc.json transcripts when the files land.
