# UGC ads — Claude fix pass (all 18 files)

Separate from Perplexity's work: nothing in `main`, `videos/` or the live page was changed. These files live only in `claude-fixes/` on branch `claude/ugc-fixes`.

## What was fixed in every file

1. **Silent logo opener removed** — every file now opens on the presenter's face with the first word within ~0.2 s.
2. **Fake press collage replaced** — real coverage cards with the headlines verbatim as published: Fortune (Nov 4, 2023), Business Insider (Nov 6, 2023), The Sun (2024). Outlet names as text, no imitation mastheads.
3. **Jump cuts and AI seams covered** with full-screen cards while the voice continues (hard cut in and out, text on screen within 3 frames, dead air inside the cut trimmed, captions carried across in the same style): Ad 2 — the "28 vs 61" jump cut, the regeneration seam (dates card) and the "founding faculty" jump cut; Ad 3 — the seam before the dates (dates card); every 45 s cut — "28 vs 61 · 33 years apart" restores the dropped payoff and "$2M a year vs ~$100 a month" restores the dropped proof (Ad 2 / Ad 3 45 s also get the dates card).
4. **No face-on-face dissolves** — face→Zoom is a hard cut onto an eased Zoom-in (no frozen or shrinking title frame), Zoom→face is a hard cut; press and cover cards cut in and out cleanly.
5. **VIP line captioned** inside the Zoom shot ("FOR ONE HOUR. / VIP STAYS FOR / A PRIVATE Q&A / ABOUT YOUR OWN GOALS.").
6. **Ending rebuilt** — chrome swirl, white→black flash and eTeacher card removed. "I'm in" cuts straight to a new offer card that builds immediately and holds ~4 s: Masterclass of the Year, with Julie Gibson Clark, No. 2 on the Rejuvenation Olympics leaderboard 2023, Live on Zoom · 60 min, Tue Oct 27 · 7 PM ET / Sat Nov 14 · 1 PM ET, $49, VIP $79 (+ private 30-min Q&A, + $249 Blueprint credit), SIGN UP NOW, URL, 14-day refund. On 9:16 everything sits inside the top 75% (clear of the Reels caption/CTA area).
7. **Dead air filled** — a low room-tone bed under the whole ad (no more digital silence in pauses); music after "I'm in" ramps in instead of slamming; loudness −14 LUFS, true peak ≤ −1.5 dBTP.
8. **16:9 rebuilt** as a side-panel layout (the vertical video next to a brand panel with title, dates, price, URL) instead of a blown-up crop; full-frame 16:9 offer card at the end.
9. **Ad 1 judder smoothed** — the 24→30 fps duplicate frames in the talking take are motion-blended (duplicates in a sample second: 20/59 → 1/59), captions untouched.
10. **Ad 2 second half matched** — light sharpening + fine grain from the regeneration seam so it no longer looks softer than the first half.

## Not fixable from the finished files (needs the source pipeline)

- Music bed under the first ~34 s (needs the music stem; room tone covers the dead air for now).
- Ad 2's "New Zealand-ins" pronunciation (needs a re-voice).
- Captions burned into the talking take keep their original timing (e.g. "954 38-YEAR-OLD" ~0.5 s late); all new captions are word-timed.
- 4:5 and 1:1 talking-head crops (hairline) are Perplexity's framing; only the edits above were applied.
- AI-generated names on the Zoom gallery tiles and the tight date margin in the 1:1 Zoom shot are in the generated footage.
- The "75" slot: Perplexity's originals run 67–72 s, not 75 s. After removing the silent opener, the swirl/eTeacher ending and dead air they run ~59–63 s. Reaching 75 s needs new footage.

## Files

