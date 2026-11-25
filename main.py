import os
from PIL import Image, ImageDraw, ImageFont
W,H=1024,1024
OUT=os.path.join(os.environ.get("MAKEFUN_OUTPUT_DIR","out"),"entry.png")
def F(s,b=False,ser=False):
    p="/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf" if ser else ("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if b else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf")
    try: return ImageFont.truetype(p,s)
    except Exception: return ImageFont.load_default()
def T(d,x,y,s,f,fill=(20,20,20)): d.text((x,y),s,font=f,fill=fill)
def wrap(s,f,mx):
    ws=[]
    for w in s.split():
        if ws and d_.textlength(ws[-1]+" "+w,font=f)<=mx: ws[-1]+=" "+w
        else: ws.append(w)
    return ws
def lines(d,x,y,ss,f,mx,lh,fill=(20,20,20)):
    out=[]
    for s in ss: out+=wrap(s,f,mx)
    for i,l in enumerate(out): d.text((x,y+i*lh),l,font=f,fill=fill)
    return y+len(out)*lh
def chip(d,x,y,s,c):
    w=int(d.textlength(s,font=F(8,True)))+10; d.rounded_rectangle([x,y,x+w,y+13],2,fill=c); d.text((x+5,y+2),s,font=F(8,True),fill=(255,255,255)); return x+w+4
