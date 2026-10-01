# Julie Film v4 Audit — Master + 75/60/45 s Cutdowns

Oct 1, 2026 · Omri

Files audited: `lla-masterclass-assets/video/julie-masterclass-film-full-1080p-masterclass-edit.mp4` (v4 master, 2:17) and `julie-film-v4/video/cuts/LLA_Julie_Masterclass_{75,60,45}s_16x9.mp4`.

## Summary

Film v4 is a real step up, from 5/10 to **7/10 as the landing-page hero**. 11 of the 17 claimed fixes hold, 2 are accepted decisions, 3 are partial and 1 is not fixed. Two of the patches created new editing errors a viewer will catch. The cutdowns score 5–6/10 for paid social: none has subtitles, and two proof cards flash for 0.4 s.

| File | Length · format | Before | Now | Main blocker |
| --- | --- | --- | --- | --- |
| Master v4 | 2:17 · 16:9 · −18 LUFS | 5 hero · 3 paid | **7 hero · 5 paid** | Press cards (C1); search-patch failure at 1:42 (E1) |
| Cutdown 75 s | 1:12 · 16:9 · −14 LUFS | — | **6** | No subtitles; 0.4 s flash cards; cut to black |
| Cutdown 60 s | 0:59 · 16:9 · −14 LUFS | — | **6** | Same, plus 13 s of consecutive title cards |
| Cutdown 45 s | 0:42 · 16:9 · −14 LUFS | — | **5** | Same, plus a story gap after "I did the opposite" |

**Blocks go-live everywhere:** the press cards (C1). The cards in v4 are the LLA-designed cards stored in the site repo (`assets/press/`), but the live page does not show them. Their headlines are rewritten, not the real ones. Fortune's real headline is "Wealthy men are spending millions… These women are beating them with cheaper solutions", while the card says "Tech bros spend millions chasing immortality. She is beating them." Business Insider's real headline says "around $108 a month", while the card says "$12 a day" (about $360/month). Fix: put the real headlines from the site's press section on the cards, verbatim.

**Blocks paid use of the cutdowns:** no subtitles (K1). Most feed views are muted, and a muted viewer sees 9–12 s of talking head with no words.

**How it was audited:** every transition was checked at all 30 fps, 0.5 s either side, plus 1–4 fps contact sheets of every file. Julie's voice-over was checked with offline speech recognition (word timings) and lined up with each edit. Loudness was measured with ebur128; black frames, freezes, frame rate and encode settings were also checked. All four files are CFR 30 fps, progressive, faststart, with no clipping. Each editing error was then re-checked by an independent skeptic agent trying to refute it (one finding was withdrawn). The 9:16, 1:1 and 4:5 cutdowns weren't on the page yet.

## Film v4 — the 17 claimed fixes, checked

11 fixes hold, 2 are accepted decisions, 3 are partial (two of them introduce new editing errors), and 1 is not fixed.

