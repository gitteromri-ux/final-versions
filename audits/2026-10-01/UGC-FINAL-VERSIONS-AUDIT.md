# UGC Ads Final Versions Audit — 18 Files

Oct 1, 2026 · Omri

Files audited: `gitteromri-ux/final-versions` @ d5e85f7, `videos/` — Ad 1 (man42), Ad 2 (woman42), Ad 3 (woman51) × {9x16 60, 9x16 45, 9x16 "75", 4x5 60, 1x1 60, 16x9 60}.

## Summary

None of the 18 files is ready to go live; they score 3–6/10. The main problem is now editing, not copy. Every file has machine-made transitions that ghost faces into each other. Ad 2 and Ad 3 have visible seams with dead air inside the talking take. Every 45 s cut has hard jump cuts. The 16:9 versions are blown-up crops of the vertical and should not run. The best files are the **4:5 versions** (5–6/10).

| Ad | 9:16 60 s | 9:16 45 s | 9:16 "75" s | 4:5 | 1:1 | 16:9 | Worst problem |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Ad 1 · Man 42 | 5 | 4 | 4 | 5 | 5 | 3 | Ghosting dissolves, 24→30 fps judder, two jump cuts in the 45 |
| Ad 2 · Woman 42 | 5 | 5 | 5 | **6** | 5 | 3 | Jump cut at 18.9 s and regeneration seam at 24.0 s, each over dead air; softer second half |
| Ad 3 · Woman 51 | 5.5 | 5 | 4.5 | 5.5 | 5 | 4 | Frozen smile, doubled-face dissolve and 1.1 s of dead air at 26.5–27.7 s |

**Blocks launch everywhere (P0):**

1. The press-card collage (mock cards under real mastheads, "$12 a day") is still in all 18 files.
2. Jump cuts and AI-clip seams inside the talking take: Ad 2 at 18.87 s and 24.00 s, Ad 3 at 26.5–27.7 s, and every 45 s cut.
3. All three 16:9 files are soft, cropped close-ups (forehead and chin cut, strap across the forehead), and Ad 3's second date line sits on the bottom edge with no margin.

**Fix before paid spend (P1):** the ghosting dissolves (faces melting into Julie, the press cards and the chrome swirl); the 16:9 swirl inside 9:16 with blurred fill; the white→black flash before the end card; the CTA, which is fully visible for only about 2 s; the captions and CTA sitting under the Reels UI; no music under the first 34 s, which leaves dead-air gaps; the uncaptioned VIP line; and the "75 s" files, which are really 67–72 s and add nothing.

**How it was audited:** three agents ran in parallel, one per ad, covering 6 files each. Every transition was checked at all 30 fps, 0.5 s either side. Audio around every boundary was measured in 20 ms RMS windows. Speech was checked with offline recognition and lined up against OCR of the on-screen captions, and frame duplication (judder) was measured. The talking take was viewed at 4 fps in the 60 s masters and 2 fps in the other files. The serious editing errors were then re-checked by 12 independent skeptic agents trying to refute them. Their corrections are applied below: one claimed cut, Ad 3 45 s at 28.77, was withdrawn. Not checked: lip-sync in Ad 3, and caption OCR timing in the 45, 75, 4:5, 1:1 and 16:9 files (except where noted).

## Editing and transition errors

All three ads share one assembly pipeline, so they share the same transition defects at about the same timestamps. The 4:5, 1:1 and 16:9 files use the 60 s master's timeline frame for frame, so each master row below applies to them too. Times are Ad 1 / Ad 2 / Ad 3 in the 60 s masters.

