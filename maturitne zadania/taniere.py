import tkinter
import random
c=tkinter.Canvas(width=870, height=150)
c.pack()
taniere = []
pismena = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
velkostTaniera = 80
x,y = 10,30
cislo = random.randint(0,9)
nespravne = set()

def jedenKus(x,y,index):
    global velkostTaniera
    c.create_oval(x,y,x+velkostTaniera, y+velkostTaniera, fill="blue", outline="darkblue")
    c.create_oval(x+10,y+10,x+velkostTaniera-10, y+velkostTaniera-10,outline="darkblue")
    c.create_text(x+velkostTaniera/2,y+velkostTaniera/2, text=pismena[index], fill="white",font=("Arial", 20, "bold"))

def klik(sur):
    global velkostTaniera,cislo, pismena, nespravne
    surx = sur.x
    sury = sur.y
    for i in taniere:
        if i[0]<=surx<=i[0]+velkostTaniera and i[1]<=sury<=i[1]+velkostTaniera:
            if cislo == i[2]:
                c.delete('all')
                c.create_text(435,50,text = "Gratulujem, stlacil si spravny tanier! "+pismena[cislo],fill="blue",font=("Arial", 30, "bold"))
                p = ''
                if nespravne:
                    for j in nespravne:
                        p = p + pismena[j]
                    c.create_text(435,100,text="Ty si stlacil viac krat: "+p,fill="red",font=("Arial", 30, "bold"))
            else:
                i[3]+=1
                if i[3]>2:
                    nespravne.add(i[2])
            break


for i in range(10):
    taniere.append([x,y,i,0])
    jedenKus(x,y,i)
    x +=85
    
c.bind("<Button-1>", klik)

c.mainloop()