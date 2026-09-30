#!/usr/bin/env python3
"""FINAL VERSIONS delivery site generator (idempotent).

Scans videos/<slug>__<fmt>__<dur>.mp4 (+ optional .qc.json sidecar), renders posters/<name>.jpg
(ffmpeg frame at 1.0 s, only if missing/stale), writes index.html and one <name>.html per video.
"""
import glob, html, json, os, re, subprocess, datetime

ROOT = os.path.dirname(os.path.abspath(__file__))
VID = os.path.join(ROOT, "videos")
POS = os.path.join(ROOT, "posters")
os.makedirs(POS, exist_ok=True)

TITLE = "Julie Masterclass UGC Ads · FINAL VERSIONS"
ADS = [("ad1-man42", "Ad 1 · 42M", "Man, 42 · one continuous UGC take"),
       ("ad2-woman42", "Ad 2 · 42F", "Woman, 42 · punch-in at 24 s"),
       ("ad3-woman51", "Ad 3 · 51F", "Woman, 51")]
DURS = ["45", "60", "75"]
FMTS = [("9x16", "9:16", "1080×1920", 9/16), ("4x5", "4:5", "1080×1350", 4/5),
        ("1x1", "1:1", "1080×1080", 1.0), ("16x9", "16:9", "1920×1080", 16/9)]
FMT_MAP = {f[0]: f for f in FMTS}
AD_MAP = {a[0]: a for a in ADS}
NAME_RE = re.compile(r"^(?P<slug>[a-z0-9-]+)__(?P<fmt>\d+x\d+)__(?P<dur>\d+)$")

PRODUCT = [
    ("Product", "The Longevity Masterclass of the Year with Julie Gibson Clark · Longevity Life Academy (by eTeacher Group)"),
    ("Format", "Live on Zoom · 60 min"),
    ("Dates", "Tue Oct 27 2026 · 7 PM ET  or  Sat Nov 14 2026 · 1 PM ET"),
    ("Price", "$49 · VIP $79 (+30-min private Q&A, $249 credit toward the Longevity Blueprint course)"),
    ("Guarantee", "14-day refund"),
    ("Julie", "#2 slowest-aging person on Earth 2023 (Rejuvenation Olympics), ahead of Bryan Johnson ($2M/yr); ~$100/month; ages ~6.5 yrs per decade; single mom, full-time job; founding faculty at LLA"),
    ("Landing page", '<a href="https://www.longevitylifeacademy.com/julie-masterclass/" target="_blank" rel="noopener">longevitylifeacademy.com/julie-masterclass</a>'),
]
SPEC = "H.264 High · yuv420p · 30 fps · CRF ≤ 18 · AAC 192k 48 kHz stereo · +faststart · −14 LUFS ±1 · true peak ≤ −1.5 dBTP"

