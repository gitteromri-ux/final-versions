# Bug found in master assemble.py (ugc-prod) — keyword highlight never renders
`txt = " ".join(parts).upper()` uppercases the ASS override tags, turning `{\c&H66D6FF&}` into `{\C&H66D6FF&}`.
libass ignores `\C`, so the yellow keyword highlight has NOT been rendering in any 9x16 output (verified on a
frame of ad1: "$49." is white; captions.ass in ugc-prod/build/ad1-man42 contains `\C&H` 19x).
Same ordering issue means the "38 YEAR OLD"->"38-YEAR-OLD" replacement can never match (tags sit between the words).
Fix used in ugc-prod-fmt/assemble.py: upper() + replacements on plain text first, then wrap KEY words in `{\c...}` tags.
