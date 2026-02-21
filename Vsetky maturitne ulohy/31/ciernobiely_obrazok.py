import tkinter

def bod(x,y,farba):
    canvas.create_rectangle(x,y,x+1,y+1,width=0,fill = farba)
def vykresli(vsetky_odtiene):
    canvas.delete("all")
    subor = open(nazov, "r")
    riadok = subor.readline()
    y = 0
    for riadok in subor:
        riadok = riadok.strip()
        
        for x in range(sirka):
            odtien = riadok[x*2:x*2+2]
            if not vsetky_odtiene:
                farba="black"
                if odtien>"7f":
                    farba = "white"
            else:
                farba ="#"+3*odtien
            bod(x,y,farba)
        canvas.update()
        y = y + 1
    subor.close()
odtiene = True
def CB():
    global odtiene
    odtiene = not odtiene
    vykresli(odtiene)
    

nazov = "ciernobiely_obrazok_1.txt"
subor = open(nazov, "r")
riadok = subor.readline()
subor.close()
velkost = riadok.split()
sirka = int(velkost[0])
vyska = int(velkost[1])

canvas = tkinter.Canvas(width=sirka, height=vyska, background="white")
canvas.pack()
vykresli(odtiene)
button = tkinter.Button(text="CB", command=CB)
button.pack()
canvas.mainloop()
    