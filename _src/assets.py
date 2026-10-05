"""SVG brand assets: logo, door illustrations, van livery, hero scene."""
INK = "#14213D"; BLUE = "#1F4E89"; SUN = "#E3A33B"; CORAL = "#C8553D"; SKY = "#E9EEF5"; WHITE = "#FFFFFF"; STEEL = "#C9D3E6"

def mark(x=0, y=0, s=1.0):
    """Logo mark: blue rounded square, yellow roof, roller-door slats."""
    return f'''<g transform="translate({x},{y}) scale({s})">
  <rect width="100" height="100" rx="22" fill="{BLUE}"/>
  <path d="M14 46 L50 18 L86 46" fill="none" stroke="{SUN}" stroke-width="9" stroke-linecap="round" stroke-linejoin="round"/>
  <rect x="26" y="48" width="48" height="36" rx="3" fill="{WHITE}"/>
  <rect x="26" y="48" width="48" height="7" fill="{SUN}"/>
  <rect x="26" y="59" width="48" height="4" fill="{BLUE}" opacity=".9"/>
  <rect x="26" y="67" width="48" height="4" fill="{BLUE}" opacity=".9"/>
  <rect x="26" y="75" width="48" height="4" fill="{BLUE}" opacity=".9"/>
</g>'''

def logo_svg(dark_text=INK, sub=BLUE):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 520 110" role="img" aria-label="Garage Doors Milton Keynes">
{mark(4,5,1)}
<text x="122" y="56" font-family="'Bricolage Grotesque','Arial Black',Arial,sans-serif" font-weight="800" font-size="46" fill="{dark_text}" letter-spacing="-1">Garage Doors</text>
<text x="124" y="94" font-family="'Bricolage Grotesque','Arial Black',Arial,sans-serif" font-weight="800" font-size="27" fill="{sub}" letter-spacing="5.2">MILTON KEYNES</text>
</svg>'''

def logo_stacked():
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 300" role="img" aria-label="Garage Doors Milton Keynes">
<rect width="400" height="300" fill="{SUN}"/>
{mark(140,24,1.2)}
<text x="200" y="210" text-anchor="middle" font-family="'Bricolage Grotesque','Arial Black',Arial,sans-serif" font-weight="800" font-size="46" fill="{INK}" letter-spacing="-1">Garage Doors</text>
<text x="200" y="250" text-anchor="middle" font-family="'Bricolage Grotesque','Arial Black',Arial,sans-serif" font-weight="800" font-size="24" fill="{BLUE}" letter-spacing="5">MILTON KEYNES</text>
</svg>'''

def favicon():
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100">{mark()}</svg>'

