import tkinter
canvas = tkinter.Canvas(width=600, height=300, bg='white')
canvas.pack()
pocetradov = 10
VEL = 40
busx, busy = 50, 50
def zafarbi(sedadlo, farba):
    canvas.itemconfig('sedadlo_' + str(sedadlo), fill=farba)
def kresli(x, y, pocet):
    cislo = 0
    for i in range(pocet):
        for j in range(4):
            cislo += 1
            canvas.create_rectangle(x+i*VEL, y+j*VEL,
                x+(i+1)*VEL-10, y+(j+1)*VEL-10,
                tags='sedadlo_'+str(cislo), fill="lightgreen")
            canvas.create_text(x+i*VEL+VEL/2-5, y+j*VEL+VEL/2-5, text=cislo)
def klik(event):
    if (busx < event.x < busx + VEL * pocetradov and
        busy < event.y < busy + VEL * 4):
        ix = (event.x - busx) // VEL
        iy = (event.y - busy) // VEL
        sedadlo = ix * 4 + iy + 1
        zafarbi(sedadlo, 'red')
        print(sedadlo)
kresli(busx, busy, pocetradov)
canvas.bind('<Button-1>', klik)
canvas.mainloop()