CSS = r"""
:root{--navy:#050A1F;--navy2:#0B1538;--ink:#F5F7FF;--mute:#9AA6C8;--line:rgba(255,255,255,.09);--gold:#E8B84A;--gold2:#FFD98A;--ok:#5BE3A6;--warn:#FFB35C}
*{box-sizing:border-box}html{scroll-behavior:smooth}
body{margin:0;background:var(--navy);background-image:radial-gradient(900px 600px at 80% -10%,rgba(232,184,74,.14),transparent 60%),radial-gradient(1000px 700px at -10% 10%,rgba(60,90,200,.25),transparent 60%);color:var(--ink);font-family:Inter,ui-sans-serif,system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;-webkit-font-smoothing:antialiased;min-height:100vh}
a{color:inherit;text-decoration:none}
.wrap{max-width:1240px;margin:0 auto;padding:22px 18px 90px}
.top{display:flex;align-items:center;justify-content:space-between;gap:14px;padding:6px 0 26px;border-bottom:1px solid var(--line)}
.brand{display:flex;align-items:center;gap:12px;font-weight:800;letter-spacing:.02em}
.brand .mark{width:34px;height:34px;border-radius:10px;background:linear-gradient(135deg,var(--gold),#b4841f);display:grid;place-items:center;color:#1a1400;font-weight:900;font-size:13px}
.brand small{display:block;font-weight:600;color:var(--mute);font-size:11px;letter-spacing:.18em;text-transform:uppercase}
.stamp{font-size:11px;letter-spacing:.2em;text-transform:uppercase;color:var(--gold);border:1px solid rgba(232,184,74,.4);padding:7px 12px;border-radius:999px;font-weight:800;white-space:nowrap}
.hero{padding:38px 0 18px}
.hero h1{margin:0;font-size:clamp(30px,5.2vw,58px);font-weight:900;line-height:1;letter-spacing:-.03em}
.hero h1 em{font-style:normal;color:var(--gold);}
.hero p{color:var(--mute);max-width:640px;font-size:15px;line-height:1.6;margin:16px 0 0}
.stats{display:flex;gap:10px;flex-wrap:wrap;margin:22px 0 6px}
.stat{background:rgba(255,255,255,.04);border:1px solid var(--line);border-radius:14px;padding:10px 14px;font-size:13px;color:var(--mute)}
.stat b{color:var(--ink);font-weight:800;font-size:15px;margin-right:6px}
.legend{display:flex;gap:16px;flex-wrap:wrap;font-size:12px;color:var(--mute);margin:12px 0 0}
.legend i{display:inline-block;width:8px;height:8px;border-radius:50%;margin-right:6px;vertical-align:middle}
.ad{margin-top:44px}
.adhead{display:flex;align-items:baseline;justify-content:space-between;gap:12px;flex-wrap:wrap;margin-bottom:14px}
.adhead h2{margin:0;font-size:26px;font-weight:900;letter-spacing:-.02em}
.adhead h2 span{color:var(--gold)}
.adhead p{margin:0;color:var(--mute);font-size:13px}
.matrix{display:grid;gap:14px;grid-template-columns:1fr}
.durrow{background:linear-gradient(180deg,rgba(255,255,255,.045),rgba(255,255,255,.015));border:1px solid var(--line);border-radius:22px;padding:14px}
.durlabel{display:flex;align-items:center;gap:10px;margin:2px 4px 12px;font-size:12px;letter-spacing:.16em;text-transform:uppercase;color:var(--mute);font-weight:800}
.durlabel b{color:var(--ink);font-size:22px;letter-spacing:-.02em;font-weight:900}
.cells{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:10px;align-items:start}
.cell{position:relative;border-radius:16px;background:rgba(5,10,31,.6);border:1px solid var(--line);padding:12px;display:flex;flex-direction:column;gap:8px;min-height:150px;transition:border-color .2s,transform .2s}
.cell.ok:hover{border-color:rgba(232,184,74,.55);transform:translateY(-2px)}
.cell .fmt{display:flex;justify-content:space-between;align-items:center;font-size:12px;letter-spacing:.12em;text-transform:uppercase;font-weight:800;color:var(--gold2)}
.cell .fmt small{color:var(--mute);letter-spacing:0;text-transform:none;font-weight:600}
.thumb{display:block;border-radius:10px;overflow:hidden;background:#000;border:1px solid rgba(255,255,255,.06);position:relative}
.thumb img{width:100%;height:100%;object-fit:cover;display:block}
.thumb .pl{position:absolute;inset:0;display:grid;place-items:center;opacity:.9}
.thumb .pl i{width:38px;height:38px;border-radius:50%;background:rgba(255,255,255,.95);display:grid;place-items:center}
.thumb .pl i:after{content:"";border-left:12px solid #0a1440;border-top:7px solid transparent;border-bottom:7px solid transparent;margin-left:3px}
.facts{display:grid;grid-template-columns:1fr 1fr 1fr;gap:6px;font-size:12px;color:var(--mute)}
.facts div b{display:block;color:var(--ink);font-weight:800;font-size:12.5px;white-space:nowrap}
.facts .lufs.good b{color:var(--ok)}.facts .lufs.bad b{color:var(--warn)}
.acts{display:flex;gap:6px;margin-top:auto}
.btn{flex:1;display:inline-flex;align-items:center;justify-content:center;gap:6px;padding:10px 10px;border-radius:10px;font-weight:800;font-size:13px;border:1px solid transparent;cursor:pointer;min-height:40px}
.btn.p{background:var(--gold);color:#1a1400}.btn.p:hover{background:var(--gold2)}
.btn.s{background:rgba(255,255,255,.06);color:var(--ink);border-color:rgba(255,255,255,.14)}.btn.s:hover{border-color:rgba(255,255,255,.4)}
.cell.pending{border-style:dashed;justify-content:center;align-items:center;color:var(--mute);font-size:12px;text-align:center;gap:6px}
.cell.pending .fmt{width:100%;color:var(--mute)}
.pulse{width:8px;height:8px;border-radius:50%;background:var(--warn);animation:pulse 1.6s infinite}
@keyframes pulse{0%,100%{opacity:.3}50%{opacity:1}}
.foot{margin-top:56px;padding-top:22px;border-top:1px solid var(--line);color:var(--mute);font-size:12px;line-height:1.7}
.foot b{color:var(--ink)}
/* single */
.player{display:grid;grid-template-columns:minmax(0,1fr);min-width:0;gap:26px;margin-top:26px;align-items:start}
.stage{position:relative;min-width:0;max-width:100%;border-radius:22px;overflow:hidden;background:#000;border:1px solid rgba(255,255,255,.12);box-shadow:0 40px 110px rgba(0,0,0,.65);margin:0 auto;width:100%}
.stage video{width:100%;height:100%;display:block;object-fit:contain;background:#000}
.tap{position:absolute;inset:0;display:none;place-items:center;background:rgba(5,10,31,.55);backdrop-filter:blur(3px);cursor:pointer;border:0;color:var(--ink);font:inherit}
.tap.show{display:grid}
.tap span{display:flex;flex-direction:column;align-items:center;gap:14px;font-weight:900;font-size:clamp(18px,4.5vw,26px);letter-spacing:-.01em;text-align:center;padding:20px}
.tap span i{width:86px;height:86px;border-radius:50%;background:var(--gold);display:grid;place-items:center;box-shadow:0 20px 60px rgba(232,184,74,.4)}
.tap span i:after{content:"";border-left:30px solid #1a1400;border-top:18px solid transparent;border-bottom:18px solid transparent;margin-left:8px}
.side{min-width:0}.side h2{margin:0;font-size:clamp(24px,4vw,36px);font-weight:900;letter-spacing:-.02em}
.side h2 span{color:var(--gold)}
.side .fname{font-family:ui-monospace,SFMono-Regular,Menlo,monospace;font-size:12px;color:var(--mute);margin:8px 0 18px;word-break:break-all}
.kv{display:grid;grid-template-columns:120px 1fr;gap:9px 14px;font-size:14px;line-height:1.45}
.kv div:nth-child(odd){color:var(--mute);font-size:12px;letter-spacing:.08em;text-transform:uppercase;font-weight:700;padding-top:2px}
.kv div:nth-child(even){color:var(--ink)}
.kv a{color:var(--gold2);text-decoration:underline}
.box{margin-top:22px;padding:18px;border-radius:18px;background:rgba(255,255,255,.04);border:1px solid var(--line)}
.box h3{margin:0 0 12px;font-size:12px;letter-spacing:.18em;text-transform:uppercase;color:var(--gold);font-weight:800}
.script{white-space:pre-wrap;font-size:14px;line-height:1.65;color:#D9E0F5}
.acts.big .btn{flex:0 1 auto;padding:14px 22px;font-size:15px;border-radius:12px}
.badge{display:inline-block;font-size:11px;padding:3px 9px;border-radius:999px;border:1px solid var(--line);color:var(--mute);margin-left:6px;vertical-align:middle;font-weight:700}
.badge.ok{color:var(--ok);border-color:rgba(91,227,166,.4)}.badge.bad{color:var(--warn);border-color:rgba(255,179,92,.4)}
@media(min-width:720px){.cells{grid-template-columns:repeat(4,1fr)}.matrix{gap:14px}}
@media(min-width:900px){.player{grid-template-columns:minmax(300px,var(--stagew,420px)) 1fr;gap:40px}.player .stage{margin:0}.wrap{padding:28px 28px 100px}}
"""