# ---------- door illustrations ----------
def _frame(inner, bg=SKY, w=480, h=360):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" role="img">
<rect width="{w}" height="{h}" rx="28" fill="{bg}"/>
<circle cx="{w-70}" cy="70" r="34" fill="{SUN}"/>
<rect x="0" y="{h-46}" width="{w}" height="46" fill="#D7DEEC"/>
<path d="M70 {h-46} L70 120 L240 50 L410 120 L410 {h-46} Z" fill="{WHITE}"/>
<path d="M54 128 L240 40 L426 128" fill="none" stroke="{INK}" stroke-width="14" stroke-linejoin="round" stroke-linecap="round"/>
<rect x="110" y="140" width="260" height="{h-46-140}" fill="{INK}"/>
{inner}
</svg>'''

def door_roller(color=WHITE, open_frac=0.0):
    x, y, w, hgt = 118, 148, 244, 166
    top = y; slats = ""
    vis = hgt*(1-open_frac)
    n = int(vis/9)
    for i in range(n):
        slats += f'<rect x="{x}" y="{top+i*9}" width="{w}" height="7" rx="1.5" fill="{color}"/>'
    box = f'<rect x="{x-8}" y="{y-14}" width="{w+16}" height="20" rx="6" fill="{BLUE}"/>'
    bar = f'<rect x="{x}" y="{top+n*9}" width="{w}" height="6" fill="{CORAL}"/>' if n else ""
    return _frame(box + slats + bar)

def door_sectional(color=WHITE, windows=False):
    x, y, w, hgt = 118, 148, 244, 166
    panels = ""; ph = hgt/4
    for i in range(4):
        py = y + i*ph
        panels += f'<rect x="{x}" y="{py+1}" width="{w}" height="{ph-3}" rx="3" fill="{color}"/>'
        for r in range(1, 4):
            panels += f'<rect x="{x+8}" y="{py+r*ph/4-1}" width="{w-16}" height="2" fill="{STEEL}"/>'
        if windows and i == 0:
            for k in range(4):
                panels += f'<rect x="{x+18+k*57}" y="{py+8}" width="44" height="{ph-19}" rx="4" fill="{SKY}" stroke="{INK}" stroke-width="3"/>'
    return _frame(panels)

def door_upover(color=WHITE):
    x, y, w, hgt = 118, 148, 244, 166
    s = f'<rect x="{x}" y="{y}" width="{w}" height="{hgt}" rx="3" fill="{color}"/>'
    for i in range(1, 16):
        s += f'<rect x="{x+i*w/16-1.5}" y="{y+8}" width="3" height="{hgt-16}" fill="{STEEL}"/>'
    s += f'<rect x="{x+w/2-18}" y="{y+hgt/2-6}" width="36" height="12" rx="6" fill="{CORAL}"/>'
    return _frame(s)

def door_sidehinged(color="#C98A4B", line="#9C6431"):
    x, y, w, hgt = 118, 148, 244, 166
    s = ""
    for k in range(2):
        lx = x + k*(w/2+2)
        s += f'<rect x="{lx}" y="{y}" width="{w/2-2}" height="{hgt}" rx="3" fill="{color}"/>'
        for i in range(1, 7):
            s += f'<rect x="{lx+i*(w/2-2)/7-1}" y="{y+6}" width="2" height="{hgt-12}" fill="{line}"/>'
        s += f'<path d="M{lx+8} {y+hgt-10} L{lx+w/2-10} {y+12}" stroke="{line}" stroke-width="6"/>'
        s += f'<rect x="{lx+6}" y="{y+16}" width="{w/2-14}" height="8" fill="{line}"/><rect x="{lx+6}" y="{y+hgt-24}" width="{w/2-14}" height="8" fill="{line}"/>'
    s += f'<rect x="{x+w/2-14}" y="{y+hgt/2-14}" width="6" height="28" rx="3" fill="{SUN}"/><rect x="{x+w/2+8}" y="{y+hgt/2-14}" width="6" height="28" rx="3" fill="{SUN}"/>'
    return _frame(s)

def door_sidedoor():
    s = door_sectional(color="#3C4A5E")
    # add a pedestrian door at right of house — overlay via string replace before </svg>
    extra = f'<rect x="384" y="190" width="0" height="0"/>'
    return s

def door_grp():
    return door_sidehinged(color="#F4F6FA", line="#C9D3E6")

def door_wood():
    return door_sidehinged()

def door_composite():
    return door_sidehinged(color="#3A4252", line="#232A36")

def door_double():
    return door_sectional(color=WHITE).replace('viewBox="0 0 480 360"', 'viewBox="0 0 480 360"')

DOOR_ART = {
  "roller-garage-doors": lambda: door_roller(),
  "electric-garage-doors": lambda: door_roller(color=WHITE, open_frac=.35),
  "insulated-garage-doors": lambda: door_sectional(color="#F3F6FC"),
  "sectional-garage-doors": lambda: door_sectional(),
  "up-and-over-garage-doors": lambda: door_upover(),
  "steel-garage-doors": lambda: door_upover(color="#E9EEF6"),
  "side-hinged-garage-doors": lambda: door_sidehinged(),
  "wooden-garage-doors": lambda: door_sidehinged(),
  "grp-garage-doors": lambda: door_grp(),
  "composite-garage-doors": lambda: door_composite(),
  "aluminium-garage-doors": lambda: door_roller(color="#D8DEE8"),
  "double-garage-doors": lambda: door_sectional(color=WHITE),
  "bespoke-garage-doors": lambda: door_sidehinged(color="#8E5A33", line="#6B4022"),
  "garage-side-doors": lambda: door_composite(),
  "garage-doors-with-windows": lambda: door_sectional(windows=True),
  "modern-garage-doors": lambda: door_sectional(color="#3C4450", windows=True),
  "secure-garage-doors": lambda: door_roller(color="#AEB8C8"),
  "garage-door-repairs": lambda: door_upover(),
  "electric-garage-door-repairs": lambda: door_roller(open_frac=.5),
  "garage-door-spring-cable-repairs": lambda: door_upover(color="#E9EEF6"),
  "garage-door-servicing": lambda: door_sectional(),
  "garage-door-replacement": lambda: door_sectional(color="#3C4450"),
  "garage-door-installation": lambda: door_sectional(windows=True),
  "garage-door-automation": lambda: door_roller(open_frac=.3),
  "garage-door-prices": lambda: door_sectional(color=WHITE),
}

# ---------- van ----------
def van_side(phone="01908 000000", web="garage-doors-milton-keynes.co.uk", w=1200, h=520, bg=None, flip=False, uid="a"):
    """Side elevation of a high-roof LWB panel van with full livery. flip=True gives the passenger side (cab on the left)."""
    bgrect = f'<rect width="{w}" height="{h}" fill="{bg}"/>' if bg else ""
    body = "M60 70 Q60 40 95 40 L850 40 Q900 40 930 70 L1050 200 Q1070 222 1110 232 Q1150 242 1150 290 L1150 400 Q1150 420 1130 420 L80 420 Q60 420 60 400 Z"
    shell = f'''<defs><clipPath id="vb{uid}"><path d="{body}"/></clipPath></defs>
