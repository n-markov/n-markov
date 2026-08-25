#!/usr/bin/env python3
"""Generate light_mode.svg and dark_mode.svg for n-markov's GitHub profile README."""

import os

MONO = "ui-monospace,SFMono-Regular,'SF Mono',Menlo,Consolas,'Liberation Mono',monospace"

DARK = dict(
    name="dark",
    card="#0E1117", border="#262C38", bar="#171C25", barline="#262C38",
    text="#C9D3E3", accent="#F2B441", accent2="#6FC3DE", muted="#6B7686",
    node="#141A24", nodeline="#33katex",  # placeholder replaced below
)
DARK["nodeline"] = "#334154"

LIGHT = dict(
    name="light",
    card="#FCFBF8", border="#E4E0D6", bar="#F3F0E8", barline="#E4E0D6",
    text="#22262E", accent="#A97A12", accent2="#22708C", muted="#7A8290",
    node="#FFFFFF", nodeline="#CFC9BC",
)

# label, value  -- label+dots is padded to exactly 16 chars so every row aligns
ROWS = [
    ("Studying",  "BSc Mathematics, University of Bath '28"),
    ("Location",  "London, UK  ·  Bath during term"),
    ("Reading",   "Problem-Solving Through Problems (Larson)"),
    ("Focus",     "data science · machine learning"),
    ("Languages", "Python · R"),
    ("Libraries", "NumPy · pandas · scikit-learn · PyTorch"),
    ("Tools",     "Git · Jupyter · openpyxl / XlsxWriter"),
    ("Latest",    "BA Forage — RandomForest booking model"),
    ("Offline",   "competitive maths · swimming · sailing"),
    ("Contact",   "nm2263@bath.ac.uk"),
]

NODES = [  # cx, cy, label
    (95, 162, "sleep"),
    (235, 162, "maths"),
    (235, 292, "code"),
    (95, 292, "swim"),
]
R = 32

