import tkinter
from random import *
c = tkinter.Canvas(width=600,height=400, bg='black')
c.pack()
vyska=()
for i in range(9):
        vyska = vyska+ (randint(50,300),) 
def ekvalizer():
    c.delete("all")
    global vyska
    farba = "#07ff00"
    c.create_text(300,350,text=" 31  62  125  250  500  1K  2K  8K  16K   [Hz]", fill=farba, font="Helvetica 19 bold" )
    x=50
    y=320
    vyskateraz = ()
    for i in range(9):
        cislo = vyska[i] + randint(-30,30)
        if cislo < 10:
             cislo = 10
        elif cislo > 350:
             cislo = 350
        vyskateraz = vyskateraz+(cislo,)
        c.create_rectangle(x*(i+1),y,x*(i+1)+30,vyskateraz[i], fill = farba, outline = farba)
    
    
    c.after(100,ekvalizer)
    

ekvalizer()
c.mainloop()