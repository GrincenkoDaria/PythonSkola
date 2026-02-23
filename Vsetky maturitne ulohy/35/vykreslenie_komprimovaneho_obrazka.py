vstup = open("komprimovany_obrazok_1.txt", "r")
velkosti = vstup.readline().split()
sirka = int(velkosti[0])
vyska = int(velkosti[1])

import tkinter
canvas = tkinter.Canvas(width=sirka, height=vyska, bg = "white")
canvas.pack()

y = 0
def cb(c):
    canvas.delete("all")
    vstup = open("komprimovany_obrazok_1.txt", "r")
    riadok = vstup.readline()
    y = 0
    for riadok in vstup:
        riadok = riadok.split()
        x = 0 
        for i in riadok:
            if c :
                farba = "black"
            else:
                farba ="white"
            canvas.create_rectangle(x,y,x+int(i),y+1, fill=farba, outline='')
            x += int(i)
            c = not c
        canvas.update()
        y +=1
    vstup.close()

c = True
def opacne():
    global c
    c = not c
    cb(c)



button  = tkinter.Button(text="Opacne", command=opacne)
button.pack()
cb(c)
canvas.mainloop()