import tkinter
def stlac(event):
    global y
    if len(zastavky) > 0:
        canvas.create_rectangle(100, y + 2, 200, y + 18)
        aktpocet = zastavky.pop(0)
        if aktpocet > kapacita:
            farba = 'red'
        else:
            farba = 'green'
        canvas.create_rectangle(100, y + 2, 100 + 100 * aktpocet / kapacita,
                                y + 18, fill=farba)
        y += 20
canvas = tkinter.Canvas(width=500, height=400, bg='white')
canvas.pack()
canvas.focus_set()
subor = open('vytazenost_autobusovej_linky.txt')
kapacita = 0
zastavky = []
pocet = 0
y = 20
for riadok in subor:
    if kapacita == 0:  # Prvý riadok
        kapacita = int(riadok)
    else:
        casti = riadok.split()
        pocet += int(casti[0])  # Nastupujúci
        pocet -= int(casti[1])  # Vystupujúci
        zastavky.append(pocet)
        canvas.create_text(5, y, text=' '.join(casti[2:]), anchor='nw')
        # join lebo názov zastávky môže byť viacslovný
        y += 20
subor.close()
y = 20
canvas.bind('<Key>', stlac)
canvas.mainloop()