| ID | Where | Priority | What a viewer sees | Fix |
| --- | --- | --- | --- | --- |
| T1 | 0.00–1.44 / 1.56 / 1.44 | P1 | Digital silence for about 0.9 s on a black LLA logo (which also reads "— Est. 2000 —"). The logo and its light streak then cross-fade over the face, and the first caption "PEOPLE BORN THE" appears about 0.45 s before the voice. | Open on the face and the voice at frame 0. |
| T2 | 29.67–29.83 / 29.4 / 32.43–32.60 | P1 | The first press card fades in as a hard-edged rectangle over the presenter's cheek, then the collage snaps in. | Clean cut on "In 2023". |
| T3 | 30.0–32.2 / 29.4–32.8 / 32.4–35.1 | P1 | Inside the collage, cards cross-fade so two Julie faces overlap (Ad 1 30.10–30.27). The top strap sits over the card headlines. Ad 3's collage shows 3–4 different-looking blonde women as "Julie". | Replace the cards (P0) and hide the strap during the collage. |
| T4 | 32.20–32.40 / 32.63–32.83 / 34.93–35.13 | P1 | Collage→face dissolve: the presenter's eyes appear over a press-card woman's face, so two faces show at once. | Hard cut or fast push. |
| T5 | 45.83–45.97 / 46.00–46.23 / 46.60–46.97 | P2 | Face→Zoom: Zoom tiles land on the presenter's nose and eyes as the face dims. The caption pops off mid-dissolve, and "LIVE ON ZOOM" scale-pops in. | Cut on "live". |
| T6 | 50.47–50.70 / 50.53–50.80 / 50.97–51.20 | **P1** | Zoom→face: an 8-frame dissolve puts Julie's Zoom face over the presenter's mouth and face (worst 4 frames, e.g. Ad 1 50.57–50.67, where two faces show at once), and "LIVE ON ZOOM" lingers over their head. | Hard cut, or a dissolve of 3 frames or fewer. |
| T7 | 52.50–52.80 / 52.50–52.87 / 53.10–53.43 | **P1** | The chrome-swirl sting fades in over the presenter's mouth while "I'M IN." is still on screen, so it reads as a face distortion or stain. | Let the caption clear, then hard-cut to the sting. |
| T8 | 52.8–53.8 (9:16 only) | P1 | The swirl is a 16:9 clip in a 9:16 frame with a zoomed, blurred copy above and below. Hard seams at about 34% and 66% of height. The 4:5, 1:1 and 16:9 files refit it full-frame and look fine. | Render a native 9:16 sting. |
| T9 | 53.80 / 53.80 / 54.43 (45 s: ~40.1; 75 s: 58.7 / 62.9) | P1 | Single-frame hard cut from a near-white swirl frame (luma about 190–205) to the near-black "by eTeacher Group" card (luma about 10). It lands as a flash. The card then holds dark about 0.3 s. | A 4–6 frame dip or dissolve. |
| T10 | 54.30–54.43 / 54.36–54.43 / 54.97–55.10 | P2 | "by eTeacher Group" ghosts under the offer title. On 4:5, 1:1 and 16:9 the wordmark runs nearly edge to edge. | Clear the card before the title enters; keep 8% margins. |
| J1 | Ad 2 · 18.87 · all 6 files | **P0** | Jump cut inside the take: an idle closed-mouth smile (18.50–18.83), then a hard cut at 18.87 — head clearly higher, lips parted, framing and background shift. Under it, about 0.58 s of near-silence with no room tone. | Trim the idle tail, cover the cut with a punch-in or B-roll, and lay room tone. |
| J2 | Ad 2 · 24.00 · all 6 files | **P0** | Regeneration seam: mid-word at 23.97, then a closed-mouth "reset" smile at 24.00, face position shifted, skin smoother and warmer. About 0.75 s of dead air (23.71–24.46) and no caption (23.93–24.33). The 1.06 punch-in doesn't hide it. | Cut on a word inside the new clip, or cover the seam. |
| J3 | Ad 2 · 41.77 (60 s and formats; 75 s at 44.70) | P1 | Jump cut: an idle tail with eyes closed, then eyes open, mouth open and head about 20 px higher. | Trim the tail or cover the cut. |
| J4 | Ad 3 · 26.5–27.73 · all 6 files | **P0** | Seam between the two AI clips. The face freezes in a closed-mouth smile (about 26.67–27.23), then a dissolve shows a soft, half-blinking double face (27.27–27.40), all inside about 1.1 s of dead air (26.5–27.6). At 27.70→27.73 the mouth snaps from wide open to nearly shut. | Remove the frozen tail, close the gap, and cover the seam or regenerate as one take. |
| J5 | All three 45 s cuts | **P0** | Hard jump cuts inside the take where lines were removed: Ad 1 at 11.27 and 27.73; Ad 2 at 11.67, 16.80 and 28.20 (with one leftover eyes-closed frame of the outgoing clip at 28.17, a visible twitch); Ad 3 at 13.10 (its second edit at 28.77 is hidden by a blink and is fine). They also drop the "28 vs 61" payoff (so "that gap" points at nothing) and the "$100 a month / 6.5 years / single mom" proof. | Cover each cut with B-roll or a stat card ("28 vs 61"), or write a native 45 s script. |
| A1 | 0–34 s in every file | P1 | No music bed under the first 34 s. Pauses fall to digital silence (−55 to −77 dB): about 7 gaps of 0.5–1.15 s per ad, roughly 6 s of dead air in Ad 3's first 32 s. The music then starts cold mid-take (about 34–37 s) and slams in at the sting (Ad 3: bass up about 30 dB at 53.0). | Run a low bed or room tone from frame 0, duck it under the voice, tighten the pauses, and ramp the end. |
| A2 | Ad 1 · talking take | P1 | Frame-rate judder: a 24 fps source padded to 30 fps, so 1 frame in 5 repeats (from 23.1 s), and from 24.03 s two of every five frames repeat (each held 3×, about 18 unique fps) through at least 28.97 s, and again at 33–36 s. Motion jumps 4–7 between holds. Ad 2 and Ad 3 do not have this. | Re-time with optical flow, or deliver at 24/25 fps. |
| A3 | Ad 1 "75" · 66.5–67.4 | P2 | 0.9 s of digital silence while the offer card is still up. | Carry the music to the last frame. |

