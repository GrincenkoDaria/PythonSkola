import tkinter
vstup = open('spokojnost_1.txt', 'r')
pocetnespok = 0
sphodiny = [0]*24
nshodiny = [0]*24
for i in vstup:

    if i.strip()[-1]=="o":
        sphodiny[int(i[:2])] +=1
    else:
        nshodiny[int(i[:2])] +=1
        pocetnespok+=1
print(pocetnespok, "nespokojnych zakaznikov")
print("Najviac nespokojni klienti boli o", nshodiny.index(max(nshodiny)), "a ich bolo",max(nshodiny))

print("Pocet nespokojnych zakaznikov po hodinam: ")

canvas = tkinter.Canvas(width=480, height=520, bg = "white")
canvas.pack()

x = 10
y = 510

for i in range(24):
    if i<10:
        text = "0"+str(i)
    else:
        text = str(i)
    canvas.create_text(x,y,text=text, fill ="red", font="Arial 10")
    x+=20
x = 2
y = 500
for i in range(len(nshodiny)):
    if nshodiny[i] != 0:
        print(str(i)+". "+str(nshodiny[i]))
    canvas.create_rectangle(x,y,x+18,y-20*nshodiny[i], fill="red")
    x+=20
print()
        

canvas.mainloop()








vstup.close()