def sh(*cmd):
    return subprocess.run(cmd, capture_output=True, text=True)


def probe(path):
    r = sh("ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries",
           "stream=width,height,r_frame_rate:format=duration,size", "-of", "json", path)
    try:
        j = json.loads(r.stdout)
        st = (j.get("streams") or [{}])[0]
        f = j.get("format", {})
        return {"w": st.get("width"), "h": st.get("height"), "fps": st.get("r_frame_rate"),
                "duration": float(f.get("duration", 0) or 0), "size": int(f.get("size", 0) or 0)}
    except Exception:
        return {"w": None, "h": None, "fps": None, "duration": 0.0, "size": os.path.getsize(path)}


def poster(mp4, name):
    out = os.path.join(POS, name + ".jpg")
    if os.path.exists(out) and os.path.getmtime(out) >= os.path.getmtime(mp4) and os.path.getsize(out) > 0:
        return out
    sh("ffmpeg", "-y", "-v", "error", "-threads", "1", "-ss", "1.0", "-i", mp4, "-frames:v", "1",
       "-vf", "scale='min(720,iw)':-2", "-q:v", "3", out)
    return out if os.path.exists(out) else None


def fmt_size(n):
    return f"{n/1_048_576:.1f} MB" if n else "—"


def scan():
    items = {}
    for mp4 in sorted(glob.glob(os.path.join(VID, "*.mp4"))):
        name = os.path.basename(mp4)[:-4]
        m = NAME_RE.match(name)
        if not m or m["slug"] not in AD_MAP or m["fmt"] not in FMT_MAP:
            print("skip (bad name):", name)
            continue
        qc = {}
        qp = os.path.join(VID, name + ".qc.json")
        if os.path.exists(qp):
            try:
                qc = json.load(open(qp))
            except Exception as e:
                qc = {"notes": f"qc.json unreadable: {e}"}
        p = probe(mp4)
        items[(m["slug"], m["dur"], m["fmt"])] = {
            "name": name, "file": os.path.basename(mp4), "slug": m["slug"], "dur": m["dur"], "fmt": m["fmt"],
            "probe": p, "qc": qc, "poster": poster(mp4, name),
        }
    return items


