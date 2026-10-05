import pandas as pd,re,json,warnings
warnings.filterwarnings('ignore')
from plan import PAGES
df=pd.read_csv('/tmp/claude-0/-home-claude/da491566-5526-5f55-88e3-f23ab13e112a/scratchpad/all.csv')
q=pd.read_csv('/root/.claude/uploads/da491566-5526-5f55-88e3-f23ab13e112a/6fc98c55-google_gb_garage-doors_matching-terms_2026-10-06_00-23-17.csv',encoding='utf-16',sep='\t')
df=pd.concat([df[['Keyword','Volume']],q[['Keyword','Volume']]]).drop_duplicates('Keyword')
df['Volume']=df.Volume.fillna(0)
df['Keyword']=df.Keyword.str.lower()
local='milton keynes|bletchley|newport pagnell|olney|wolverton|stony stratford|buckingham|leighton buzzard|woburn|towcester|cranfield|winslow|bedford|northampton|aylesbury'
# Learn "place words" = words that appear in 'garage doors X' location patterns but aren't topical
allw=pd.Series(' '.join(df.Keyword).split()).value_counts()
topical=set('garage doors door roller sectional up and over side hinged electric automatic automated auto insulated wooden wood timber steel grp aluminium aluminum composite double bespoke windows window modern secure repair repairs price prices cost costs how much are what is the of to a for uk near me new replacement replace fitted fit fitting installation install installed servicing service spring springs cable cables motor motors remote control black grey gray white anthracite oak glass with made measure custom best types type cheap security lock locks paint painted painting supply supplied canopy retractable sliding shutter shutters insulation can you do does who which why when where in my on it be by out from metal fibreglass fiberglass hardwood tall wide size sizes hormann hörmann garador cardale novoferm sws henderson seceuroglide gliderol wessex teckentrup personnel pedestrian french bifold conversion condensation seal seals draught weather insurance home house lubricant maintain maintenance clean last long work secure burglar power manual override program trends trend resale value colour colours color opener openers operator automate existing stuck broken fix tension cones vision glazed contemporary swing barn fold folding worth benefits lifespan dimensions standard single height width convert should often buy sale rated top cheapest kind different 5 manually themselves own their locking get much & up-and-over side-hinged roll rolling shutter detached single car cars panel panels doors, upvc pvc mk2 tilt traditional retractable canopy security garage’ diy kit kits opening openers fixing fixed best electrical electronic insulating thermal energy efficient there 2 two into 1 one'.split())
def national(s): return all(w in topical or w.isdigit() for w in s.split())
out={}
for slug,sec,label,pk,rx,rel in PAGES:
  m=df[df.Keyword.str.contains(rx,regex=True)]
  if sec=='area':
    m=m.sort_values('Volume',ascending=False).head(30)
  elif sec=='home':
    m=m[m.Keyword.str.contains('milton keynes')].sort_values('Volume',ascending=False).head(40)
  else:
    ml=m[m.Keyword.str.contains(local)].sort_values('Volume',ascending=False).head(15)
    mn=m[~m.Keyword.str.contains(local)]
    mn=mn.loc[mn.Keyword.map(national).astype(bool).values] if len(mn) else mn.sort_values('Volume',ascending=False).head(30)
    m=pd.concat([ml,mn])
  out[slug or 'home']={'section':sec,'label':label,'primary':pk,'related':rel,'keywords':[f'{r.Keyword} ({int(r.Volume)})' for r in m.itertuples()]}
json.dump(out,open('keywords.json','w'),indent=1)
for s,v in out.items(): print(s, len(v['keywords']), '; '.join(v['keywords'][:7]))