CMD = "nik@bath:~$ neofetch"


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def build(p):
    o = []
    a = o.append

    a('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 920 442" '
      'width="920" height="442" role="img" '
      'aria-label="Terminal card: Nik Markov, BSc Mathematics at the University of Bath, '
      'working in statistical learning and quantitative research with Python, R, NumPy, '
      'pandas, scikit-learn and PyTorch.">')

    # ---- styles -------------------------------------------------------------
    a(f'''<style>
  .m {{ font-family: {MONO}; }}
  .fade {{ animation: fade .5s ease-out backwards; }}
  @keyframes fade {{ from {{ opacity: 0 }} }}
  #wipe {{ animation: type 1.25s steps(20) .25s backwards; }}
  @keyframes type {{ from {{ width: 0 }} }}
  .caret {{ animation: blink 1.06s steps(1) infinite; }}
  @keyframes blink {{ 50% {{ opacity: 0 }} }}
  .still {{ display: none; }}
  @media (prefers-reduced-motion: reduce) {{
    .fade {{ animation: none; }}
    #wipe {{ animation: none; }}
    .caret {{ animation: none; }}
    .tok {{ display: none; }}
    .still {{ display: inline; }}
  }}
</style>''')

    a(f'<clipPath id="typeclip"><rect id="wipe" x="34" y="52" width="178" height="22"/></clipPath>')

    # ---- window -------------------------------------------------------------
    a(f'<rect x="1" y="1" width="918" height="440" rx="11" fill="{p["card"]}" '
      f'stroke="{p["border"]}" stroke-width="1.5"/>')
    a(f'<path d="M1 12a11 11 0 0 1 11-11h896a11 11 0 0 1 11 11v26H1z" fill="{p["bar"]}"/>')
    a(f'<line x1="1" y1="38" x2="919" y2="38" stroke="{p["barline"]}" stroke-width="1.5"/>')

    # app icon + left-aligned title (Windows-style)
    a(f'<rect x="20" y="13" width="13" height="13" rx="3" fill="{p["accent2"]}"/>')
    a(f'<text class="m" x="40" y="24" text-anchor="start" font-size="12" '
      f'fill="{p["muted"]}">nik@bath: ~</text>')

    # minimize / maximize / close glyphs (Windows-style, right-aligned)
    for cx, kind in ((826, "min"), (858, "max"), (890, "close")):
        if kind == "min":
            a(f'<line x1="{cx-5}" y1="19.5" x2="{cx+5}" y2="19.5" stroke="{p["muted"]}" '
              f'stroke-width="1.3" stroke-linecap="round"/>')
        elif kind == "max":
            a(f'<rect x="{cx-5}" y="14.5" width="10" height="10" fill="none" '
              f'stroke="{p["muted"]}" stroke-width="1.3"/>')
        else:
            a(f'<line x1="{cx-5}" y1="14.5" x2="{cx+5}" y2="24.5" stroke="{p["muted"]}" '
              f'stroke-width="1.3" stroke-linecap="round"/>')
            a(f'<line x1="{cx-5}" y1="24.5" x2="{cx+5}" y2="14.5" stroke="{p["muted"]}" '
              f'stroke-width="1.3" stroke-linecap="round"/>')

    # ---- typed command ------------------------------------------------------
    a(f'<g clip-path="url(#typeclip)"><text class="m" x="34" y="68" font-size="14" '
      f'fill="{p["accent"]}">{esc(CMD)}</text></g>')

    # ---- markov chain -------------------------------------------------------
    a('<g class="fade" style="animation-delay:1.55s">')

    a(f'<g stroke="{p["nodeline"]}" stroke-width="1.6" fill="none" '
      f'marker-end="url(#arw)" stroke-linecap="round">')
    a('<line x1="131" y1="162" x2="195" y2="162"/>')     # sleep -> maths
    a('<line x1="235" y1="198" x2="235" y2="252"/>')     # maths -> code
    a('<line x1="199" y1="292" x2="135" y2="292"/>')     # code  -> swim
    a('<line x1="95" y1="256" x2="95" y2="202"/>')       # swim  -> sleep
    a('<path d="M262 275 C 336 248 336 336 264 309"/>')  # code  -> code
    a('</g>')

    a(f'<defs><marker id="arw" viewBox="0 0 8 8" refX="6.5" refY="4" markerWidth="6" '
      f'markerHeight="6" orient="auto-start-reverse">'
      f'<path d="M0 0.8 L7 4 L0 7.2 z" fill="{p["nodeline"]}"/></marker></defs>')

    for i, (cx, cy, lab) in enumerate(NODES):
        a(f'<circle cx="{cx}" cy="{cy}" r="{R}" fill="{p["node"]}" '
          f'stroke="{p["nodeline"]}" stroke-width="1.6"/>')
        a(f'<text class="m" x="{cx}" y="{cy+4}" text-anchor="middle" font-size="11.5" '
          f'fill="{p["text"]}">{lab}</text>')

    for x, y, t in ((166, 153, ".7"), (249, 228, ".8"), (166, 283, ".4"),
                    (79, 228, ".9"), (330, 296, ".6")):
        a(f'<text class="m" x="{x}" y="{y}" text-anchor="middle" font-size="10" '
          f'fill="{p["muted"]}">{t}</text>')

    # walking token
    a(f'<circle class="tok" r="5.5" fill="{p["accent2"]}">'
      '<animateMotion dur="13s" repeatCount="indefinite" begin="2.1s" '
      'path="M95 162 L235 162 L235 292 c60 -32 60 32 0 0 L95 292 L95 162" '
      'keyPoints="0;0;0.204;0.204;0.394;0.394;0.606;0.606;0.810;0.810;1" '
      'keyTimes="0;0.10;0.19;0.30;0.39;0.50;0.60;0.71;0.80;0.91;1" '
      'calcMode="linear"/></circle>')
    a(f'<circle class="still" cx="95" cy="162" r="5.5" fill="{p["accent2"]}"/>')

    # node pulses, timed to the token's pauses
    pulses = [
        ("0;0.10;0.13;0.88;0.91;1", "1;1;0;0;1;1"),
        ("0;0.17;0.19;0.30;0.33;1", "0;0;1;1;0;0"),
        ("0;0.37;0.39;0.71;0.74;1", "0;0;1;1;0;0"),
        ("0;0.78;0.80;0.91;0.94;1", "0;0;1;1;0;0"),
    ]
    for i, (kt, vals) in enumerate(pulses):
        cx, cy, _ = NODES[i]
        a(f'<circle cx="{cx}" cy="{cy}" r="{R+6}" fill="none" stroke="{p["accent2"]}" '
          f'stroke-width="1.4" opacity="0" class="tok">'
          f'<animate attributeName="opacity" dur="13s" begin="2.1s" '
          f'repeatCount="indefinite" keyTimes="{kt}" values="{vals}" calcMode="linear"/>'
          f'</circle>')

    a(f'<text class="m" xml:space="preserve" x="188" y="366" text-anchor="middle" '
      f'font-size="11" fill="{p["muted"]}">π ≈ ( .19  .27  .41  .13 )  ·  stationary</text>')
    a('</g>')

    # ---- divider ------------------------------------------------------------
    a(f'<line class="fade" style="animation-delay:1.5s" x1="345" y1="98" x2="345" y2="372" '
      f'stroke="{p["border"]}" stroke-width="1.5"/>')

    # ---- neofetch panel -----------------------------------------------------
    X = 380
    a(f'<text class="m fade" style="animation-delay:1.45s" x="{X}" y="116" font-size="15" '
      f'font-weight="600" fill="{p["accent2"]}">nik<tspan fill="{p["muted"]}">@</tspan>'
      f'<tspan fill="{p["accent"]}">markov</tspan></text>')
    a(f'<line class="fade" style="animation-delay:1.5s" x1="{X}" y1="128" x2="864" y2="128" '
      f'stroke="{p["border"]}" stroke-width="1.5"/>')

    y = 158
    for i, (label, value) in enumerate(ROWS):
        d = f"{1.62 + i*0.085:.2f}s"
        a(f'<g class="fade" style="animation-delay:{d}">')
        a(f'<text class="m" x="{X}" y="{y}" font-size="13.5" '
          f'fill="{p["accent"]}">{label}</text>')
        a(f'<line x1="468" y1="{y - 4}" x2="506" y2="{y - 4}" stroke="{p["muted"]}" '
          f'stroke-width="1.4" stroke-linecap="round" stroke-dasharray="0.1 5.4" opacity=".8"/>')
        a(f'<text class="m" x="516" y="{y}" font-size="13.5" '
          f'fill="{p["text"]}">{esc(value)}</text>')
        a('</g>')
        y += 25

    # ---- prompt -------------------------------------------------------------
    a(f'<text class="m fade" style="animation-delay:2.55s" x="34" y="406" font-size="14" '
      f'fill="{p["accent"]}">nik@bath:~$ <tspan class="caret" fill="{p["accent2"]}">▊</tspan></text>')

    a('</svg>')
    return "\n".join(o)


out = os.path.dirname(os.path.abspath(__file__))
for p in (DARK, LIGHT):
    path = f"{out}/{p['name']}_mode.svg"
    with open(path, "w", encoding="utf-8") as f:
        f.write(build(p))
    print("wrote", path)