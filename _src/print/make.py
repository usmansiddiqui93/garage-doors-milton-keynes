import sys; import os; sys.path.insert(0,os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import assets as A, build as B
from playwright.sync_api import sync_playwright
P=B.PHONE; W="garage-doors-milton-keynes.co.uk"
side=A.van_side(phone=P,uid="d"); pas=A.van_side(phone=P,flip=True,uid="q"); rear=A.van_rear(phone=P)
def card_front():
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 850 550"><rect width="850" height="550" fill="{A.SUN}"/>{A.mark(60,60,1.3)}
<text x="60" y="300" font-family="Bricolage Grotesque" font-weight="800" font-size="72" fill="{A.INK}" letter-spacing="-1.5">Garage Doors</text>
<text x="64" y="350" font-family="Bricolage Grotesque" font-weight="800" font-size="36" fill="{A.BLUE}" letter-spacing="8">MILTON KEYNES</text>
<rect y="470" width="850" height="80" fill="{A.INK}"/><text x="60" y="522" font-family="Figtree" font-weight="700" font-size="28" fill="#fff">Repairs · Supply &amp; Fit · Electric Doors · Servicing</text></svg>'''
def card_back():
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 850 550"><rect width="850" height="550" fill="{A.BLUE}"/>
<text x="60" y="120" font-family="Figtree" font-weight="700" font-size="30" fill="{A.SUN}">Free survey &amp; written quote</text>
<text x="60" y="250" font-family="Bricolage Grotesque" font-weight="800" font-size="92" fill="#fff">{P}</text>
<text x="60" y="320" font-family="Figtree" font-weight="700" font-size="34" fill="#fff">{W}</text>
<text x="60" y="470" font-family="Figtree" font-weight="600" font-size="26" fill="#C6D2EC">Milton Keynes · Bletchley · Newport Pagnell · Olney · Buckingham</text></svg>'''
css='''@page{size:420mm 297mm;margin:0}body{margin:0;font-family:Figtree;color:#0B1B3F}
.pg{width:420mm;height:297mm;box-sizing:border-box;padding:18mm 20mm;page-break-after:always;display:flex;flex-direction:column;gap:8mm;position:relative}
h1{font-family:'Bricolage Grotesque';font-size:30pt;margin:0}h2{font-family:'Bricolage Grotesque';font-size:18pt;margin:0}
.note{font-size:11pt;color:#4A5878;max-width:300mm}.art{flex:1;display:flex;align-items:center;justify-content:center}.art svg{max-width:100%;max-height:100%}
.sw{display:flex;gap:8mm}.sw div{width:60mm}.sw i{display:block;height:34mm;border-radius:4mm;border:1px solid #ccd}
.foot{position:absolute;bottom:10mm;left:20mm;font-size:9pt;color:#7a87a5}.grid{display:grid;grid-template-columns:1fr 1fr;gap:12mm;flex:1}.grid>div{display:flex;flex-direction:column;gap:3mm;justify-content:center;border:1px dashed #ccd;border-radius:4mm;padding:8mm}'''
sw=[("Navy","#14213D","C100 M80 Y35 K45","Pantone 2767 C (closest)"),("Steel Blue","#1F4E89","C95 M65 Y10 K10","Pantone 2154 C (closest)"),("Amber","#E3A33B","C5 M38 Y85 K0","Pantone 7409 C (closest)"),("Brick","#C8553D","C10 M78 Y80 K5","Pantone 7618 C (closest)"),("White","#FFFFFF","C0 M0 Y0 K0","Vinyl white")]
swh="".join(f'<div><i style="background:{h}"></i><b>{n}</b><br>{h}<br>{c}<br><small>{p}</small></div>' for n,h,c,p in sw)
pages=[
 f'<div class="pg"><h1>Van Livery &amp; Brand Print Pack</h1><p class="note">Garage Doors Milton Keynes · artwork for vehicle graphics, business cards and signage. Artwork is drawn for a long-wheelbase high-roof panel van (Ford Transit / Mercedes Sprinter / VW Crafter class). Your sign-maker should scale it to the exact vehicle template, check panel joins, handles and the fuel cap, and convert text to outlines before cutting. Confirm the phone number before printing.</p><div class="art">{A.logo_svg()}</div><h2>Colours</h2><div class="sw">{swh}</div><p class="note">Fonts: Bricolage Grotesque ExtraBold (headings, phone) and Figtree Bold (strapline, web address). Both are free Google Fonts (SIL Open Font License).</p></div>',
 f'<div class="pg"><h1>Driver side (offside)</h1><p class="note">Cab at the front (right). Phone number should be readable from 20 m: at true scale it is roughly 150–170 mm cap height.</p><div class="art">{side}</div></div>',
 f'<div class="pg"><h1>Passenger side (nearside)</h1><p class="note">Mirrored colour sweep so the graphic rises towards the front. Text sits clear of the sliding door handle area; the sign-maker should adjust around the door seam.</p><div class="art">{pas}</div></div>',
 f'<div class="pg"><h1>Rear doors</h1><p class="note">Logo straddles the door split; keep the phone number clear of the rear lights and number plate area.</p><div class="art" style="max-height:220mm">{rear}</div></div>',
 f'<div class="pg"><h1>Logo set</h1><div class="grid"><div>{A.logo_svg()}<b>Primary — on white</b></div><div style="background:#0B1B3F">{A.logo_svg(dark_text="#FFFFFF",sub=A.SUN)}<b style="color:#fff">Reversed — on navy</b></div><div>{A.logo_stacked()}<b>Stacked — on yellow (bonnet, signage, social)</b></div><div style="align-items:center"><div style="width:70mm">{A.favicon()}</div><b>Mark only — bonnet, wing mirrors, favicon</b></div></div></div>',
 f'<div class="pg"><h1>Business card (85 × 55 mm)</h1><p class="note">Add 3 mm bleed on all sides when sending to print.</p><div class="grid"><div>{card_front()}<b>Front</b></div><div>{card_back()}<b>Back</b></div></div></div>',
]
html=f'<html><head><style>{css}</style></head><body>{"".join(pages)}</body></html>'
out=os.path.dirname(os.path.abspath(__file__))+'/'
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page()
    pg.set_content(html); pg.wait_for_timeout(500)
    pg.pdf(path=out+'GDMK-van-livery-print-pack.pdf',width='420mm',height='297mm',print_background=True)
    for name,svg,w,h in [('van-driver-side',side,4800,2080),('van-passenger-side',pas,4800,2080),('van-rear',rear,2400,2560),('logo-primary',A.logo_svg(),3120,660),('logo-stacked',A.logo_stacked(),2400,1800),('logo-mark',A.favicon(),2000,2000)]:
        open(out+name+'.svg','w').write(svg)
        q=b.new_page(viewport={'width':w//4,'height':h//4},device_scale_factor=4)
        q.set_content(f'<body style="margin:0">{svg.replace("<svg ","<svg style=\'width:100vw;height:100vh;display:block\' ",1)}</body>'); q.wait_for_timeout(200)
        q.screenshot(path=out+name+'.png',omit_background=True); q.close()
    b.close()
print('ok')