## Ad 1 · Man 42

A believable kitchen-selfie presenter and a continuous take in the 60 s; lip-sync is fine (about −67 ms). He is let down by judder, ghosting dissolves and a broken 45 s and 16:9.

| File | Time | Priority | Finding | Fix |
| --- | --- | --- | --- | --- |
| 45 s | 11.27 · 27.73 | **P0** | Two head-jump cuts (J5). The first drops the "28 vs 61" payoff; the second drops "$100 a month", "6.5 years" and "single mom". | Cover them, or write a native 45 s script. |
| 16:9 | whole | **P0** | Eyebrows-to-chin crop, upscaled about 2.5× and very soft, strap across the forehead. The swirl lands across his whole face. | Rebuild on a wide or side-panel layout, or don't ship it. |
| all | talking take | P1 | 24→30 fps judder (A2). | Re-time. |
| all | 0.97–1.40, 29.67–32.40, 45.83–50.70, 52.50–53.80 | P1 | Transitions T1, T2–T4, T5–T6, T7–T9. | See the editing table. |
| 9:16 | end card | P1 | SIGN UP NOW is fully visible from 56.67 and the URL from about 57.10, so the full CTA shows for about 2.0 s (about 2 s in the 45). On Reels the CTA (88% of height) and URL (95%) sit under the UI; the strap (14%) and captions (73%) are in UI zones too. | Build the card faster; CTA at 65–75% of height. |
| "75" | file | P1 | 67.4 s, not 75. The same script at about 1.0× speed instead of 1.12×, plus a longer card. Nothing new, and about 3 s of stings before the CTA. | Rename, or add real content (VIP detail, refund, a Julie clip). |
| 60 | 5.8→6.33 · 46.0–50.6 | P2 | The "954 38-YEAR-OLD" caption lands about 0.5 s late. No spoken-word caption at all during the Zoom shot ("for one hour", VIP line). | Retime and add captions. |
| 4:5 · 1:1 | talking | P2 | Head cropped at the hairline with the strap over it; the face is upscaled about 1.4–1.5× and soft. In 1:1 the Zoom dates sit 3% from the bottom edge. | Widen the crop; keep 5–8% margins. |
| all | 29.7–32.2 | **P0** | Mock press cards (the 16:9 shows even more: "budget biohacker mum, 55", "Tech bros spend millions…"). | Real headlines, verbatim. |

Clean: no audio clicks, no clipping (sample peak −2.8 dB), and no jump cut inside the 60 s take.

## Ad 2 · Woman 42

Warm, relatable presenter with good lip-sync (closures on "measure", "Bryan", "month" and "mom" within about 1 frame). The "second half at 1080p" fix made the second half softer, not sharper, and the take now has two visible stitches.