| # | Claimed fix | Verdict | What the file actually shows |
| --- | --- | --- | --- |
| 1 | Press cards replaced with "approved site press cards" | **Not fixed** | Same LLA-made cards from `assets/press/`, which the live page does not display. The headlines are rewritten (Fortune, Business Insider "$12 a day") under real mastheads. |
| 2 | Offer panel with both dates and prices (2:01) | Fixed | Tue Oct 27 · 7 PM ET / Sat Nov 14 · 1 PM ET, From $49 · VIP $79, URL. Clear and readable. |
| 3 | End card with dates, price, URL | Fixed | All present, Trustpilot labelled. |
| 4 | Phone gibberish replaced (1:47–1:48) | **Partial** | "Glucose · 98 mg/dL · Daily summary" is fixed, but the clock still reads "1:91" and the axis reads 200 / 200 / 200 / 200 / 100 / 30. |
| 5 | Trustpilot labelled | Fixed | "Trustpilot rating of eTeacher Group, the school behind Longevity Life Academy". |
| 6 | MarketWatch replaced by Fortune | Fixed | The subtitle under "As seen on" still says "National press coverage · July 2026", but Fortune's coverage is from 2023–24. |
| 7 | Julie-only faculty card | Fixed | Clean; no other teachers, no cursor. |
| 8 | Toothbrush B-roll replaced | Fixed, with a new error | The "AUTOMATIC." card works, but see editing error E5. |
| 9 | Search query replaced (1:42) | **Partial, new errors** | The patch is visible as a box, and the old query flashes back (E1). The next shot still shows "mediterranean diet longevity benefits" with gibberish UI ("Searn Now", "Sacudents", "Frravilets") at 1:43.8–1:44.7. |
| 10 | "$2M a year vs 3 things" | Fixed | Matches Julie's line. |
| 11 | LLA-branded Zoom class (1:33) | Fixed, with a new error | Old stock grid frames flash first (E2). The LLA logo repeats in 8 grid tiles. |
| 12 | Kinetic captions recoloured | Fixed | "RUNS OUT / TANK / EMPTIES" now read. |
| 13 | Dead air at the end trimmed | Fixed | Swirl 1.0 s + eTeacher card 1.2 s. |
| 14 | Light burst over Julie (1:52) | **Partial** | A cyan streak still passes over her lower face (1:51.8–1:52.8) and leaves a white hotspot on her mouth and chin (1:52.5–1:53.1). |
| 15 | Cutdowns at −14 LUFS | Fixed | Measured −14.1 / −14.0 / −14.0 LUFS, sample peak −1.3 / −1.3 / −1.5 dBFS. |
| 16 | 33.5% vs 34% | Decision — accepted | The exact figure is fine. |
| 17 | No course / 18 lessons / pillars in the voice-over | Decision — accepted | My speech pass agrees: no "18 lessons" or "pillars". "You need a curriculum that makes longevity automatic" remains. |

## Film v4 master — editing errors and remaining issues

Every transition was checked at all 30 frames per second, 0.5 s either side. The v4 patches introduced two new editing errors (E1, E2) that a viewer will catch.

| ID | Time | Priority | What happens on screen | Fix |
| --- | --- | --- | --- | --- |
| E1 | 1:41.53–1:42.23 | **P0** | The search-bar patch fails three ways. The original "healthspan and longevity course" shows unpatched at 1:41.53–1:41.57 (before the patch starts) and again at 1:42.20–1:42.23. At 1:41.60–1:41.67 and 1:42.10–1:42.17 the patch is a visible box with old-text residue poking out past its right edge, and it is sharp while the plate is motion-blurred. | Re-track the patch with matching blur and full coverage, or cut the shot. |
| E2 | 1:32.57–1:32.73 | **P1** | 6 frames of the old stock 9-person grid flash before the new LLA Zoom class: a blurred zoom on a woman in a white blouse pulling back to a 3×3 grid. It's the leftover head of the replaced shot. | Trim the 6 frames, or start the new shot at 1:32.57. |
| E3 | 1:43.8–1:44.7 | P1 | The second search close-up still has AI gibberish ("Searn Now", "Sacudents", "Frravilets", "Bo wciroy and feade at coxirelss") and the "mediterranean diet" query. The phone-wall shot that follows (to 1:44.7) carries the same garbled UI. | Blur or patch it, or cut it. |
| E4 | 1:47–1:48 | P2 | The phone clock reads "1:91". The chart axis reads 200 / 200 / 200 / 200 / 100 / 30. | Patch the clock and axis labels. |
| E5 | 0:54.27–0:54.73 | P1 | The cut lands while Julie is mid-word with her mouth open, onto an empty navy card. "AUTOMATIC." only appears 0.43 s later. | Put the word on screen at the cut, timed to her "automatic". |
| E6 | 1:50.1–1:53.1 | P2 | The cyan transition streak runs across the Zoom grid from 1:50.1, passes over Julie's lower face at 1:51.8–1:52.8, and leaves a white hotspot on her mouth and chin at 1:52.5–1:53.1. | Mask the streak off her face. |
| E7 | 2:07.7 and 2:08.7 | P2 | Dark wood cuts to a white swirl, then to black. That's two hard brightness jumps in 1 s, which reads as a strobe. | A 6-frame dip or dissolve on each cut. |
| E8 | 0:08.93–0:09.5 | P2 | About 0.6 s of black between "Held No. 2 on Earth" and the press collage fading in. | Overlap the press fade-in with the previous card. |
| E9 | 0:13.1 | P2 | The press collage hard-cuts to an empty starfield, and the text arrives 0.25 s later. There's no exit motion on the cards. | Short dissolve, or text on the first frame. |
| C1 | 0:09–0:13 | **P0** | Press cards: rewritten headlines under real mastheads, including Business Insider "$12 a day". | Use the real headlines from the site's press section, verbatim. |
| C2 | 1:35 | P2 | "National press coverage · July 2026" under the logos, but Fortune and The Sun are 2023–24. | Drop the date line or make it "2023–2026". |
| C3 | 1:33 | P2 | The LLA logo is repeated in 8 grid tiles of the Zoom class, which reads as filler. | Replace those tiles with participant faces. |
| A1 | whole film | P2 | Integrated loudness −18 LUFS (sample peak −0.9 dBFS). Fine for the website, but too quiet for social. | Use the −14 LUFS cutdowns for paid. |

