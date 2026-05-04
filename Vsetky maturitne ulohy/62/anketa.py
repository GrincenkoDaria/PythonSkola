import tkinter

subor = open("anketa.txt", "r", encoding="utf-8")
t = subor.readline()
udaje = list(map(int, subor.readline().split()))
subor.close()

canvas = tkinter.Canvas(width=300, height=200)
canvas.pack()

def kresli():
    canvas.delete("all")
    canvas.create_text(10, 20, text=t, anchor="w")

    spolu = sum(udaje)
    naj = max(udaje)

    odpovede = ["Áno", "Nie", "Neviem"]

    for i in range(3):
        y = 50 + i * 40
        if udaje[i] == naj:
            farba = "green"
        else:
            farba = "red"

        canvas.create_text(10, y, text=str(i+1) + ") " + odpovede[i] + " - " + str(udaje[i]), anchor="w")
        canvas.create_rectangle(100, y-10, 100 + udaje[i] / spolu * 100, y+10, fill=farba, outline="")

def zmen(sur):
    global udaje

    if 40 < sur.y < 70:
        udaje[0] += 1
    elif 80 < sur.y < 110:
        udaje[1] += 1
    elif 120 < sur.y < 150:
        udaje[2] += 1

    subor = open("anketa.txt", "w", encoding="utf-8")
    u = ""
    for i in udaje:
        u += str(i) + " "
    subor.write(t + u[:-1])
    subor.close()

    kresli()

canvas.bind("<Button-1>", zmen)

kresli()
canvas.mainloop()