def lufs_of(it):
    v = it["qc"].get("lufs")
    try:
        v = float(v)
    except (TypeError, ValueError):
        return None, ""
    return v, ("good" if abs(v + 14) <= 1 else "bad")


def tp_of(it):
    v = it["qc"].get("true_peak")
    try:
        v = float(v)
    except (TypeError, ValueError):
        return None, ""
    return v, ("good" if v <= -1.5 else "bad")


def e(s):
    return html.escape(str(s), quote=True)


def head(title):
    return f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{e(title)}</title><meta name="robots" content="noindex,nofollow"><meta name="theme-color" content="#050A1F">
<link rel="preconnect" href="https://rsms.me/"><link rel="stylesheet" href="https://rsms.me/inter/inter.css">
<style>{CSS}</style></head><body><div class="wrap">"""


def topbar():
    return """<div class="top"><a class="brand" href="index.html"><span class="mark">LLA</span><span>Julie Masterclass · UGC Ads<small>Longevity Life Academy</small></span></a><span class="stamp">Final versions</span></div>"""


def cell(it, fmt):
    key, label, res, ratio = fmt
    if not it:
        return f"""<div class="cell pending"><div class="fmt"><span>{label}</span><small>{res}</small></div><span class="pulse"></span>rendering…</div>"""
    p, dur = it["probe"], it["probe"]["duration"]
    lufs, cls = lufs_of(it)
    lufs_txt = f"{lufs:.1f}" if lufs is not None else "—"
    return f"""<div class="cell ok"><div class="fmt"><span>{label}</span><small>{res}</small></div>