<g clip-path="url(#vb{uid})">
  <rect x="0" y="0" width="{w}" height="{h}" fill="{WHITE}"/>
  <path d="M0 300 L560 300 Q640 300 700 250 L1200 -60 L1200 520 L0 520 Z" fill="{SUN}"/>
  <path d="M0 340 L600 340 Q690 340 760 290 L1200 10 L1200 520 L0 520 Z" fill="{BLUE}"/>
  <rect x="60" y="356" width="520" height="10" fill="{SUN}"/>
  <rect x="60" y="376" width="520" height="10" fill="{SUN}" opacity=".7"/>
  <rect x="60" y="396" width="520" height="10" fill="{SUN}" opacity=".45"/>
</g>
<path d="{body}" fill="none" stroke="{INK}" stroke-width="6"/>
<path d="M872 70 L1010 205 L872 205 Z" fill="#9FB4D9" stroke="{INK}" stroke-width="6" stroke-linejoin="round"/>
<line x1="860" y1="60" x2="860" y2="420" stroke="{INK}" stroke-width="4"/>
<line x1="520" y1="44" x2="520" y2="420" stroke="{INK}" stroke-width="2" opacity=".2"/>
<rect x="890" y="232" width="40" height="10" rx="5" fill="{INK}"/>
<rect x="1128" y="252" width="24" height="34" rx="6" fill="{CORAL}"/>
<g fill="{INK}"><circle cx="250" cy="420" r="62"/><circle cx="960" cy="420" r="62"/></g>
<g fill="#D9DFEA"><circle cx="250" cy="420" r="30"/><circle cx="960" cy="420" r="30"/></g>'''
    text = f'''{mark(90,74,1.15)}
<text x="232" y="128" font-family="'Bricolage Grotesque','Arial Black',Arial,sans-serif" font-weight="800" font-size="64" fill="{INK}" letter-spacing="-1.5">Garage Doors</text>
<text x="236" y="172" font-family="'Bricolage Grotesque','Arial Black',Arial,sans-serif" font-weight="800" font-size="36" fill="{BLUE}" letter-spacing="7">MILTON KEYNES</text>
<text x="92" y="228" font-family="'Figtree',Arial,sans-serif" font-weight="700" font-size="25" fill="{INK}">Repairs · Supply &amp; Fit · Electric Doors · Servicing</text>
<text x="92" y="264" font-family="'Figtree',Arial,sans-serif" font-weight="800" font-size="24" fill="{BLUE}">{web}</text>
<text x="92" y="330" font-family="'Bricolage Grotesque','Arial Black',Arial,sans-serif" font-weight="800" font-size="58" fill="{INK}">{phone}</text>'''
    if flip:
        shell = f'<g transform="translate({w},0) scale(-1,1)">{shell}</g>'
        text = f'<g transform="translate(560,12) scale(.78)">{text}</g>'
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" role="img" aria-label="Garage Doors Milton Keynes van livery">
{bgrect}
<ellipse cx="600" cy="468" rx="560" ry="18" fill="#000" opacity=".12"/>
{shell}
{text}
</svg>'''

