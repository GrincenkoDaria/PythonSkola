import tkinter

vstup = open("lodicky.txt", "r")
rozmery = vstup.readline().split()

velkost = 50
canvas = tkinter.Canvas(
    width=int(rozmery[0]) * velkost,
    height=int(rozmery[1]) * velkost
)
canvas.pack()

x = 0
y = 0
mapa = []

for riadok in vstup:
    riadok = riadok.split()
    mapa.append(riadok)
    
    for i in riadok:
        farba = "blue"
        if i == "1":
            farba = "darkgrey"
        
        canvas.create_rectangle(x, y, x + velkost, y + velkost, fill=farba, outline="")
        x += velkost
    
    y += velkost
    x = 0

vstup.close()

def kresli_lodicku(x, y):
    canvas.create_rectangle(x, y, x + velkost*3, y + velkost, fill='yellow')


def kontrola_miesta():
    for i in range(len(mapa)):
        for j in range(len(mapa[i]) - 2):
            if mapa[i][j] == "0" and mapa[i][j+1] == "0" and mapa[i][j+2] == "0":
                return i, j+2
    return None, None


def pridaj():
    riadok, blok = kontrola_miesta()
    
    if riadok is not None:
        mapa[riadok][blok-2] = '2'
        mapa[riadok][blok-1] = '2'
        mapa[riadok][blok] = '2'
        
        kresli_lodicku((blok-2) * velkost, riadok * velkost)


button = tkinter.Button(text="Pridaj lodicku", command=pridaj)
button.pack()

canvas.mainloop()