<a class="thumb" href="{e(it['name'])}.html" style="aspect-ratio:{ratio:.4f}"><img src="posters/{e(it['name'])}.jpg" alt="" loading="lazy"><span class="pl"><i></i></span></a>
<div class="facts"><div>Length<b>{dur:.1f} s</b></div><div>Size<b>{fmt_size(p['size'])}</b></div><div class="lufs {cls}">LUFS<b>{lufs_txt}</b></div></div>
<div class="acts"><a class="btn p" href="videos/{e(it['file'])}" download>Download</a><a class="btn s" href="{e(it['name'])}.html">Open</a></div></div>"""


def index(items):
    total = len(items)
    sizes = sum(i["probe"]["size"] for i in items.values())
    blocks = []
    for slug, title, desc in ADS:
        n = sum(1 for k in items if k[0] == slug)
        rows = []
        for d in DURS:
            cells = "".join(cell(items.get((slug, d, f[0])), f) for f in FMTS)
            rows.append(f"""<div class="durrow"><div class="durlabel"><b>{d}s</b><span>· 4 formats</span></div><div class="cells">{cells}</div></div>""")
        blocks.append(f"""<section class="ad" id="{slug}"><div class="adhead"><h2>{e(title.split(' · ')[0])} <span>· {e(title.split(' · ')[1])}</span></h2><p>{e(desc)} · {n}/12 delivered</p></div><div class="matrix">{''.join(rows)}</div></section>""")
    state = f"<b>{total}</b>/36 files live" if total else "<b>0</b>/36 · rendering"
    now = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    body = f"""{topbar()}
<div class="hero"><h1>Julie Masterclass UGC Ads<br><em>FINAL VERSIONS</em></h1>
<p>Three talking-head ads · three lengths · four formats. Every cell is a finished Meta-ready MP4 with burned-in captions, film opener, PR pop-up, Zoom B-roll and the offer closer. Tap a thumbnail to play with sound, or download directly.</p>
<div class="stats"><div class="stat">{state}</div><div class="stat"><b>{fmt_size(sizes)}</b>total</div><div class="stat"><b>3</b>ads</div><div class="stat"><b>45 · 60 · 75</b>s</div><div class="stat"><b>9:16 · 4:5 · 1:1 · 16:9</b></div></div>
<div class="legend"><span><i style="background:var(--ok)"></i>LUFS within −14 ±1</span><span><i style="background:var(--warn)"></i>LUFS outside target / rendering</span><span>Updated {now}</span></div></div>
{''.join(blocks)}
<div class="foot"><b>Spec:</b> {SPEC}<br><b>Offer facts (VERIFIED 2026-09-29):</b> Live on Zoom, 60 min · Tue Oct 27 2026 7 PM ET or Sat Nov 14 2026 1 PM ET · $49 · VIP $79 (+30-min private Q&amp;A, $249 Blueprint credit) · 14-day refund · <a href="https://www.longevitylifeacademy.com/julie-masterclass/" style="color:var(--gold2)">longevitylifeacademy.com/julie-masterclass</a></div>
</div></body></html>"""
    with open(os.path.join(ROOT, "index.html"), "w") as f:
        f.write(head(TITLE) + body)


def single(it):
    key, label, res, ratio = FMT_MAP[it["fmt"]]
    slug, adtitle, desc = AD_MAP[it["slug"]]
    p, qc = it["probe"], it["qc"]
    lufs, lc = lufs_of(it)
    tp, tc = tp_of(it)
    stagew = "420px" if ratio < 1 else ("520px" if ratio == 1 else "760px")
    kv = [("Ad", f"{adtitle} — {desc}"), ("Target", f"{it['dur']} s · {label} ({res})"),
          ("Measured", f"{p['duration']:.2f} s · {p['w']}×{p['h']} · {p['fps'] or '?'} fps · {fmt_size(p['size'])}"),
          ("Loudness", (f"{lufs:.1f} LUFS" if lufs is not None else "—") + f'<span class="badge {lc}">{"target −14 ±1" if lc else "no qc.json"}</span>'),
          ("True peak", (f"{tp:.1f} dBTP" if tp is not None else "—") + (f'<span class="badge {tc}">≤ −1.5</span>' if tc else "")),
          ("Language", e(qc.get("lang", "—"))),
          ("Captions", e(str(qc.get("captions_matched", "—")))),
          ("Verified by", e(qc.get("verified_by", "—"))),
          ("Notes", e(qc.get("notes", "—")))]
    kvh = "".join(f"<div>{k}</div><div>{v}</div>" for k, v in kv)
    prod = "".join(f"<div>{k}</div><div>{v}</div>" for k, v in PRODUCT)
    tr = qc.get("transcript")
    tr_html = f'<div class="box"><h3>Transcript (whisper)</h3><div class="script">{e(tr)}</div></div>' if tr else ""
    body = f"""{topbar()}
