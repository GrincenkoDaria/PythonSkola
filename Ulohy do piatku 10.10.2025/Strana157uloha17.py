import tkinter
from random import *
c = tkinter.Canvas(width=600,height=400, bg='black')
xy =  open("x.txt", "r")
yy =  open("y.txt", "r")
c.pack()
#farebne pozadie
farby = ["#4C3702", "#5a0f2e", "#072f49","#084e38"]
for i in range(randint(3,5)):
    polomer = randint(100,200)
    x = randint(0,600)
    y = randint(0,400)
    c.create_oval(x+polomer, y +polomer, x-polomer, y-polomer, outline=choice(farby), width=40)
    c.update()
xcislo = xy.readline()
ycislo = yy.readline()
while xcislo != '' and ycislo != '':
    c.create_oval(int(xcislo), int(ycislo), int(xcislo)-20, int(ycislo)-20,width=5, outline="white")
    xcislo = xy.readline()
    ycislo = yy.readline()
    c.update()
    c.after(100)
xy.close()
yy.close()
c.mainloop() 