| Ad | Format | Length | Duration | LUFS | True peak | Black frames | Download |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Ad 1 · Man 42 | 9:16 | 60 slot | 55.63 s | -14.0 | -2.2 dBTP | none | [mp4](https://raw.githubusercontent.com/gitteromri-ux/final-versions/claude/ugc-fixes/claude-fixes/videos/ad1-man42__9x16__60.mp4) (39.3 MB) |
| Ad 1 · Man 42 | 9:16 | 45 slot | 42.13 s | -14.2 | -2.2 dBTP | none | [mp4](https://raw.githubusercontent.com/gitteromri-ux/final-versions/claude/ugc-fixes/claude-fixes/videos/ad1-man42__9x16__45.mp4) (29.1 MB) |
| Ad 1 · Man 42 | 9:16 | 75 slot | 59.37 s | -14.2 | -2.3 dBTP | none | [mp4](https://raw.githubusercontent.com/gitteromri-ux/final-versions/claude/ugc-fixes/claude-fixes/videos/ad1-man42__9x16__75.mp4) (41.1 MB) |
| Ad 1 · Man 42 | 4:5 | 60 slot | 55.63 s | -14.1 | -2.3 dBTP | none | [mp4](https://raw.githubusercontent.com/gitteromri-ux/final-versions/claude/ugc-fixes/claude-fixes/videos/ad1-man42__4x5__60.mp4) (29.5 MB) |
| Ad 1 · Man 42 | 1:1 | 60 slot | 55.63 s | -14.1 | -2.3 dBTP | none | [mp4](https://raw.githubusercontent.com/gitteromri-ux/final-versions/claude/ugc-fixes/claude-fixes/videos/ad1-man42__1x1__60.mp4) (24.2 MB) |
| Ad 1 · Man 42 | 16:9 | 60 slot | 55.63 s | -14.0 | -2.2 dBTP | none | [mp4](https://raw.githubusercontent.com/gitteromri-ux/final-versions/claude/ugc-fixes/claude-fixes/videos/ad1-man42__16x9__60.mp4) (19.0 MB) |
| Ad 2 · Woman 42 | 9:16 | 60 slot | 54.97 s | -13.9 | -2.5 dBTP | none | [mp4](https://raw.githubusercontent.com/gitteromri-ux/final-versions/claude/ugc-fixes/claude-fixes/videos/ad2-woman42__9x16__60.mp4) (39.1 MB) |
| Ad 2 · Woman 42 | 9:16 | 45 slot | 41.6 s | -14.1 | -2.4 dBTP | none | [mp4](https://raw.githubusercontent.com/gitteromri-ux/final-versions/claude/ugc-fixes/claude-fixes/videos/ad2-woman42__9x16__45.mp4) (28.7 MB) |
| Ad 2 · Woman 42 | 9:16 | 75 slot | 58.57 s | -14.1 | -2.3 dBTP | none | [mp4](https://raw.githubusercontent.com/gitteromri-ux/final-versions/claude/ugc-fixes/claude-fixes/videos/ad2-woman42__9x16__75.mp4) (41.3 MB) |
| Ad 2 · Woman 42 | 4:5 | 60 slot | 54.97 s | -14.0 | -2.3 dBTP | none | [mp4](https://raw.githubusercontent.com/gitteromri-ux/final-versions/claude/ugc-fixes/claude-fixes/videos/ad2-woman42__4x5__60.mp4) (28.2 MB) |
| Ad 2 · Woman 42 | 1:1 | 60 slot | 54.97 s | -14.0 | -2.3 dBTP | none | [mp4](https://raw.githubusercontent.com/gitteromri-ux/final-versions/claude/ugc-fixes/claude-fixes/videos/ad2-woman42__1x1__60.mp4) (24.1 MB) |
| Ad 2 · Woman 42 | 16:9 | 60 slot | 54.97 s | -13.9 | -2.5 dBTP | none | [mp4](https://raw.githubusercontent.com/gitteromri-ux/final-versions/claude/ugc-fixes/claude-fixes/videos/ad2-woman42__16x9__60.mp4) (16.7 MB) |
| Ad 3 · Woman 51 | 9:16 | 60 slot | 55.47 s | -14.1 | -2.2 dBTP | none | [mp4](https://raw.githubusercontent.com/gitteromri-ux/final-versions/claude/ugc-fixes/claude-fixes/videos/ad3-woman51__9x16__60.mp4) (36.3 MB) |
| Ad 3 · Woman 51 | 9:16 | 45 slot | 41.07 s | -14.2 | -2.0 dBTP | none | [mp4](https://raw.githubusercontent.com/gitteromri-ux/final-versions/claude/ugc-fixes/claude-fixes/videos/ad3-woman51__9x16__45.mp4) (26.5 MB) |
| Ad 3 · Woman 51 | 9:16 | 75 slot | 62.67 s | -14.2 | -2.2 dBTP | none | [mp4](https://raw.githubusercontent.com/gitteromri-ux/final-versions/claude/ugc-fixes/claude-fixes/videos/ad3-woman51__9x16__75.mp4) (40.4 MB) |
| Ad 3 · Woman 51 | 4:5 | 60 slot | 55.47 s | -14.2 | -2.4 dBTP | none | [mp4](https://raw.githubusercontent.com/gitteromri-ux/final-versions/claude/ugc-fixes/claude-fixes/videos/ad3-woman51__4x5__60.mp4) (28.3 MB) |
| Ad 3 · Woman 51 | 1:1 | 60 slot | 55.47 s | -14.2 | -2.4 dBTP | none | [mp4](https://raw.githubusercontent.com/gitteromri-ux/final-versions/claude/ugc-fixes/claude-fixes/videos/ad3-woman51__1x1__60.mp4) (24.8 MB) |
| Ad 3 · Woman 51 | 16:9 | 60 slot | 55.47 s | -14.1 | -2.2 dBTP | none | [mp4](https://raw.githubusercontent.com/gitteromri-ux/final-versions/claude/ugc-fixes/claude-fixes/videos/ad3-woman51__16x9__60.mp4) (18.1 MB) |