<div class="player" style="--stagew:{stagew}">
<div class="stage" style="aspect-ratio:{ratio:.4f};max-width:{stagew}"><video id="v" src="videos/{e(it['file'])}" poster="posters/{e(it['name'])}.jpg" autoplay playsinline controls preload="auto"></video>
<button class="tap" id="tap" aria-label="Tap to play with sound"><span><i></i>Tap to play with sound</span></button></div>
<div class="side"><h2>{e(adtitle.split(' · ')[0])} <span>· {e(adtitle.split(' · ')[1])}</span> · {it['dur']}s · {label}</h2>
<div class="fname">{e(it['file'])}</div>
<div class="acts big"><a class="btn p" href="videos/{e(it['file'])}" download>Download MP4</a><a class="btn s" href="videos/{e(it['file'])}" target="_blank" rel="noopener">Open raw file</a><a class="btn s" href="index.html">All versions</a></div>
<div class="box"><h3>QC facts</h3><div class="kv">{kvh}</div></div>
<div class="box"><h3>Product facts (VERIFIED 2026-09-29)</h3><div class="kv">{prod}</div></div>
{tr_html}
<div class="foot"><b>Spec:</b> {SPEC}</div></div></div>
<script>
const v=document.getElementById('v'),t=document.getElementById('tap');
v.muted=false;v.volume=1;
function attempt(){{const p=v.play();if(p&&p.catch)p.catch(()=>{{t.classList.add('show');}});}}
attempt();
setTimeout(()=>{{if(v.paused||v.muted)t.classList.add('show');}},900);
t.addEventListener('click',()=>{{v.muted=false;v.volume=1;v.currentTime=0;v.play();t.classList.remove('show');}});
v.addEventListener('play',()=>{{if(!v.muted)t.classList.remove('show');}});
v.addEventListener('volumechange',()=>{{if(!v.muted&&!v.paused)t.classList.remove('show');}});
</script>
</div></body></html>"""
    with open(os.path.join(ROOT, it["name"] + ".html"), "w") as f:
        f.write(head(f"{adtitle} · {it['dur']}s · {label} · FINAL") + body)


def main():
    items = scan()
    index(items)
    for it in items.values():
        single(it)
    # prune pages/posters for videos that disappeared
    live = {it["name"] for it in items.values()}
    for p in glob.glob(os.path.join(ROOT, "*__*__*.html")):
        if os.path.basename(p)[:-5] not in live:
            os.remove(p)
    for p in glob.glob(os.path.join(POS, "*.jpg")):
        if os.path.basename(p)[:-4] not in live:
            os.remove(p)
    manifest = [{"file": it["file"], "slug": it["slug"], "fmt": it["fmt"], "dur": it["dur"],
                 "duration": round(it["probe"]["duration"], 2), "size": it["probe"]["size"],
                 "lufs": it["qc"].get("lufs"), "true_peak": it["qc"].get("true_peak")} for it in items.values()]
    json.dump(manifest, open(os.path.join(ROOT, "manifest.json"), "w"), indent=1)
    big = [it["file"] for it in items.values() if it["probe"]["size"] > 95 * 1_048_576]
    print(f"built index + {len(items)} pages" + (f"  WARNING >95MB: {big}" if big else ""))


if __name__ == "__main__":
    main()