| File | Time | Priority | Finding | Fix |
| --- | --- | --- | --- | --- |
| all 6 | 18.87 | **P0** | Jump cut over dead air (J1). | Cover the cut and lay room tone. |
| all 6 | 24.00 | **P0** | Regeneration seam with an expression reset and 0.75 s of dead air (J2). | Cover it or recut. |
| 60 s + formats, 75 s | 41.77 / 44.70 | P1 | Jump cut, eyes closed → open (J3). | Trim or cover. |
| 45 s | 28.17–28.20 | **P0** | One leftover eyes-closed, closed-mouth frame (28.167) of the outgoing clip just before the jump cut at 28.20: a visible twitch (J5). | End the outgoing clip one frame earlier, and cover the cut. |
| all | 24–46 | P1 | The regenerated half is measurably softer (face sharpness about 30 → about 19): waxy skin, softer hair edges, an "AI" look from the seam onward. | Regenerate or upscale it to match the grain of the first half. |
| all | 24+ | P2 | The voice gets duller at the seam (−6 to −7 dB above 6 kHz; pitch 182 → 178 Hz). | EQ-match the two halves. |
| all | 7.9–8.65 | P1 | She says "New Zealand-ins" while the caption reads "NEW ZEALANDERS". A phone-level ASR pass finds no "-ers" ending. | Re-voice that one word. |
| all | 46.10–50.77 | P1 | About 4.7 s of speech with no caption ("for one hour" plus the VIP line). | Caption it inside the Zoom shot. |
| all | 29.40 · 5.93 · 41.0 | P2 | "IN 2023," appears 0.3 s before the word; "954 38-YEAR-OLD" lands 0.47 s late; "A FULL TIME JOB" is missing its hyphen. | Retime and fix the text. |
| 9:16 | whole | P1 | The strap sits at 12–18% of height (inside the top UI zone), "LIVE ON ZOOM" at about 11%, captions at 71–75%, SIGN UP NOW at 88% and the URL at 95%. The URL and refund show about 2 s before the end. | Move everything into the 15–70% band and hold the full card 3–4 s. |
| 16:9 | whole | **P0** | Crop of the vertical blown up about 2.7×. Top of the head cut off, strap on the forehead, soft and blocky. | Don't run it; rebuild it. |
| 1:1 · 4:5 | whole | P2 | 1:1: the strap overlaps her hair and the logo is clipped on the right. 4:5: the best-composed version; only the eTeacher wordmark margins are tight. | Small layout fixes. |
| "75" | file | P2 | 67.4 s. Speech about 6% slower, longer pauses, longer Zoom shot and card. No new content. | Rename or add content. |
| all | 29.5–32.8 | **P0** | Mock press cards. | Real headlines, verbatim. |

## Ad 3 · Woman 51

The most believable presenter of the three: a real-looking 51-year-old in a real room, with no frame-rate judder. She is let down by one bad seam, a long run of dry, music-less pauses and the same transition ghosts. Speed is 1.14×, not the 1.12× in the brief.

