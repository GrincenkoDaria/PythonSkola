subor = open("trasa_linky_metra.txt", "r")
farba = subor.readline().strip()
stanice = []
for i in subor:
    i = i.strip()
    if i[0]=="*":
        stanice.append([i[1:],'white'])
    else:
        stanice.append([i,farba])
import tkinter
pocet = len(stanice)
dlzka = pocet*70
print(pocet)
canvas = tkinter.Canvas(width=dlzka, height=200, bg="white")
canvas.pack()
x = 0
y = 175
canvas.create_line(10,180, 60*(pocet-1), 180, fill=farba, width=3)
for i in range(pocet):
    canvas.create_text(x+40,y-70,text = stanice[i][0], angle=60, font="Arial 10" )
    canvas.create_oval(x,y, x+10,y+10, fill=stanice[i][1],outline=farba)
    x += 60

canvas.create_rectangle(3,185,13,175, fill = farba, outline= farba)
canvas.create_rectangle(x-60,185,x-50,175, fill = farba, outline= farba)
canvas.mainloop()
subor.close()