All other boundaries are clean: the faculty card, the "Her protocol" card, the offer panel fade-in, the end card, the Zoom grid entry and the $2M/$100 cards. There are no frozen frames, no clipped audio and no clicks at edits.

## Film cutdowns 75 / 60 / 45 s (16:9)

The cutdowns are cut too mechanically. Two proof cards flash for 0.4 s, there are black and empty gaps, and none of the three has subtitles. The encoding is clean: CFR 30 fps, progressive, faststart, −14 LUFS.

| ID | Cut · time | Priority | What happens | Fix |
| --- | --- | --- | --- | --- |
| K1 | all three | **P0 (paid)** | No subtitles for Julie's voice. Only the 75 s cut has the kinetic "WILLPOWER / TANK / EMPTIES" words. A muted viewer sees 9–12 s of talking head with no text. | Burn in word-level captions, the same style as the UGC ads. |
| K2 | 75: 20.93–21.37 · 60: 13.90–14.33 · 45: 9.73–10.17 | **P1** | The "Pace of aging 0.665 · 33.5% slower" card is on screen for 13 frames (0.43 s) — a flash nobody can read. | Hold it at least 2 s, or drop it. |
| K3 | 75: 42.60–43.00 · 60: 29.47–29.87 · 45: 16.93–17.33 | **P1** | The "Learn longevity from the world's #2 slowest ager" card is on screen for 0.4 s. In the 60 s and 45 s cuts it follows the AUTOMATIC card, so two cards flash back to back. | Hold it at least 2 s, or drop it. |
| K4 | 75: 16.77 · 60: 9.73 | P1 | A hard cut from Julie to pure black (about 0.3 s), then a slow fade-up. The first press card shows about 0.57 s after the cut. It reads as a dropped clip. | Dissolve straight into the collage. |
| K5 | 75: 23.50 · 60: 16.47 · 45: 12.30 | P2 | Julie cuts to an empty navy frame (0.17 s) before the $2M bars start. | Start the card on its first drawn frame. |
| K6 | 75: 34.33 (0.43 s) · 60: 27.30 (0.43 s) | P1 | Julie cuts to a logo-only navy card, and "AUTOMATIC." appears 0.43 s later. Same as master E5. | Put the word on screen at the cut. |
| K8 | all three: 2.37 | P2 | The first punch-in lands on a blink (eyes shut on the first frame of the close-up). | Shift the cut 3–4 frames. |
| K9 | 45 s | P1 (story) | "…on a burst of motivation. I did the opposite." jumps straight to the Longevity Life Academy line. The "habits made so small… like brushing my teeth" explanation is cut, so "the opposite" is never explained. | Keep one habit sentence, or end that beat on "$100 a month". |
| K10 | 60 and 45 | P1 (pacing) | 13–14 s of consecutive title cards (Claim your seat → Zoom → faculty card → Her protocol) with no Julie on screen, which is about a third of the 45 s cut. | Cut one card. Put Julie's voice line over the Zoom shot. |
| K11 | all three | P2 | 16:9 plays small in a mobile feed, and the 4:5, 1:1 and 9:16 versions are not delivered yet. | Ship the vertical formats first for Meta. |
| K12 | 75 and 60 | P0 | The same press-card collage as the master. | As C1. |

(K7, a caption jump at 75 s 0:09.4, was withdrawn after the skeptic re-check: the caption holds steady across the cut.)

## Viewer's eye — watched as a person would, with sound

