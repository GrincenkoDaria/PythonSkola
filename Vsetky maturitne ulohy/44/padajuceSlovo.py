import tkinter, random
canvas=tkinter.Canvas(width=420, height=400)
canvas.pack()

slova=('qqqqqqq',"qqqwwwweeee")
def nova_hra():
    global vx,vy,uhadnute,slovo
    vx,vy=random.randint(100,300),0
    slovo=slova[random.randrange(len(slova))]
    uhadnute='*'*len(slovo)

def prekresli():
    canvas.delete('slovo')
    canvas.create_text(vx,vy,text=uhadnute,font='Arial 20',anchor='nw',tags='slovo')
    
def padanie():
    global vy
    vy+=5
    prekresli()
    if vy<400 and uhadnute!=slovo:
        canvas.after(500,padanie)
    elif uhadnute!=slovo:
        canvas.create_text(200,200,text='Neuhádol si')
def klaves(event):
    global uhadnute
    if event.char in slovo and not event.char in uhadnute:
        nove_uhadnute=''
        for znak in slovo:
            if znak in uhadnute or znak==event.char:
                nove_uhadnute+=znak
            else:
                nove_uhadnute+='*'
        uhadnute=nove_uhadnute
                
slovo=''
uhadnute=''
vx,vy=0,0


nova_hra()
padanie()
canvas.bind_all('<Key>',klaves)
canvas.mainloop()