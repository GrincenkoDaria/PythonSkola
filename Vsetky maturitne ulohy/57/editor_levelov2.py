import tkinter
c = tkinter.Canvas(width=300, height=300, background="white")
c.pack()
farba = "blue"
v_farba = "lightgreen"
vyznacene = False
x = 0
y = 0
velkost = 30
for i in range(10):
    c.create_line(0,y,300,y, fill = "grey")
    c.create_line(x,0,x,300, fill = "grey")
    x += velkost
    y += velkost

def kresli(sur):
    c.delete("v")
    global vyznacene, zaciatokX,zaciatokY
    sx = sur.x
    sy = sur.y
    x = sx//velkost*velkost
    y = sy// velkost*velkost
    if vyznacene:
        if zaciatokX == x or zaciatokY == y:
            if zaciatokX>x :
                c.create_rectangle(x, zaciatokY,zaciatokX+velkost, y + velkost, fill=farba, outline=farba)
            if zaciatokY>y :
                c.create_rectangle(zaciatokX, y,x+velkost, zaciatokY+velkost, fill=farba, outline=farba)
            else:
                c.create_rectangle(zaciatokX, zaciatokY,x+velkost, y + velkost, fill=farba, outline=farba)
            vyznacene = False
        else:
            c.create_rectangle(x,y,x+velkost,y+velkost, fill = v_farba, outline= "black", tags="v")

            vyznacene =  True
            zaciatokX = x
            zaciatokY = y
    else:
        c.create_rectangle(x,y,x+velkost,y+velkost, fill = v_farba, outline= "black", tags="v")
        vyznacene =  True
        zaciatokX = x
        zaciatokY = y
        
c.bind("<Button-1>", kresli)
c.mainloop()