| File | Time | Priority | Finding | Fix |
| --- | --- | --- | --- | --- |
| all 6 | 26.5–27.73 | **P0** | Frozen smile, doubled-face dissolve and about 1.1 s of dead air, then a mouth snap (J4). | Remove the frozen tail and cover or regenerate the seam. |
| 45 s | 13.10 | **P0** | A head-jump cut (J5) that removes the 28-vs-61 proof. The later edit around 28.8 s (dropping "$100 a month / 6.5 years / single mom") is hidden by a blink, but the $2M line now has no $100 payoff. | Cover it, or write a native 45 s script. |
| 9:16 (all 3) | 1.5–32.4 | P1 | About 6.3 s of dead air across 8 pauses in the first 32 s, with no music until about 35–37 s. The end music slams in (+30 dB bass at 53.0) and the end card is 2–3 dB louder than the voice. | Run a low bed from 0 s, tighten the pauses, ramp the end and trim 2 dB. |
| 9:16 | 47–51, 55–59.7 | P1 | "LIVE ON ZOOM" at 8–15% of height, the Zoom dates at 82–90%, and $49 / SIGN UP NOW / URL in the bottom 23%: all under Reels UI. The full card is readable for about 2.0 s (45 s: about 1.9 s). | Move into the 15–70% band and hold 3 s or more. |
| 9:16 60 | 51.6–52.36 · 18.8 | P2 | The "$49." caption shows for under 0.5 s while "dollars" is still being spoken. "SAME BIRTH YEAR?" has the wrong punctuation. The VIP line has no caption. | Extend, fix and add. |
| 16:9 | whole · 49.5–51 | **P0** | Centre crop upscaled about 1.8× and soft; forehead and chin cut; strap on the forehead and caption on the chin. The "or NOV 14 · 1 PM ET" line sits on the bottom edge with no safe margin. | Rebuild. |
| 16:9 | 47–51 | P2 | Zoom participant names are AI gibberish ("Elxirah D.", "Fmnsh R.", "Naysso T."), and "Julie Gibson Clark · Host" appears twice. | Blur the names and keep one label. |
| 1:1 | talking | P2 | Top of the head cut, strap across her hair, captions at 87% over her chest. | Pull back the framing. |
| "75" | file | P1 | 71.7 s. The 60 s edit at 1.0× voice plus about 7.7 s of end card. Padded, not richer. | Drop it or add content. |
| qc.json | 4:5 / 1:1 / 16:9 | info | The transcripts claim a trailing "Thank you for watching". It is not in any of the six files: after "I'm in" there is only music. The claim is wrong, but the audio is fine. | Correct the qc notes. |
| all | 32.4–35.1 | **P0** | Mock press cards, including 3–4 different blonde women presented as Julie, none matching the Zoom-tile Julie. | Real coverage, verbatim. |

Loudness measured: 9:16 60 s −14.6, 45 s −14.2, 75 s −14.4, 4:5 −14.5 LUFS. The 4:5, 1:1 and 16:9 audio tracks are bit-identical.

## Scores per metric (1–10)

The 4:5 versions score best. All three 16:9 files fail on format. Editing is the weakest metric across the set.

| File | Hook | Script | Claims | Captions | Talent / AI look | Lip-sync & audio | Editing & pacing | Offer / CTA | Format & safe area | Technical | **Overall** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Ad 1 · 9:16 60 | 4 | 7 | 3 | 6 | 6 | 5 | 5 | 6 | 5 | 5 | **5** |
| Ad 1 · 9:16 45 | 4 | 5 | 3 | 6 | 4 | 5 | 4 | 5 | 5 | 4 | **4** |
| Ad 1 · 9:16 "75" (67 s) | 4 | 7 | 3 | 6 | 6 | 5 | 4 | 6 | 5 | 5 | **4** |
| Ad 1 · 4:5 | 4 | 7 | 3 | 6 | 5 | 5 | 5 | 7 | 6 | 5 | **5** |
| Ad 1 · 1:1 | 4 | 7 | 3 | 6 | 5 | 5 | 5 | 7 | 5 | 5 | **5** |
| Ad 1 · 16:9 | 3 | 7 | 3 | 6 | 2 | 5 | 5 | 7 | 2 | 4 | **3** |
| Ad 2 · 9:16 60 | 5 | 7 | 4 | 6 | 5 | 6 | 5 | 6 | 6 | 5 | **5** |
| Ad 2 · 9:16 45 | 5 | 5 | 4 | 6 | 5 | 6 | 4 | 6 | 6 | 4 | **5** |
| Ad 2 · 9:16 "75" (67 s) | 5 | 7 | 4 | 6 | 5 | 6 | 5 | 7 | 6 | 5 | **5** |
| Ad 2 · 4:5 | 5 | 7 | 4 | 7 | 5 | 6 | 5 | 6 | 7 | 5 | **6** |
| Ad 2 · 1:1 | 5 | 7 | 4 | 7 | 5 | 6 | 5 | 6 | 6 | 5 | **5** |
| Ad 2 · 16:9 | 4 | 7 | 4 | 6 | 3 | 6 | 5 | 6 | 2 | 3 | **3** |
| Ad 3 · 9:16 60 | 5 | 7 | 4 | 6 | 7 | 5 | 5 | 6 | 5 | 5 | **5.5** |
| Ad 3 · 9:16 45 | 5 | 5 | 4 | 6 | 6 | 5 | 5 | 6 | 5 | 4 | **5** |
| Ad 3 · 9:16 "75" (72 s) | 5 | 7 | 4 | 6 | 7 | 5 | 3 | 6 | 5 | 5 | **4.5** |
| Ad 3 · 4:5 | 5 | 7 | 4 | 6 | 7 | 5 | 5 | 6 | 7 | 5 | **5.5** |
| Ad 3 · 1:1 | 5 | 7 | 4 | 6 | 7 | 5 | 5 | 6 | 5 | 5 | **5** |
| Ad 3 · 16:9 | 4 | 7 | 4 | 5 | 6 | 5 | 5 | 6 | 3 | 4 | **4** |

