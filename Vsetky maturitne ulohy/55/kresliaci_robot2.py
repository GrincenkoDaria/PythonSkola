import tkinter
c = tkinter.Canvas(width=400, height=400)
c.pack()
vstup = open("kresliaci_robot2.txt", "r").readlines()

s = [[0,-1],[1,0],[0,1],[-1,0]]
smerx = 0
smery = -1

x = 200
y = 200
velkost = 50

def ciara():
    global x, y
    c.create_line(x, y, x + velkost*smerx, y + velkost*smery, width=3)
    x = x + velkost*smerx
    y = y + velkost*smery

def vlavo():
    global smerx, smery
    i = s.index([smerx, smery])
    smerx, smery = s[i - 1]

def vpravo():
    global smerx, smery
    i = s.index([smerx, smery])
    smerx, smery = s[(i + 1) % 4]

def vykonaj(prikazy):
    global vstup
    i = 0

    while i < len(prikazy):
        riadok = prikazy[i].split()

        if riadok[0] == "ciara":
            ciara()

        elif riadok[0] == "vlavo":
            vlavo()

        elif riadok[0] == "vpravo":
            vpravo()

        elif riadok[0] == "opakuj":
            n = int(riadok[1])

            blok = []
            i += 1
            hlbka = 1

            while i < len(prikazy) and hlbka > 0:
                r = prikazy[i].split()

                if r[0] == "opakuj":
                    hlbka += 1
                elif r[0] == "koniecopakuj":
                    hlbka -= 1

                if hlbka > 0:
                    blok.append(prikazy[i])

                i += 1

            for _ in range(n):
                vykonaj(blok)

            continue 

        elif riadok[0] == "koniecopakuj":
            return

        i += 1

def kresli():
    vykonaj(vstup)

b = tkinter.Button(text="Vykonaj prikazy zo suboru", command=kresli)
b.pack()

c.mainloop()