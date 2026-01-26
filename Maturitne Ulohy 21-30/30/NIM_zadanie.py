import tkinter, random
canvas = tkinter.Canvas(width=500, height=250)
canvas.pack()
def zapalka(x, y):
    canvas.create_line(x, y, x, y+100, width=5, fill='yellow')
    canvas.create_oval(x-5, y-5, x+5, y+8, fill='brown', outline='brown')
def vypis(hrac, pocet_zapaliek):
    canvas.delete('all')
    x = 40
    y = 100
    for i in range(pocet_zapaliek):
        zapalka(x,y)
        x +=30

    canvas.create_text(250, 10, text="Taha hrac: "+str(hrac))
    canvas.create_text(250, 30, text='Pocet zapaliek: '+str(pocet_zapaliek))
def klavesy(event):
    global pocet_zapaliek, hrac
    cisla = [1,2,3]
    cislo = int(event.char)
    if cislo > pocet_zapaliek:
        return
    if cislo not in cisla:
        return
    pocet_zapaliek -= cislo
    if pocet_zapaliek == 0:
        canvas.delete("all")
        canvas.create_text(250, 100, text = "Hrac "+str(hrac)+ " vyhral!", fill= 'red', font='Arial 30')
        return
    if hrac == 1:
        hrac = 2
    else:
        hrac = 1
    vypis(hrac, pocet_zapaliek)



hrac = 1
pocet_zapaliek = 15
vypis(hrac, pocet_zapaliek)


canvas.bind_all("<Key>", klavesy)
canvas.mainloop()