def R(d,x,y,w,h,c): d.rectangle([x,y,x+w,y+h],fill=c)
def E(d,x,y,w,h,c): d.ellipse([x,y,x+w,y+h],fill=c)
img=Image.new("RGB",(W,H),(250,244,230)); d_=ImageDraw.Draw(img); d=d_
# continents as (lon,lat) polygons, equirectangular map later
NA=[(-168,66),(-140,70),(-125,72),(-110,73),(-95,80),(-85,70),(-80,73),(-65,60),(-55,52),(-60,47),(-70,42),(-75,35),(-80,32),(-85,29),(-90,21),(-97,16),(-105,20),(-110,24),(-117,33),(-125,40),(-125,49),(-135,58),(-155,58)]
SA=[(-80,9),(-77,4),(-80,-3),(-81,-6),(-77,-12),(-70,-18),(-70,-23),(-65,-25),(-58,-28),(-52,-32),(-48,-28),(-40,-20),(-35,-9),(-40,-3),(-50,0),(-60,5),(-70,9)]
GL=[(-58,64),(-45,60),(-40,64),(-30,68),(-25,70),(-35,76),(-55,76),(-60,70)]
EU=[(-10,36),(-9,43),(-2,48),(-4,50),(0,51),(3,53),(8,57),(10,59),(18,56),(21,55),(24,58),(28,60),(30,62),(32,70),(40,68),(45,66),(40,60),(35,55),(30,50),(28,45),(23,40),(22,37),(19,42),(12,44),(8,44),(3,43),(-2,37)]
AF=[(-6,35),(0,36),(10,37),(11,34),(20,32),(30,31),(32,31),(35,28),(37,22),(40,15),(43,11),(48,11),(51,10),(46,5),(41,0),(40,-5),(36,-12),(32,-18),(28,-26),(20,-35),(16,-28),(12,-18),(12,-6),(9,4),(4,6),(-8,5),(-13,8),(-17,15),(-17,20),(-15,25),(-10,30)]
AS=[(30,62),(40,68),(50,70),(60,70),(70,73),(80,73),(90,75),(100,77),(110,74),(120,73),(130,72),(140,72),(150,70),(160,66),(170,66),(178,65),(170,60),(162,58),(158,52),(150,59),(142,55),(140,45),(135,43),(130,42),(127,40),(122,38),(120,32),(122,28),(118,25),(110,20),(108,15),(105,10),(100,8),(98,12),(95,16),(92,20),(88,22),(85,20),(80,15),(77,8),(75,12),(72,20),(68,23),(62,25),(58,26),(55,26),(52,28),(50,30),(48,30),(44,29),(40,25),(35,20),(35,15),(38,12),(42,15),(43,12),(40,18),(35,22),(32,28),(30,32),(28,38),(25,40),(28,45),(30,50),(32,55)]
AU=[(113,-22),(114,-30),(115,-35),(120,-34),(125,-32),(130,-32),(135,-35),(140,-38),(145,-38),(150,-37),(153,-32),(150,-25),(146,-19),(142,-15),(142,-11),(137,-12),(135,-15),(132,-12),(130,-13),(126,-14),(122,-17),(118,-20)]
CONT=[NA,SA,GL,EU,AF,AS,AU]
def scene(d,x,y,w,h,kind):
    bg={"sky":(18,32,64),"court":(40,60,110),"gate":(150,30,30),"war":(30,28,50),"sport":(20,110,60),"sea":(20,80,120),"market":(20,60,90),"tech":(120,20,20),"heli":(90,70,40),"city":(60,40,90),"desert":(170,120,50),"space":(10,15,45)}.get(kind,(40,60,90))
    R(d,x,y,w,h,bg)
    if kind=="sky":
        for i,bx in enumerate([8,45,95,150,210,260]): R(d,x+bx,y+h-55-(i%3)*18,28,55+(i%3)*18,(35,55,95))
        R(d,x+150,y+8,26,70,(220,200,120)); E(d,x+215,y+18,26,26,(255,170,60)); E(d,x+228,y+30,34,14,(120,120,120))
    elif kind=="court":
        R(d,x+10,y+h-45,w-20,45,(210,200,170)); R(d,x+w//2-45,y+12,90,22,(230,220,190)); d.line([x+20,y+h-45,x+w-20,y+h-45],fill=(120,90,40),width=3); R(d,x+w-70,y+30,34,10,(180,140,60))
    elif kind=="gate":
        R(d,x+20,y+20,w-40,h-20,(180,60,50)); R(d,x+w//2-14,y+30,28,44,(250,244,230)); d.rectangle([x+30,y+30,x+w-30,y+38],outline=(255,220,120),width=2); R(d,x+12,y+h-18,w-24,8,(255,255,255))
    elif kind=="war":
        E(d,x+30,y+12,30,30,(255,180,60)); E(d,x+w-70,y+30,22,22,(255,120,40)); R(d,x+10,y+h-30,w-20,30,(60,55,60)); d.line([x+20,y+20,x+90,y+40],fill=(255,255,255),width=2)
    elif kind=="sport":
        E(d,x+w//2-22,y+8,44,44,(255,210,60)); d.line([x+10,y+h-12,x+w-10,y+h-12],fill=(255,255,255),width=3); R(d,x+14,y+16,10,26,(220,40,40)); R(d,x+w-24,y+16,10,26,(20,120,60))
    elif kind=="sea":
        R(d,x,y+h-26,w,26,(15,60,110)); R(d,x+20,y+18,w-90,18,(200,60,50)); R(d,x+30,y+6,8,14,(255,255,255)); R(d,x+w-60,y+30,40,10,(240,240,240))
    elif kind=="market":
        d.line([x+8,y+h-10,x+w-8,y+14],fill=(80,200,120),width=4); d.line([x+8,y+30,x+60,y+22,x+120,y+34,x+w-8,y+10],fill=(255,220,80),width=2); R(d,x+10,y+8,60,14,(255,255,255))
    elif kind=="tech":
        R(d,x+14,y+14,w-28,26,(30,30,40)); d.text((x+20,y+18),"CODE RED",font=F(11,True),fill=(255,80,80)); E(d,x+w//2-8,y+28,16,16,(255,60,60))
    elif kind=="heli":
        E(d,x+w//2-18,y+14,36,18,(90,90,100)); d.line([x+10,y+22,x+w-10,y+22],fill=(200,200,200),width=3); R(d,x+20,y+h-22,w-40,22,(70,90,60))
    elif kind=="city":
        for i,bx in enumerate([10,60,110,160,210]): R(d,x+bx,y+20+(i%2)*12,32,h-32,(80,70,120))
        E(d,x+w-40,y+10,22,22,(255,200,80))
    elif kind=="desert":
        R(d,x,y+h-24,w,24,(200,170,90)); R(d,x+30,y+18,60,26,(180,140,70)); E(d,x+w-50,y+12,26,26,(255,220,120))
    else:
        E(d,x+w//2-16,y+10,32,32,(230,230,240)); d.line([x+10,y+h-14,x+w-10,y+h-14],fill=(255,255,255),width=2); R(d,x+16,y+44,18,10,(255,180,60))
HEROES=[("1","RIYADH","MIDDLE EAST","CONFIRMED","Houthi drone hits Riyadh's tallest tower again, 11 hurt","A Houthi drone hit the PIF tower, the tallest in Riyadh, for the second time in a week. At least 11 were hurt.","11","sky",(20,90,140)),("2","SHANGHAI","ASIA","OFFICIAL","China probes Shanghai party chief Chen Jining","Chen Jining, 62, is probed for serious violations. He is the fourth Politburo member to fall this year.","62","gate",(150,30,30)),("3","NEW YORK","US / TECH","CONFIRMED","Huawei guilty on 10 of 12 counts","A US jury found Huawei guilty on 10 of 12 counts, including trade-secret theft and bank fraud. Sentencing is in Sep 2027.","10/12","court",(40,60,110))]
HSRC=["Saudi officials","CCDI","US court"]
CARDS=[("4","ZAPORIZHZHIA","EUROPE / WAR","REPORTED","Russian attacks kill 9 across Ukraine in a day","Russia launched 96 drones; 73 were shot down. Nine were killed and 81 wounded.","war"),("5","CAS","AFRICA / SPORT","OFFICIAL","CAS hands Senegal back the AFCON title","CAS restored the title to Senegal after Morocco forfeited 3-0, so Senegal won 1-0.","sport"),("6","HORMUZ","MIDDLE EAST","REPORTED","IRGC attacks container ship in Hormuz","An IRGC attack hit a container ship at 18:58 UTC, switching off its navigation near Khasab.","sea"),("7","NEW YORK","WORLD / MARKETS","CONFIRMED","Dow closes above 50,000 for the first time","The Dow closed at 50,018, its first finish above 50,000. Taiex jumped a record 8.99%.","market"),("8","REDMOND","WORLD / TECH","REPORTED","Microsoft declares 'Code Red' after historic outage","After a 24-hour outage, Microsoft set a one-hour global recovery target.","tech"),("9","ESKISEHIR","EUROPE","REPORTED","Turkish military helicopter crash kills 5","A Turkish military AS-532 helicopter crashed in Eskisehir, killing all five on board.","heli"),("10","CARTAGENA","AMERICAS","REPORTED","Supermarket hostages: 25 held in Cartagena","Twenty-five people were held in a Cartagena supermarket, and five elderly women were freed.","city"),("11","ADEN","MIDDLE EAST","REPORTED","Houthis advance within 60 km of Aden","Houthi forces advanced to within 60 km of Aden in Yemen, wires reported at 16:51 UTC.","desert"),("12","LAHJ","MIDDLE EAST","REPORTED","Saudi strikes kill 25, wound 6 in Yemen","Saudi strikes on a bus and truck in Wadi Maabaq killed or left missing 25 and wounded six.","desert"),("13","JIUQUAN","WORLD / SPACE","OFFICIAL","China names first foreign astronaut for Tiangong","China named the Shenzhou-24 crew: Tang Hongbo, Wu Yi and Zeeshan Ali of Pakistan.","space")]
ALSO=[("14","Ankara","Haftar visits Turkey, first time.","REPORTED"),("15","London","UK sanctions Houthis + 4 officials.","OFFICIAL"),("16","Villavicencio","Car bomb injures 23.","REPORTED"),("17","Gaza","Israel kills Hamas security chief.","REPORTED"),("18","Baghdad","Iraq takes Kurdish oilfields.","OFFICIAL"),("19","Gaza","Meningitis alert: 272 cases in Oct.","OFFICIAL"),("20","DR Congo","Cessna 208 missing, rebels claim hit.","CLAIM"),("21","Hanoi","Hot-pot blast kills at least 6.","REPORTED"),("22","Gulf of Finland","Ukraine hits ship Sparta II.","REPORTED"),("23","Kuala Lumpur","Malaysia returns migrants to Myanmar.","OFFICIAL"),("24","Ulleungdo","S. Korea shelter order, jets in ADIZ.","OFFICIAL"),("25","Dhaka","Hasina plans return on 16 Dec.","REPORTED"),("26","The Hague","14 nations back ICJ Myanmar ruling.","REPORTED"),("27","Jakarta","Indonesia names 2 VP candidates.","OFFICIAL"),("28","Beijing","China sentences Ma to death, spying.","OFFICIAL"),("29","Brussels","NATO vows defence vs space threat.","OFFICIAL"),("30","Mexico City","El Chapo Isidro, held Fri 20 Nov; US drone aided capture.","REPORTED"),("31","San Salvador","Bukele names 3 soldiers killed in Haiti.","OFFICIAL"),("32","Ottawa","Pentagon rebukes Canada: only 41.9% of air fleet ready.","REPORTED"),("33","Washington","US adds Megaspeed to blacklist.","OFFICIAL"),("34","Kyiv","Zelensky urges talks soon.","REPORTED"),("35","Ras Al Khaimah","UAE bus-truck crash kills 13.","REPORTED"),("36","London","England record 5,258 heat deaths.","OFFICIAL"),("37","Kourou","Ariane 6 lofts 36 Amazon satellites.","OFFICIAL"),("38","Cikande","Factory-fire toll rises to 26.","REPORTED")]
# header
R(d,0,0,W,4,(180,30,30)); T(d,8,10,"THE WORLD ON ONE PAGE",F(11,True),(180,30,30))
d.text((1016-d.textlength("38 STORIES · 6 REGIONS · 13 FIELDS",font=F(11,True)),10),"38 STORIES · 6 REGIONS · 13 FIELDS",font=F(11,True),fill=(180,30,30))
T(d,8,28,"Tuesday 24 November 2026",F(30,True,True)); T(d,8,62,"Riyadh tower hit again · Shanghai party chief probed · Huawei guilty on 10 of 12 counts.",F(12,False,True),(150,30,30))
# region bar
RB=[("Europe",9,(30,80,160)),("Middle East",8,(180,30,30)),("Asia",8,(200,120,20)),("Africa",2,(20,120,60)),("Americas",7,(120,60,140)),("World / Space",4,(40,90,110))]
x=8
for n,v,c in RB:
    w=int(1008*v/38); R(d,x,80,w-2,20,c); T(d,x+6,84,f"{n} {v}",F(10,True),(255,255,255)); x+=w
# number strip: 8 numbers
NS=[("11","hurt in Riyadh"),("9","killed in Ukraine"),("50,018","Dow close"),("+8.99%","Taiex record"),("25","killed in Lahj"),("26","Cikande toll"),("10/12","Huawei counts"),("96","drones at Ukraine")]
T(d,8,104,"THE DAY IN NUMBERS",F(10,True),(180,30,30)); x=8
for n,l in NS:
    T(d,x,118,n,F(20,True)); T(d,x,140,l,F(8,False),(90,90,90)); x+=126
R(d,8,158,W-16,1,(180,30,30))
T(d,8,162,"BY THE CLOCK · UTC  02:15 NATO vows space defence · 08:16 Hanoi blast · 10:42 Saudi strikes Yemen · 14:27 Riyadh tower hit · 16:51 Houthis 60 km from Aden · 18:58 Hormuz ship attack · 20:41 Huawei guilty.",F(9,False),(60,60,60))
# heroes: scene 100px tall (y 180-280), text below
HY=180; HW=330; HX=[8,347,686]
for i,(num,loc,field,ch,hl,deck,giant,kind,c) in enumerate(HEROES):
    x=HX[i]; scene(d,x,HY,HW,92,kind); d.text((x+HW-10,HY+38),giant,font=F(40,True),anchor="ra",fill=(255,255,255)); d.rectangle([x,HY,x+34,HY+22],fill=(0,0,0)); T(d,x+4,HY+4,num,F(12,True),(255,255,255))
    y=HY+96; T(d,x,y,f"{num} {loc} · {field}",F(10,True),(180,30,30)); y+=14; cx=chip(d,x,y,ch,(20,110,60) if ch=="CONFIRMED" else (30,80,160)); T(d,cx,y,HSRC[i],F(8,False),(100,100,100)); y+=16
    y=lines(d,x,y,[hl],F(13,True),HW,15); y=lines(d,x,y,[deck],F(10,False),HW,13)
# cards grid 5+5: mini-scene 48px, text below
CY=[360,486]
for r in range(2):
    for j in range(5):
        idx=r*5+j; num,loc,field,ch,hl,deck,kind=CARDS[idx]; x=8+j*202; y=CY[r]; scene(d,x,y,196,48,kind); d.rectangle([x,y,x+22,y+18],fill=(0,0,0)); T(d,x+3,y+2,num,F(10,True),(255,255,255))
        yy=y+52; T(d,x,yy,f"{loc} · {field}",F(8,True),(180,30,30)); yy+=12; chip(d,x,yy,ch,(20,110,60) if ch=="CONFIRMED" else ((30,80,160) if ch=="OFFICIAL" else (110,110,110))); yy+=16; yy=lines(d,x,yy,[hl],F(10,True),196,12); lines(d,x,yy,[deck],F(9,False),196,11)
# map: equirectangular, lon -180..180 -> x 8..508, lat 80..-60 -> y 614..794 (180px tall)
MX,MY,MW,MH=8,614,500,180
def mp(lon,lat): return MX+(lon+180)/360*MW, MY+(80-lat)/140*MH
R(d,MX,MY,MW,MH,(210,225,235)); d.rectangle([MX,MY,MX+MW,MY+MH],outline=(100,100,100))
for poly in CONT:
    pts=[mp(lo,la) for lo,la in poly]; d.polygon(pts,fill=(150,190,130),outline=(90,120,80))
T(d,MX+6,MY+4,"WORLD MAP — PINS 1–13",F(9,True),(40,40,40))
PINS=[(1,24.7,46.7),(2,31.2,121.5),(3,40.7,-74.0),(4,47.8,35.2),(5,14.7,-17.4),(6,26.5,56.3),(7,40.7,-74.0),(8,47.7,-122.1),(9,39.8,30.5),(10,10.4,-75.5),(11,12.8,45.0),(12,13.0,44.9),(13,39.7,98.5)]
OFF={3:(0,-14),7:(0,14),11:(-16,-10),12:(16,10),6:(14,-12)}
for n,la,lo in PINS:
    px,py=mp(lo,la); dx,dy=OFF.get(n,(0,0)); qx,qy=px+dx,py+dy
    if (dx,dy)!=(0,0): d.line([px,py,qx,qy],fill=(180,30,30),width=1)
    E(d,qx-9,qy-9,18,18,(180,30,30)); d.text((qx-d.textlength(str(n),font=F(9,True))/2,qy-7),str(n),font=F(9,True),fill=(255,255,255))
# legend beside map
T(d,524,614,"1–13  WHERE THE STORIES ARE",F(11,True),(180,30,30))
LEG=["1 Riyadh — PIF tower hit","2 Shanghai — Chen Jining probe","3 New York — Huawei guilty","4 Zaporizhzhia — 9 killed","5 Senegal — CAS returns AFCON title","6 Hormuz — ship attacked","7 New York — Dow over 50,000","8 Redmond — Microsoft Code Red","9 Eskisehir — helicopter crash","10 Cartagena — 25 hostages","11 Aden — Houthis 60 km away","12 Lahj — Saudi strikes kill 25","13 Jiuquan — first foreign astronaut"]
for i,s in enumerate(LEG):
    xx=524+(i%2)*246; yy=636+(i//2)*22; d.text((xx,yy),s,font=F(10,False),fill=(20,20,20))
T(d,524,786,"Map: real lat/lon, equirectangular.",F(9,False),(100,100,100))
# ALSO 25 stories, 3 columns
T(d,8,800,"ALSO ON TUESDAY 24 NOVEMBER — 25 MORE STORIES",F(11,True),(180,30,30))
COLS=[ALSO[0:9],ALSO[9:18],ALSO[18:25]]
for ci,col in enumerate(COLS):
    x=8+ci*336
    for ri,(n,city,txt,ch) in enumerate(col):
        y=818+ri*12; s=f"{n} {city}: {txt} [{ch}]"; d.text((x,y),s,font=F(8,False),fill=(20,20,20))
# DATE CHECK: exactly 2 lines, 40px tall (y 930-970)
R(d,8,930,W-16,40,(180,30,30)); T(d,14,934,"DATE CHECK — Every story above happened or was first reported on Tue 24 Nov 2026. Wires read up to 23:00 UTC.",F(10,True),(255,255,255))
T(d,14,950,"LEFT OUT (not 24 Nov): Hormuz mine claims (23 Nov) · Nvidia Huang returns (23 Nov) · EU sanctions 22 (23 Nov) · COP31 no deal (22 Nov). NOT YET: Shenzhou-24 launch (25 Nov) · Huawei sentencing (Sep 2027).",F(9,False),(255,255,255))
# footer
T(d,8,976,"Sources: Saudi officials · CCDI · US court · CAS · UKMTO · Reuters · AP · CMSA · wires. CONFIRMED = 2+ outlets · OFFICIAL = on record · REPORTED = one outlet · CLAIM = one side's claim.",F(9,False),(80,80,80))
T(d,8,992,"Scenes are drawn in code, not photographs. Tuesday 24 November 2026 — 38 stories, one page.",F(9,False),(80,80,80))
R(d,0,1008,W,16,(180,30,30))
os.makedirs(os.path.dirname(OUT) or ".",exist_ok=True); img.save(OUT)
print("saved",OUT,os.path.getsize(OUT))
