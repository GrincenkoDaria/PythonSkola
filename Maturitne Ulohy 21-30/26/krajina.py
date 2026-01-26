import tkinter
import random
width=500
height=300
c = tkinter.Canvas(width=width, height=height, bg = 'lightblue')
c.pack()
zelena = ["#3bb133","#306c45","#0e7b0e","#02531E","#01ff5a"]

def vykresli():
    suradnice = [500,300,0,300,0, random.randint(150,250)]
    smer = random.choice([1,-1])
    vrcholX = random.randint(100,400)
    for i in range(vrcholX // 10):
        suradnice.append((i+1)*10)
        suradnice.append(suradnice[-2] + smer * random.randint(0, 5))
    smer = -1 *smer
    for i in range((500-vrcholX) // 10 + 10):
        suradnice.append((i+1)*10+vrcholX)
        suradnice.append(suradnice[-2] + smer * random.randint(0, 5))
    
    c.create_polygon(suradnice, fill= random.choice(zelena),outline="black")
    
def stlac(event):
    c.delete('all')
    for i in range(5):
        vykresli()

c.bind_all('<space>', stlac)
c.mainloop()