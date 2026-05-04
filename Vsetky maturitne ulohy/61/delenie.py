import tkinter, random
canvas = tkinter.Canvas(width=600, height= 150, bg = "white")
canvas.pack()
delenec = random.randint(11,20)
delitel = random.randint(2,9)
farby = ["green", "blue", "red"]
zvysokF = 'yellow'

canvas.create_text(80,40, text =(str(delenec)+" : "+str(delitel)+" ="), font = "Arial 30")
def over():
    odpoved = int(entry.get())
    if odpoved==delenec//delitel:
        t = "SPRAVNE"
    else:
        t = "NESPRAVNE"
    canvas.create_text(130,90, text =t, font = "Arial 30" )
    x = 15
    y = 120
    for i in range(delenec//delitel):
        farba = farby[i%len(farby)]
        for j in range(delitel):
            canvas.create_oval(x,y,x+20,y+20, fill = farba, outline="")
            x += 25
    x +=25
    for i in range(delenec%delitel):
        canvas.create_oval(x,y,x+20,y+20, fill = zvysokF, outline="")
        x += 25

entry = tkinter.Entry()
entry.pack()
button = tkinter.Button(text="Over", command=over)
button.pack()


canvas.mainloop()