**Master (2:17).** It opens on 3 s of logo animation, then 6 s of dark data cards before Julie's face. On the website that's fine; in a feed nobody stays. The middle is the strongest stretch: Julie on camera, "willpower runs out", the $2M vs $100 bars, "AUTOMATIC — like brushing your teeth". It feels premium and human. Trust dips at 1:41–1:44: the phone montage is fast and blurry, the patched search bar looks pasted on, and a sharp-eyed viewer catches the old "healthspan…course" text and the gibberish UI. The close is clear for the first time: the dates and prices panel at 2:01, then the end card with the URL. The white swirl right after Julie's warm wood room is the one jarring moment.

**75 s.** Strong start: Julie's face and voice on frame 1, "Willpower is not the reason some people age slower". The kinetic words help. After the press collage, the two 0.4 s cards blink past and read as mistakes. The cut to black before the press looks like a dropped clip. It ends well: the offer panel, Julie's closing line on camera, then the end card for 5 s. It would work muted only if subtitles are added.

**60 s.** Same opening without the kinetic words, so the first 10 s are a talking head with no text. Around 0:33–0:47 it turns into a slideshow of four title cards in a row, and the energy drops. The offer panel and end card land.

**45 s.** The "I did the opposite" line now leads straight into Longevity Life Academy, without explaining what the opposite was, so the argument breaks. A third of the cut is title cards. As it stands, this is the weakest of the three.

## Scores per metric (1–10)

| Metric | Master v4 | 75 s | 60 s | 45 s |
| --- | --- | --- | --- | --- |
| Hook (first 3 s) | 4 (logo + cards) | 8 | 7 | 7 |
| Story / script | 8 | 7 | 6 | 4 |
| Editing & transitions | 5 (E1, E2, E5) | 5 (K2–K4, K6) | 5 | 5 |
| Visual craft | 8 | 8 | 8 | 8 |
| AI artifacts | 6 | 7 | 7 | 7 |
| On-screen copy accuracy | 7 | 7 | 7 | 7 |
| Claims & compliance | 4 (press cards) | 4 | 4 | 6 (no press) |
| Captions / subtitles | n/a (site) | 3 | 2 | 2 |
| Offer / CTA | 8 | 8 | 8 | 7 |
| Audio (level, edits) | 6 (−18 LUFS) | 8 | 8 | 8 |
| Technical encode | 9 | 9 | 9 | 9 |
| **Overall** | **7 hero · 5 paid** | **6** | **6** | **5** |

Fixing C1, E1, E2, K1, K2, K3 and K4 should take the master to about 8.5 for the website and each cutdown to about 8 for paid.

## Editor checklist (film)

**P0 — before anything goes live**

- [ ] C1: press cards use the real headlines from the site's press section, verbatim, in the master and the 75/60 s cuts
- [ ] E1: re-track the search-bar patch (1:41.53–1:42.23) so it is motion-blurred, fully covers the old text and never drops out, or cut the shot
- [ ] K1: burn word-level subtitles into all cutdowns

**P1 — before paid spend**

- [ ] E2: trim the 6 frames of the old stock grid at 1:32.57–1:32.73
- [ ] E3: blur or patch the gibberish search UI and phone wall at 1:43.8–1:44.7
- [ ] E5 / K6: put "AUTOMATIC." on screen on the first frame of the card
- [ ] K2 / K3: hold the "Pace of aging" and "#2 slowest ager" cards at least 2 s, or drop them
- [ ] K4: replace the hard cut to black and slow fade-up before the press collage with a dissolve
- [ ] K9: 45 s — restore one habit sentence after "I did the opposite"
- [ ] K10: 60/45 s — cut one of the four consecutive title cards

**P2 — polish**

- [ ] E4: clock "1:91" and axis labels on the phone (1:47–1:48)
- [ ] E6: mask the cyan streak and hotspot off Julie's face (1:51.8–1:53.1)
- [ ] E7: soften the wood → white swirl → black cuts (2:07.7, 2:08.7)
- [ ] E8 / E9 / K5: remove the empty and black lead-ins around the press and $2M cards
- [ ] K8: move the first punch-in off the blink (2.37 s)
- [ ] C2: fix the "July 2026" date line under "As seen on"
- [ ] C3: replace the 8 logo tiles in the Zoom grid with faces
- [ ] Deliver the 9:16, 4:5 and 1:1 cutdowns with the same fixes
