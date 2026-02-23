import tkinter, random
canvas = tkinter.Canvas(width=650, height=270)
canvas.pack()

def kresli_riadok(x, y, posun, vnutro, pismena, velkost):
    for i in range(len(vnutro)):
        farba = "white"
        if i + posun == 0:
            farba = "darkgrey"
        canvas.create_rectangle(x+(i+posun)*velkost, y,x+(i+posun)*velkost+velkost, y + velkost, fill = farba)
        if pismena:
            canvas.create_text(x+(i+posun)*velkost+velkost/2, y+velkost/2, text=vnutro[i], font = "Arial "+str(velkost-10))

def kresli_krizovku(x, y, krizovka, vyplnit, velkost):
    for riadok in krizovka:
        kresli_riadok(x,y, riadok[0], riadok[1],vyplnit, velkost)
        y +=velkost

krizovka = []
subor = open("krizovka2-2.txt", "r")

tajnicka = subor.readline().strip()
i = 0
for r in subor:
    r = r.strip()
    posun = -1 *r.index(tajnicka[i])
    krizovka.append([posun, r])
    i +=1
kresli_krizovku(160,10,krizovka, False, 25)
kresli_krizovku(470, 10, krizovka, True, 30)

canvas.mainloop()