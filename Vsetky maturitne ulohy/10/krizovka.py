import tkinter
c = tkinter.Canvas(width =1000, height = 400 )
c.pack()

vstup = open("krizovka.txt", "r")
velkostStvorca= 40

def stvorceky(x,y,farba):
    c.create_rectangle(x,y,x+velkostStvorca,y+velkostStvorca, fill = farba)
cisla = []
slova = []
riadok = vstup.readline()
while riadok != '':
    cisla.append(riadok[0])
    slova.append(riadok[2:-1])
    riadok = vstup.readline()
def nakresliKrizovku(x):
    pismena = []
    zaciatky= []
    konce = []
    y = 40
    for i in range(len(cisla)):
        pismena.append(slova[i][int(cisla[i])-1])
        zaciatky.append(slova[i][0:int(cisla[i])-1])
        konce.append(slova[i][int(cisla[i]):])
        stvorceky(x,y,'grey')
        xz = x-velkostStvorca
        xk = x+velkostStvorca
        if zaciatky!='':
            for j in range(len(zaciatky[i])):
                stvorceky(xz,y,'white')
                xz -=velkostStvorca
        if konce!="":
            for j in range(len(konce[i])):
                stvorceky(xk,y,'white')
                xk +=velkostStvorca
        y +=velkostStvorca
def napisPismena(x):
    pismena = []
    zaciatky= []
    konce = []
    y = 40
    for i in range(len(cisla)):
        pismena.append(slova[i][int(cisla[i])-1])
        zaciatky.append(slova[i][0:int(cisla[i])-1])
        konce.append(slova[i][int(cisla[i]):])
        c.create_text(x+velkostStvorca/2,y+velkostStvorca/2,text=pismena[i], font = "Arial 20 bold")
        xz = x-len(zaciatky[i])*velkostStvorca
        xk = x+velkostStvorca
        if zaciatky!='':
            for j in range(len(zaciatky[i])):
                c.create_text(xz+velkostStvorca/2,y+velkostStvorca/2,text=zaciatky[i][j],font = "Arial 20")
                xz +=velkostStvorca
        if konce!="":
            for j in range(len(konce[i])):
                c.create_text(xk+velkostStvorca/2,y+velkostStvorca/2,text=konce[i][j],font = "Arial 20")
                xk +=velkostStvorca
        y +=velkostStvorca
nakresliKrizovku(250)
nakresliKrizovku(700)
napisPismena(700)
vstup.close()
c.mainloop()