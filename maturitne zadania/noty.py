import tkinter
vstup = open("noty.txt", "r")
riadok = vstup.readline()
dlzka = len(riadok)
osnovy = dlzka//19
if dlzka%19 > 0:
    osnovy+=1
    


#cdefgah

canvas = tkinter.Canvas(width=500, height=osnovy*70+40) 
canvas.pack()
y = 30

for i in range(osnovy):
    for i in range(4):
        canvas.create_line(10,y,490, y, fill = "#babbbd")
        y = y + 10
    y = y + 30

c = 70
d = 65
e = 60
f = 55
g = 50
a = 45
h = 40
x = 20 
plusy = 0
cislo = 0
for i in riadok:
    
    if i == "c":
        y = c
        color = "#ff0000"
    elif i == "d":
        y = d
        color = "#d98200"
    elif i == "e":
        y = e
        color = "#d9c300"
    elif i == "f":
        y = f
        color = "#50d900"
    elif i == "g":
        y = g
        color = "#00d9aa"
    elif i == "a":
        y = a
        color = "#0077d9"
    else:
        y = h
        color = "#ae00d9"
    canvas.create_oval(x+5 , y+5+plusy,x-5, y-5+plusy, width=2, outline = color)
    x += 25
    cislo +=1
    if cislo>18:
        x = 20
        plusy +=70
        cislo = 0

canvas.mainloop()