import tkinter
c = tkinter.Canvas(width=500, height=320)
c.pack()

pocet = 0
celkovyPocet = 0
zapalky = ()
hrac = 1
zapalkyPreJednoKolo = 3
uzVyzdvihnuteZapalky = 0
hra = False
historia = ()
t = ''

def velkazapalka(x, y):
    telo = c.create_line(x, y+3, x, y+200, fill="#f6bf52", width=10)
    hlava = c.create_oval(x+10, y, x-10, y+30, fill="#aa1111", outline="")
    return telo, hlava

def malazapalka(x, y):
    telo = c.create_line(x, y+3, x, y+100, fill="#f6bf5f", width=8)
    hlava = c.create_oval(x+7, y, x-7, y+20, fill="#aa1111", outline="")
    return telo, hlava

def text(n):#funkcia na to aby texty boli na tom istom mieste ale iba jeden za raz
    global t
    if t: #ked '' su prazdne to je False
        c.delete(t)
    t = c.create_text(250, 300, text=n, font="Arial 10")

def kreslitZ():
    global zapalky, pocet, celkovyPocet, hra, hrac, historia, uzVyzdvihnuteZapalky
    hra = True
    hrac = 1
    historia = ()
    uzVyzdvihnuteZapalky = 0
    c.delete("all")
    pocet = int(entry1.get()) #dostali sme pocet zapaliek od usera
    celkovyPocet = pocet
    zapalky = ()

    if pocet > 20:
        pocet = 20
        print("Viac ako 20 zapaliek sa nezmesti.")

    if pocet > 10: #pouzieme male zapalky ak je ich viac ako 10
        for i in range(pocet // 2): # rovnomerne rozdelime zapalky na hornu a dolnu cast +berieme do uvahy parne a neparne cisla
            x = (i + 1) * (400 / (pocet / 2))
            y = 150
            telo, hlava = malazapalka(x, y)
            zapalky = zapalky + ((i, telo, hlava, x, y),)
        for i in range(pocet - pocet // 2):
            x = (i + 1) * (400 / (pocet / 2))
            y = 30
            telo, hlava = malazapalka(x, y)
            zapalky = zapalky + (((pocet // 2) + i, telo, hlava, x, y),)
    else:
        for i in range(pocet): 
            x = (i + 1) * (400 / pocet)
            y = 30
            telo, hlava = velkazapalka(x, y)
            zapalky = zapalky + ((i, telo, hlava, x, y),)

    text("Hrac " + str(hrac) + " je na tahu (vezmi 1–3 zapalky)") 

def klik(event):
    global zapalky, pocet, uzVyzdvihnuteZapalky, hrac, hra, historia

    if not hra: #kontrolujeme ci hra sa zacala 
        return

    if uzVyzdvihnuteZapalky >= zapalkyPreJednoKolo:
        text("Nemozeš vziat viac ako 3 zapalky!")
        return

    nove_zapalky = ()
    klikZ = 0

    for z in zapalky:
        index, telo, hlava, x, y = z # zapalky=((...,...,...,...,...),(...,...,...,...,...),...) z = (...,...,...,...,...)
        if pocet>10:#dlhsie zapalky maju aj dlhsie okolie 
            dlzka = 100
        else:
            dlzka = 200
        if abs(event.x - x) < 10 and y <= event.y <= y + dlzka and klikZ == 0: #klik pri zapalke sa rata ako klik po zapalke
            klikZ = index
            c.delete(telo)#vymazujeme zapalku
            c.delete(hlava)
            pocet -= 1
            uzVyzdvihnuteZapalky += 1
            historia = historia + ((hrac, index),)
        else:
            nove_zapalky = nove_zapalky + (z,)#iba nevymazane zapalky

    zapalky = nove_zapalky
    if pocet == 0:
        text("Hrac " + str(hrac) + " prehral!")
        hra = False

def koniecTahu():
    global hra,hrac, uzVyzdvihnuteZapalky
    
    if not hra:
        return
    if uzVyzdvihnuteZapalky == 0:
        text("Musis vziat aspon jednu zapalku!")
        return

    
    if hrac == 1:
        hrac = 2 
    else: hrac= 1
    uzVyzdvihnuteZapalky = 0
    text("Hrac " + str(hrac) + " je na tahu (vezmi 1–3 zapalky)")

def repriza():
    global celkovyPocet, zapalky
    c.delete("all")
    zapalky = ()

    if celkovyPocet > 10:
        for i in range(celkovyPocet):
            x = (i % 10 + 1) * (400 / (celkovyPocet / 2))
            y = 30 if i < 10 else 150
            telo, hlava = malazapalka(x, y)
            zapalky = zapalky + ((i, telo, hlava, x, y),)
    else:
        for i in range(celkovyPocet):
            x = (i + 1) * (400 / celkovyPocet)
            y = 30
            telo, hlava = velkazapalka(x, y)
            zapalky = zapalky + ((i, telo, hlava, x, y),)

    def animacia(krok):
        global zapalky
        if krok >= len(historia):  
            return
        hracN, idx = historia[krok]
        nove_zapalky = ()
        for z in zapalky:
            i, telo, hlava, x, y = z#aj ked nepouzivame x a z dalej musime z z dat tie premenne niekam
            if i == idx:
                c.delete(telo)
                c.delete(hlava)
            else:
                nove_zapalky = nove_zapalky + (z,)
        zapalky = nove_zapalky
        c.after(600, lambda: animacia(krok + 1))#vdaka lambde program trochu pocka

    animacia(0)

entry1 = tkinter.Entry()
entry1.pack()

button1 = tkinter.Button(command=kreslitZ, text="OK (nova hra)")
button2 = tkinter.Button(command=koniecTahu, text="Koniec tahu")
button3 = tkinter.Button(command=repriza, text="Repriza")

button1.pack()
button2.pack()
button3.pack()

c.bind("<Button-1>", klik)

c.mainloop()
