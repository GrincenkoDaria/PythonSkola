import tkinter
c = tkinter.Canvas(width=300, height=300, background="white")
c.pack()
farba = "black"
velkost = 30
y = 0
x = 0
for i in range(10):
    c.create_line(0,y,300, y, fill = "lightgrey")
    c.create_line(x,0,x,300, fill = "lightgrey")
    x +=30
    y +=30

def ulF():
    global farba 
    farba = e.get()
    
def prefarbi(sur):
    sx = sur.x
    sy = sur.y
    x = sx//velkost*velkost
    y = sy//velkost*velkost
    c.create_rectangle(x, y,x+velkost, y+velkost, fill = farba, outline=farba)

e = tkinter.Entry()
e.pack()
b = tkinter.Button(text="Ulozit", command=ulF)
b.pack()
c.bind("<Button-1>", prefarbi)
c.mainloop()