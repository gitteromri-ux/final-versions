# v10 — response to `UGC-FINAL-VERSIONS-AUDIT.md` (Claude, 2026-10-01)

Everything below is VERIFIED from this session's own output (frame tiles in `audit_frames/v10/`, `videos/*.qc.json` = ffprobe + ebur128 + faster-whisper small.en re-transcription + caption/onset alignment). Nothing is claimed from memory.

## Pipeline changes (ugc-prod/assemble.py v10, 24 fps)

| # | Audit finding | Fix | Proof |
|---|---|---|---|
| P0 | Mock press-card collage | Replaced by `render_press.py`: three real, verbatim headlines (Fortune 2023-11-04, Business Insider 2023-11-06, Daily Mail 2025-03-27), outlet + date as text, no photos. Sources with URLs in `PRESS-SOURCES.md`. | tiles row "IN THE PRESS" |
| P0 | Ad 2 jump cut 18.87 s + regeneration seam 24.00 s over dead air | Dead air removed (source 18.33–18.68, 23.98–24.30, 42.27–42.56) and each seam covered by a motivated full-frame card: 28-vs-61 stat card, title card, founding-faculty card. Edit = select/atrim on the re-encoded 24 fps source (53.06 s video / 52.97 s audio, 1272 frames). | `audit_frames/v10/ad2-woman42__seams.jpg` |
| P0 | Ad 3 frozen smile / doubled face / 1.1 s dead air at 26.5–27.7 | Source 29.12–30.08 removed, covered by the title card. | tile ad3 |
| P0 | 45 s cuts: hard jump cuts, lose "28 vs 61" and "$100/month" | Sentence A and B removed in silences; the proof is carried by the 28-vs-61 card and a "$100 a month vs $2M a year" card at exactly those points. | tiles `*__9x16__45.tile.jpg` |
| P0 | 16:9 = blown-up crops | Not shipped. Removed from the site and the matrix. | site |
| P1 | Ghosting dissolves (T2–T7) | All alpha fades removed: press, Zoom, inserts and main→closer are hard cuts; closer→offer is a 0.25 s dip to black. | tiles |
| P1 | Swirl 16:9 inside 9:16 with blurred fill (T8) | Closer is the orb shot only (film 128.6–130.0), centre-cropped to native 9:16, 1.4 s. | tile last row |
| P1 | White→black flash swirl→"by eTeacher" (T9) | "by eTeacher" card dropped; dip-to-black into the offer card. | tile |
| P1 | Silent 0.9 s logo opener (T1) | Removed. Frame 0 = face + voice. | tile frame 0, qc offset 0 |
| P1 | No music under first 34 s, slams at the sting | Music bed from 0 s at −21 dB rising to −13 dB over 3 s into the Zoom shot, carried to the last frame (1.2 s fade). | ebur128 in qc.json |
| P1 | Ad 1 24→30 fps judder | All sources rebuilt at native 24 fps; ads rendered at 24 fps. mpdecimate on Ad 1 20–35 s: 350/360 frames unique (1-in-5 duplication would give 288). | qc.json `video: … 24/1` |
| P1 | No speech captions inside the Zoom shot | Captions continue (style CapZ) in a free band; Zoom composition scaled 0.86 so tiles, dates and captions never overlap. | tile |
| P1 | End card builds too slowly, CTA/URL under Reels UI | Offer card: all elements in by 0.85 s, CTA button centred at 75 % height, URL at 81 %, held ≥ 4 s. | tile |
| P1 | Strap at 12–18 %, "LIVE ON ZOOM" at 8–15 % | Strap MarginV 300 (≥ 15.6 %), "LIVE ON ZOOM" at 18 %. | tile |
| P1 | Strap over graphics | Strap hidden during press cards, insert cards and the Zoom shot. | tile |
| P1 | "75 s" files are 67/67/72 s | No 75 s exists: the takes contain 54–59 s of speech. Not shipped; matrix row removed. |  |
| P2 | "A FULL TIME JOB" hyphen, "SAME BIRTH YEAR?" | Replacements added (FULL-TIME; "year."). | captions.ass |
| P2 | qc.json wrong claims | Regenerated per file by `qc.py` from the delivered MP4. | videos/*.qc.json |

## Residual (honest list)

- One caption ("JULIE GIBSON CLARK") lands ~0.5 s off the whisper onset in Ad 1 (early) and Ad 2 (late); all other captions ≤ 0.4 s.
- "$49." caption is on screen 0.33 s (it is a one-word utterance).
- Ad 2 "New Zealand-ins" pronunciation and the softer second half are in the generated performance; fixing them needs a Higgsfield regeneration (not done — would cost credits and was not approved).
- 4:5 and 1:1 crop the 9:16 graphics to their safe band (dates are shown on the offer card, not on the Zoom shot, in those formats).
- Claude's second file (`JULIE-FILM-V4-AUDIT.md`, the film) is not addressed in this round.

## Numbers (from qc.json)

| File | Length | LUFS | TP | Captions matched |
|---|---|---|---|---|
| ad1-man42__9x16__60 | 58.1 s | −14.3 | −2.9 | 57/58 |
| ad2-woman42__9x16__60 | 57.2 s | −14.0 | −2.9 | 54/54 |
| ad3-woman51__9x16__60 | 57.9 s | −14.6 | −2.8 | 58/59 |
| ad1-man42__9x16__45 | 43.4 s | −14.3 | −2.8 | 40/40 |
| ad2-woman42__9x16__45 | 43.9 s | −14.0 | −2.7 | 38/39 |
| ad3-woman51__9x16__45 | 42.8 s | −14.4 | −2.8 | 40/41 |

("Unmatched" items are the strap text being picked up by the matcher, not speech captions.)