def van_rear(phone="01908 000000", web="garage-doors-milton-keynes.co.uk"):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 640" role="img" aria-label="Van rear doors livery">
<defs><clipPath id="vr"><rect x="40" y="30" width="520" height="560" rx="36"/></clipPath></defs>
<g clip-path="url(#vr)">
 <rect x="0" y="0" width="600" height="640" fill="{WHITE}"/>
 <path d="M0 470 L600 400 L600 640 L0 640 Z" fill="{SUN}"/>
 <path d="M0 510 L600 440 L600 640 L0 640 Z" fill="{BLUE}"/>
</g>
<rect x="40" y="30" width="520" height="560" rx="36" fill="none" stroke="{INK}" stroke-width="6"/>
<line x1="300" y1="30" x2="300" y2="590" stroke="{INK}" stroke-width="4"/>
<rect x="70" y="60" width="200" height="130" rx="14" fill="#9FB4D9" stroke="{INK}" stroke-width="5"/>
<rect x="330" y="60" width="200" height="130" rx="14" fill="#9FB4D9" stroke="{INK}" stroke-width="5"/>
{mark(250,212,1)}
<text x="300" y="358" text-anchor="middle" font-family="'Bricolage Grotesque','Arial Black',Arial,sans-serif" font-weight="800" font-size="48" fill="{INK}">Garage Doors</text>
<text x="300" y="396" text-anchor="middle" font-family="'Bricolage Grotesque','Arial Black',Arial,sans-serif" font-weight="800" font-size="25" fill="{BLUE}" letter-spacing="5">MILTON KEYNES</text>
<text x="300" y="548" text-anchor="middle" font-family="'Bricolage Grotesque','Arial Black',Arial,sans-serif" font-weight="800" font-size="46" fill="{WHITE}">{phone}</text>
<text x="300" y="580" text-anchor="middle" font-family="'Figtree',Arial,sans-serif" font-weight="700" font-size="21" fill="{SUN}">{web}</text>
</svg>'''

def hero_scene(phone):
    """Home hero: house with roller door, van parked alongside."""
    van = van_side(phone=phone).split('\n',1)[1].rsplit('</svg>',1)[0]
    slats = ''.join(f'<rect x="150" y="{350+i*17}" width="380" height="13" rx="3" fill="#F4F7FD"/>' for i in range(11))
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 760" role="img" aria-label="Garage Doors Milton Keynes van outside a home with a new roller garage door">
<rect width="1200" height="760" rx="28" fill="#DCE4EF"/><circle cx="1040" cy="150" r="70" fill="{SUN}" opacity=".85"/>
<path d="M60 680 L60 290 L340 110 L620 290 L620 680 Z" fill="{WHITE}"/>
<path d="M30 306 L340 92 L650 306" fill="none" stroke="{INK}" stroke-width="30" stroke-linejoin="round" stroke-linecap="round"/>
<rect x="140" y="340" width="400" height="340" fill="{INK}"/>
<rect x="128" y="318" width="424" height="32" rx="10" fill="{BLUE}"/>
{slats}
<rect x="150" y="537" width="380" height="9" fill="{CORAL}"/>
<path d="M0 680 H1200 V732 Q1200 760 1172 760 H28 Q0 760 0 732 Z" fill="#C5D0DF"/>
<rect x="0" y="680" width="1200" height="10" fill="{INK}" opacity=".15"/>
<g transform="translate(470,428) scale(.6)">{van}</g>
</svg>'''