With the P0 fixes and the transition rebuild (T6–T9, A1), the 9:16 and 4:5 files should reach about 7.5–8. Ad 3 has the highest ceiling because its talent reads most real.

## Viewer's eye and editor checklist

**Watched as a person scrolling with sound on.** In every file the first 1.4 s is a silent logo, which is enough to lose a thumb. Once the presenter says "33 years apart", the hook works and all three people read as believable. Ad 3 is the most natural, Ad 1 is close, and Ad 2 goes waxy after 24 s.

The first half then feels dry: no music, and pauses that drop to dead silence. In Ad 2 and Ad 3, the seams (a head pop, a frozen smile, a reset expression) make it feel stitched together.

The second half gets busy. Faces melt into press cards, into Julie and into a chrome blob over the mouth. Then a white-to-black flash, and a CTA that finishes building just as the video ends, under the Reels buttons.

The 45 s cuts lose the "28 vs 61" and "$100 a month" proof that make the story land, and they jump. The "75 s" cuts are the same ad told slower. The 16:9 cuts look like a zoomed-in phone video. The 4:5 cuts look the most finished.

**P0 — before launch**

- [ ] Replace the press-card collage in all 18 files with real headlines, verbatim from the site's press section
- [ ] Ad 2: cover or recut the jump cut at 18.87 and the seam at 24.00, and lay room tone under both
- [ ] Ad 3: remove the frozen smile and doubled-face dissolve at 26.5–27.7, and close the dead air
- [ ] 45 s cuts: cover the jump cuts (Ad 1 11.27 and 27.73 · Ad 2 11.67, 16.80, 28.20 plus the leftover frame at 28.17 · Ad 3 13.10), or write a native 45 s script that keeps "28 vs 61"
- [ ] 16:9: don't ship until it's rebuilt as a wide or side-panel layout

**P1 — before paid spend**

- [ ] Replace the ghosting dissolves (T2–T7) with motivated hard cuts or 2–3 frame dissolves; never dissolve a face into a face
- [ ] Native 9:16 swirl sting, or drop the sting; add a dip on the white→black cut (T8, T9)
- [ ] Open on the face and voice at frame 0 (T1)
- [ ] Run a music or room-tone bed from frame 0, tighten the pauses and ramp the end (A1)
- [ ] Ad 1: fix the 24→30 fps judder (A2)
- [ ] Caption "for one hour" and the VIP line inside the Zoom shot
- [ ] End card: build it in under 1 s and hold the full CTA at least 3 s; CTA and URL inside 15–70% of height on 9:16
- [ ] Move the strap and "LIVE ON ZOOM" below the top 15% on 9:16
- [ ] Ad 2: re-voice "New Zealand-ins"; match the sharpness and voice EQ of the second half
- [ ] "75 s": rename to the real length (67 / 67 / 72 s), or add real content

**P2 — polish**

- [ ] Caption timing ("954 38-YEAR-OLD" 0.5 s late, "IN 2023," 0.3 s early, "$49." under 0.5 s), plus "FULL-TIME" and "SAME BIRTH YEAR."
- [ ] 4:5 and 1:1: widen the crop so the head and hair aren't cut, and keep 5–8% margins on the eTeacher wordmark and Zoom dates
- [ ] "SIGN UP NOW" → "Enroll now" to match the site; check the "Est. 2000" on the LLA logo
- [ ] Blur the gibberish Zoom tile names and keep one "Host" label
- [ ] Correct the qc.json claims (the 5 s CTA, "face framed", "Thank you for watching", the 75 s naming)
