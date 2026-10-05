# Site architecture: every page, its section, primary keyword, keyword regex, and planned links.
# section: home | hub | door | service | brand | area | guide | util
PAGES = [
  # slug, section, nav label, primary keyword, regex for keyword pull, related slugs
  ("", "home", "Home", "garage doors milton keynes", r"milton keynes", []),

  # Hubs
  ("garage-doors", "hub", "Garage Doors", "garage doors milton keynes types", r"^(garage doors|types of garage doors|garage doors uk|garage doors for sale|new garage doors|garage doors online)$", []),
  ("services", "hub", "Services", "garage door services milton keynes", r"^(garage doors (repairs?|servic\w+|fitted|replacement|installation)|installation for garage doors|installed garage doors)", []),
  ("areas", "hub", "Areas We Cover", "garage doors buckinghamshire", r"buckinghamshire|bedfordshire|northamptonshire", []),
  ("guides", "hub", "Guides", "garage door advice guides", r"^(how|what|which|are|can|do|does|who)\b", []),
  ("brands", "hub", "Brands", "garage door brands", r"^(hormann|hörmann|garador|cardale|novoferm|sws|henderson|gliderol|wessex|teckentrup|seceuroglide)\b.*garage doors$", []),

  # Door types (money pages)
  ("roller-garage-doors", "door", "Roller Garage Doors", "roller garage doors milton keynes", r"roller|roll up|rolling", ["electric-garage-doors","insulated-garage-doors","secure-garage-doors","brand-sws","roller-garage-doors-secure","how-roller-garage-doors-work"]),
  ("sectional-garage-doors", "door", "Sectional Garage Doors", "sectional garage doors milton keynes", r"sectional", ["brand-hormann","insulated-garage-doors","electric-garage-doors","brand-novoferm","double-garage-doors"]),
  ("up-and-over-garage-doors", "door", "Up and Over Garage Doors", "up and over garage doors milton keynes", r"up and over|up & over|up-and-over|canopy|retractable", ["steel-garage-doors","brand-garador","brand-cardale","garage-door-spring-cable-repairs","garage-door-automation"]),
  ("side-hinged-garage-doors", "door", "Side Hinged Garage Doors", "side hinged garage doors milton keynes", r"side hinged|side-hinged|swing|hinged", ["wooden-garage-doors","grp-garage-doors","garage-side-doors","double-garage-doors"]),
  ("electric-garage-doors", "door", "Electric Garage Doors", "electric garage doors milton keynes", r"electric|automatic|automated|auto garage|remote", ["garage-door-automation","electric-garage-door-repairs","roller-garage-doors","sectional-garage-doors","electric-garage-door-not-working"]),
  ("insulated-garage-doors", "door", "Insulated Garage Doors", "insulated garage doors milton keynes", r"insulat|thermal|energy", ["are-insulated-garage-doors-worth-it","sectional-garage-doors","roller-garage-doors","garage-door-condensation-weather-seals"]),
  ("wooden-garage-doors", "door", "Wooden & Timber Garage Doors", "wooden garage doors milton keynes", r"wood|timber|oak|hardwood|cedar|larch", ["side-hinged-garage-doors","bespoke-garage-doors","painting-garage-doors","what-are-garage-doors-made-of"]),
  ("steel-garage-doors", "door", "Steel Garage Doors", "steel garage doors milton keynes", r"steel|metal", ["up-and-over-garage-doors","secure-garage-doors","painting-garage-doors","brand-garador"]),
  ("grp-garage-doors", "door", "GRP Garage Doors", "grp garage doors milton keynes", r"grp|fibreglass|fiberglass|glass reinforced", ["side-hinged-garage-doors","up-and-over-garage-doors","wooden-garage-doors","brand-cardale"]),
  ("aluminium-garage-doors", "door", "Aluminium Garage Doors", "aluminium garage doors milton keynes", r"alumin", ["roller-garage-doors","modern-garage-doors","garage-doors-with-windows"]),
  ("composite-garage-doors", "door", "Composite Garage Doors", "composite garage doors milton keynes", r"composite|upvc|pvc", ["side-hinged-garage-doors","garage-side-doors","modern-garage-doors"]),
  ("double-garage-doors", "door", "Double Garage Doors", "double garage doors milton keynes", r"double|wide|two car|2 car", ["sectional-garage-doors","roller-garage-doors","garage-door-sizes-uk","garage-conversion-doors"]),
  ("bespoke-garage-doors", "door", "Bespoke & Made to Measure", "bespoke garage doors milton keynes", r"bespoke|made to measure|custom|tailor", ["wooden-garage-doors","garage-door-sizes-uk","modern-garage-doors"]),
  ("garage-side-doors", "door", "Garage Side Doors", "garage side doors milton keynes", r"side door|personnel|pedestrian|wicket|back door|rear door", ["composite-garage-doors","side-hinged-garage-doors","secure-garage-doors"]),
  ("garage-doors-with-windows", "door", "Garage Doors with Windows", "garage doors with windows", r"window|glass|glazed|vision", ["sectional-garage-doors","aluminium-garage-doors","modern-garage-doors"]),
  ("modern-garage-doors", "door", "Modern Garage Doors & Colours", "modern garage doors", r"modern|contemporary|black|grey|gray|anthracite|white|colour|color|blue|green|red|brown", ["sectional-garage-doors","aluminium-garage-doors","painting-garage-doors","bespoke-garage-doors"]),
  ("secure-garage-doors", "door", "Secure Garage Doors", "secure garage doors milton keynes", r"secur|lock|burglar|police", ["roller-garage-doors-secure","how-to-secure-garage-door","roller-garage-doors","steel-garage-doors"]),

  # Services
  ("garage-door-repairs", "service", "Garage Door Repairs", "garage door repairs milton keynes", r"repair|fix|broken|stuck|jammed", ["electric-garage-door-repairs","garage-door-spring-cable-repairs","garage-door-servicing","repair-or-replace-garage-door"]),
  ("electric-garage-door-repairs", "service", "Electric Door Repairs", "electric garage door repairs", r"(electric|automatic|motor|opener|remote|roller).*(repair|fix|not working)", ["garage-door-repairs","electric-garage-door-not-working","garage-door-automation"]),
  ("garage-door-spring-cable-repairs", "service", "Springs & Cables", "garage door spring replacement", r"spring|cable|cone|tension", ["garage-door-repairs","up-and-over-garage-doors","garage-door-maintenance"]),
  ("garage-door-servicing", "service", "Garage Door Servicing", "garage door servicing milton keynes", r"servic|maintenance|maintain|lubric", ["garage-door-maintenance","garage-door-repairs","how-long-do-garage-doors-last"]),
  ("garage-door-replacement", "service", "Garage Door Replacement", "replacement garage doors milton keynes", r"replac|new garage", ["garage-door-installation","garage-door-prices","repair-or-replace-garage-door","types-of-garage-doors"]),
  ("garage-door-installation", "service", "Supply & Fit Installation", "garage doors supplied and fitted", r"install|fitted|fitting|supply|supplied", ["garage-door-replacement","garage-door-prices","garage-door-sizes-uk"]),
  ("garage-door-automation", "service", "Garage Door Automation", "automate existing garage door", r"automat\w+ existing|convert|conversion kit|motor|opener|operator", ["electric-garage-doors","electric-garage-door-repairs","up-and-over-garage-doors"]),
  ("garage-door-prices", "service", "Garage Door Prices", "garage door prices milton keynes", r"price|cost|how much|cheap|quote", ["garage-door-replacement","electric-garage-doors","roller-garage-doors","up-and-over-garage-doors"]),

  # Brands
  ("brand-hormann", "brand", "Hörmann", "hormann garage doors milton keynes", r"hormann|hörmann", ["sectional-garage-doors","up-and-over-garage-doors","brands"]),
  ("brand-garador", "brand", "Garador", "garador garage doors milton keynes", r"garador", ["up-and-over-garage-doors","side-hinged-garage-doors","brands"]),
  ("brand-cardale", "brand", "Cardale", "cardale garage doors milton keynes", r"cardale", ["up-and-over-garage-doors","garage-door-spring-cable-repairs","brands"]),
  ("brand-novoferm", "brand", "Novoferm", "novoferm garage doors milton keynes", r"novoferm", ["sectional-garage-doors","roller-garage-doors","brands"]),
  ("brand-sws", "brand", "SWS / SeceuroGlide", "sws garage doors milton keynes", r"sws|seceuro", ["roller-garage-doors","secure-garage-doors","brands"]),
  ("brand-henderson", "brand", "Henderson", "henderson garage doors milton keynes", r"henderson", ["up-and-over-garage-doors","garage-door-spring-cable-repairs","brands"]),

  # Areas
  ("garage-doors-bletchley", "area", "Bletchley", "garage doors bletchley", r"bletchley", []),
  ("garage-doors-newport-pagnell", "area", "Newport Pagnell", "garage doors newport pagnell", r"newport pagnell", []),
  ("garage-doors-olney", "area", "Olney", "garage doors olney", r"olney", []),
  ("garage-doors-wolverton", "area", "Wolverton", "garage doors wolverton", r"wolverton", []),
  ("garage-doors-stony-stratford", "area", "Stony Stratford", "garage doors stony stratford", r"stony stratford", []),
  ("garage-doors-buckingham", "area", "Buckingham", "garage doors buckingham", r"buckingham\b(?!shire)", []),
  ("garage-doors-leighton-buzzard", "area", "Leighton Buzzard", "garage doors leighton buzzard", r"leighton buzzard", []),
  ("garage-doors-towcester", "area", "Towcester", "garage doors towcester", r"towcester", []),
  ("garage-doors-woburn-sands", "area", "Woburn Sands", "garage doors woburn sands", r"woburn", []),
  ("garage-doors-cranfield", "area", "Cranfield", "garage doors cranfield", r"cranfield", []),
  ("garage-doors-winslow", "area", "Winslow", "garage doors winslow", r"winslow", []),
  ("garage-doors-bedford", "area", "Bedford", "garage doors bedford", r"bedford\b(?!shire)", []),
  ("garage-doors-northampton", "area", "Northampton", "garage doors northampton", r"northampton\b(?!shire)", []),
  ("garage-doors-aylesbury", "area", "Aylesbury", "garage doors aylesbury", r"aylesbury", []),

  # Guides (topical authority)
  ("types-of-garage-doors", "guide", "Types of Garage Doors", "types of garage doors uk", r"types of|kind of garage|what are the 5|different garage", ["roller-garage-doors","sectional-garage-doors","up-and-over-garage-doors","side-hinged-garage-doors"]),
  ("roller-garage-doors-secure", "guide", "Are Roller Doors Secure?", "are roller garage doors secure", r"secure are roller|roller.*secure|secure roller", ["roller-garage-doors","secure-garage-doors","how-to-secure-garage-door"]),
  ("are-insulated-garage-doors-worth-it", "guide", "Are Insulated Doors Worth It?", "are insulated garage doors worth it", r"insulat.*(worth|best|how)|how to insulate", ["insulated-garage-doors","garage-door-condensation-weather-seals"]),
  ("how-roller-garage-doors-work", "guide", "How Roller Doors Work", "how do roller garage doors work", r"how do .*work|how .* work|space do roller|manual override", ["roller-garage-doors","electric-garage-doors","electric-garage-door-not-working"]),
  ("how-long-do-garage-doors-last", "guide", "How Long Do Garage Doors Last?", "how long do garage doors last", r"how long|lifespan|last\b", ["garage-door-servicing","repair-or-replace-garage-door","garage-door-replacement"]),
  ("painting-garage-doors", "guide", "Painting Garage Doors", "can you paint garage doors", r"paint|stain|spray", ["steel-garage-doors","wooden-garage-doors","modern-garage-doors"]),
  ("what-are-garage-doors-made-of", "guide", "Garage Door Materials", "what are garage doors made of", r"made of|made out of|material", ["steel-garage-doors","wooden-garage-doors","grp-garage-doors","aluminium-garage-doors"]),
  ("garage-door-maintenance", "guide", "Garage Door Maintenance", "how to maintain garage doors", r"maintain|lubric|lube|grease|oil|clean", ["garage-door-servicing","garage-door-spring-cable-repairs"]),
  ("home-insurance-garage-doors", "guide", "Insurance & Garage Doors", "does home insurance cover garage doors", r"insurance", ["secure-garage-doors","garage-door-repairs"]),
  ("garage-door-sizes-uk", "guide", "Garage Door Sizes UK", "garage door sizes uk", r"size|wide|width|tall|height|dimension|measure", ["bespoke-garage-doors","double-garage-doors","garage-door-installation"]),
  ("how-to-secure-garage-door", "guide", "How to Secure Your Garage", "how to secure garage doors", r"how to secure|lock|security", ["secure-garage-doors","roller-garage-doors-secure","home-insurance-garage-doors"]),
  ("electric-garage-door-not-working", "guide", "Electric Door Not Working?", "electric garage door not working", r"not working|won.t|power cut|power is out|open by themselves|on their own|program|manually", ["electric-garage-door-repairs","electric-garage-doors","how-roller-garage-doors-work"]),
  ("repair-or-replace-garage-door", "guide", "Repair or Replace?", "can garage doors be repaired", r"can garage doors be repaired|repair or replace|replace.*repair", ["garage-door-repairs","garage-door-replacement","garage-door-prices"]),
  ("garage-conversion-doors", "guide", "Garage Conversion Doors", "garage conversion doors", r"conversion|french door|bifold|2 garage doors into 1", ["double-garage-doors","garage-side-doors"]),
  ("garage-door-condensation-weather-seals", "guide", "Condensation & Weather Seals", "garage door weather seals", r"seal|draught|draft|condensation|weather|damp", ["insulated-garage-doors","garage-door-maintenance"]),
  ("best-garage-doors-uk", "guide", "Choosing the Best Door", "best garage doors uk", r"best|which garage|top rated|resale|trend", ["types-of-garage-doors","brands","garage-door-prices"]),
  ("electric-garage-door-cost", "guide", "Electric Garage Door Cost", "how much are electric garage doors", r"(electric|automatic|remote).*(cost|price|how much)|how much.*(electric|automatic)", ["electric-garage-doors","garage-door-automation","garage-door-prices"]),

  # Utility
  ("about", "util", "About", "about garage doors milton keynes", r"$^", []),
  ("contact", "util", "Get a Quote", "garage door quote milton keynes", r"$^", []),
  ("privacy", "util", "Privacy", "privacy", r"$^", []),
  ("thank-you", "util", "Thank You", "thank you", r"$^", []),
]
