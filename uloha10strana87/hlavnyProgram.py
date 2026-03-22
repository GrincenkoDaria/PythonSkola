import tkinter
import vlajkamodul
subor=open("krajiny.txt","r",encoding="utf-8")
vstup=subor.readlines()
subor.close()
tkinter.Tk()
c=tkinter.Canvas(width=950,height=150)
c.pack()
n=[]
roz=[]
oby=[]
emi=[]
v=[]
x=100
y=50
vzd=150

for riadok in vstup:
    riadok=riadok.strip()
    if riadok!="":
        nazov,zvislo,farby,rozloha,pocet_obyvatelov,pocet_emigrantov=riadok.split(";")
        farby=tuple(farby.split(","))
        zvislo=zvislo=="True"
        vl=vlajkamodul.Vlajka(x,y,100,70,zvislo,farby)
        v.append(vl)
        n.append(nazov)
        roz.append(float(rozloha))
        oby.append(int(pocet_obyvatelov))
        emi.append(int(pocet_emigrantov))
        x+=vzd

def kresli():
    c.delete("all")
    for i in range(len(v)):
        v[i].kresli(c)
        c.create_text(v[i].x,v[i].y+v[i].vyska/2+15,text=n[i])

def rovnako():
    for i in range(len(v)):
        v[i].sirka=100
        v[i].vyska=70
    kresli()

def rozloha():
    mi=min(roz);ma=max(roz)
    for i in range(len(v)):
        v[i].sirka=100
        v[i].vyska=70
        v[i].zoom(0.5+(roz[i]-mi)/(ma-mi)*1.5)
    kresli()

def obyvatelia():
    mi=min(oby);ma=max(oby)
    for i in range(len(v)):
        v[i].sirka=100
        v[i].vyska=70
        v[i].zoom(0.5+(oby[i]-mi)/(ma-mi)*1.5)
    kresli()

def emigranti():
    mi=min(emi);ma=max(emi)
    for i in range(len(v)):
        v[i].sirka=100
        v[i].vyska=70
        v[i].zoom(0.5+(emi[i]-mi)/(ma-mi)*1.5)
    kresli()
kresli()

b1=tkinter.Button(text="Rovnako",command=rovnako)
b1.pack()
b2=tkinter.Button(text="Rozloha",command=rozloha)
b2.pack()
b3=tkinter.Button(text="Obyvatelia",command=obyvatelia)
b3.pack()
b4=tkinter.Button(text="Emigranti",command=emigranti)
b4.pack()
c.mainloop()