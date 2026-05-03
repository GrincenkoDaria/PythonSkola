import tkinter, random
c = tkinter.Canvas(width=420, height=400)
c.pack()
def nova_hra():
    global pismeno, vx, vy
    vx, vy = random.randint(20, 400), 0
    pismeno = chr(random.randrange(26)+97)
    
pismeno = ''
vx, vy = 0,0

def prekresli(vidiet):
    c.delete('all')
    c.create_oval(vx-10, vy-20, vx+10,vy+20, tags = 'vajicko')
    if vidiet:
        c.create_text(vx, vy, text= pismeno, font='Arial 20', tags="vajicko")

def padanie():
    global vy
    vy+=10
    vidiet = vy>400-400//3
    prekresli(vidiet)
    if vy <400:
        c.after(100, padanie)


def klaves(event):
    if event.char == pismeno:
        nova_hra()

nova_hra()
padanie()
c.bind_all('<Key>', klaves)
c.mainloop()