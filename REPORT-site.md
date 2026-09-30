# REPORT-site (FINAL VERSIONS delivery page)
- Live: https://gitteromri-ux.github.io/final-versions/  (repo https://github.com/gitteromri-ux/final-versions, Pages from main /)
- HEAD: baa0424
- Re-deploy any time new mp4/qc.json land: `/home/user/workspace/final-versions/deploy.sh` (build → add -A → commit → push, rebase on reject). Must run with GitHub credentials (api_credentials=["github"]).
- build_site.py: idempotent; posters via ffmpeg @1.0 s (only when missing/stale); prunes pages of removed videos; warns on >95 MB; writes manifest.json.
- VERIFIED: index, video page, poster, mp4 all HTTP 200; mp4 Content-Length 35881777 == local size. Desktop (1920) + 390 px mobile screenshots checked: no horizontal overflow; "Tap to play with sound" overlay appears when autoplay-with-sound is blocked.
- NOT done: only 1/36 videos present at time of writing; other 35 cells show "rendering…" until files arrive.
