import tkinter as tk

def Canvas2Radiobutton():
    okno2 = tk.Toplevel(root)
    okno2.title("Radiobutton")

    canvas2 = tk.Canvas(okno2, width=400, height=300, bg = "#f0aeae")
    canvas2.pack(padx=10, pady=10)
    v = tk.IntVar()
    radiobutton1 = tk.Radiobutton(okno2,text='kruh', variable=v, value=1)
    radiobutton1.pack()
    radiobutton2 = tk.Radiobutton(okno2,text='štvorec', variable=v, value=2)
    radiobutton2.pack()
    radiobutton3 = tk.Radiobutton(okno2,text='čiara', variable=v, value=3)
    radiobutton3.pack()
    radiobutton4 = tk.Radiobutton(okno2,text='text', variable=v, value=4)
    radiobutton4.pack()
    def klik(sur):
        typ = v.get()
        if typ == 1:
            canvas2.create_oval(sur.x-10, sur.y-10, sur.x+10, sur.y+10)
        if typ == 2:
            canvas2.create_rectangle(sur.x-10, sur.y-10, sur.x+10, sur.y+10)
        if typ == 3:
            canvas2.create_line(sur.x-10, sur.y, sur.x+10, sur.y)
        if typ == 4:
            canvas2.create_text(sur.x, sur.y, text='['+str(sur.x)+','+str(sur.y)+']')
    canvas2.bind('<Button-1>', klik)
def Canvas3Scale():
    okno3 = tk.Toplevel(root)
    okno3.title("Scale")

    canvas3 = tk.Canvas(okno3, width=400, height=300, bg = "#f0dbae")
    canvas3.pack(padx=10, pady=10)
    rx, ry = 100, 50
    x, y = 200, 100
    canvas3.create_oval(x-rx, y-ry, x+rx, y+ry, width=5, outline="#f8b629",tags='oval')
    def zmena1(val):
        global rx
        rx = scale1.get()
        prekresli()
    def zmena2(val):
        global ry
        ry = scale2.get()
        prekresli()
    def prekresli():
        global rx, ry
        canvas3.coords('oval',[x-rx, y-ry, x+rx, y+ry])

    scale1 = tk.Scale(okno3,from_=10, to=200, orient='horizontal',length=400, command=zmena1)
    scale1.pack()
        
    scale1.set(rx)
    scale2 = tk.Scale(okno3,from_=10, to=100, orient='vertical',length=200, command=zmena2)
    scale2.place(x=380, y=0)
    scale2.set(ry)
def Canvas4Checkbutton():
    okno4 = tk.Toplevel(root)
    okno4.title("Checkbutton")
    okno4.configure(bg="#ecf0ae")

    label1 = tk.Label(okno4, text='Z ktorého predmetu idete maturovať?')
    label1.pack(pady=(20, 10))

    predmet1 = tk.StringVar()
    predmet2 = tk.StringVar()
    predmet3 = tk.StringVar()

    def vypis():
        predmety = predmet1.get() + ' ' + predmet2.get() + ' ' + predmet3.get()
        predmety = predmety.strip()
        if predmety:
            vysledok.config(text="Vybrané predmety: "+predmety)
        else:
            vysledok.config(text=None)
    checkbutton1 = tk.Checkbutton(okno4, text='slovenský jazyk a literatúra',onvalue='SJL', offvalue='', variable=predmet1,command=vypis)
    checkbutton1.pack(padx=30)
    checkbutton2 = tk.Checkbutton(okno4, text='anglický jazyk',onvalue='AJ', offvalue='', variable=predmet2,command=vypis)
    checkbutton2.pack(padx=30)
    checkbutton3 = tk.Checkbutton(okno4, text='nemecký jazyk',onvalue='NJ', offvalue='', variable=predmet3,command=vypis)
    checkbutton3.pack(padx=30)
    vysledok = tk.Label(okno4, text=None)
    vysledok.pack(pady=20)
def Canvas5Scrollbar():
    okno5 = tk.Toplevel(root)
    okno5.title("Scrollbar")
    okno5.configure(bg="#c6f0ae")  
    frame = tk.Frame(okno5)
    frame.pack(padx=10, pady=10, fill="both", expand=True)
    scroll_bar = tk.Scrollbar(frame)
    scroll_bar.pack(side="right")
    mylist = tk.Listbox(frame, width=25, height=15)
    mylist.pack()
    for i in range(30):
        mylist.insert(tk.END, str(i))
    scroll_bar.config(command=mylist.yview)
def Canvas6Listbox():
    okno6 = tk.Toplevel(root)
    okno6.title("Listbox")

    canvas6 = tk.Canvas(okno6, width=400, height=300, bg = "#aef0e7")
    canvas6.pack(padx=10, pady=10)
    def prefarbi(event):
        oznacene = listbox1.curselection()
        canvas6['bg'] = listbox1.get(oznacene)
    def pridaj():
        listbox1.insert('end', entry1.get())
    def vymaz():
        oznacene = listbox1.curselection()
        if len(oznacene) == 1:
            listbox1.delete(oznacene)
    listbox1 = tk.Listbox(canvas6)
    listbox1.pack()
    farby = ["#2227bf","#2273bf","#7b7caf","#c1c2f0","#22b2bf","#0a2245",]
    for prvok in farby:
        listbox1.insert('end', prvok)
        listbox1.bind('<Double-Button-1>', prefarbi)
    label1 = tk.Label(canvas6,text='Napíš názov farby:')
    label1.pack()
    entry1 = tk.Entry(canvas6)
    entry1.pack()
    button1 = tk.Button(canvas6,text='Pridaj farbu', command=pridaj)
    button1.pack()
    button2 = tk.Button(canvas6,text='Vymaž označenú farbu', command=vymaz)
    button2.pack()
def Canvas7Progressbar():
    from tkinter import ttk
    okno7 = tk.Toplevel(root)
    okno7.title("Progressbar")
    canvas7 = tk.Canvas(okno7, bg="#e4aef0")
    canvas7.pack(fill="both", expand=True, padx=10, pady=10)
    style = ttk.Style()
    style.theme_use('default')
    style.configure("purple.Horizontal.TProgressbar",background="#6b087b")
    progressbar = ttk.Progressbar(canvas7, style="purple.Horizontal.TProgressbar", mode="indeterminate")
    progressbar.pack()

    def zacat():
        progressbar.start(10)
          
    button = tk.Button(canvas7, text="Download", command=zacat)
    button.pack()
    
#hlavne okno
root = tk.Tk()
root.title("Hlavne okno")
00
#vytvorime menu 
menu_bar = tk.Menu(root)
root.config(menu= menu_bar)

#pridame menu polozku "Zobrazit"
zobrazit_menu = tk.Menu(menu_bar, tearoff = 0)
menu_bar.add_cascade(label="Zobrazit", menu = zobrazit_menu)
#polozka, krota otvori nove okno s Canvasom
zobrazit_menu.add_command(label="Radiobutton", command=Canvas2Radiobutton)
zobrazit_menu.add_command(label="Scale", command=Canvas3Scale)
zobrazit_menu.add_command(label="Checkbutton", command=Canvas4Checkbutton)
zobrazit_menu.add_command(label="Scrollbar", command=Canvas5Scrollbar)
zobrazit_menu.add_command(label="Listbox", command=Canvas6Listbox)
zobrazit_menu.add_command(label="Progressbar", command=Canvas7Progressbar)
#hlavny canvas v hlavnom okne 
canvas1 = tk.Canvas(root, width=400, height=300, bg = "white")
canvas1.pack(padx=10, pady=10)
canvas1.create_text(200, 250, text = "Vyber si co chces vidiet", font=("Arial", 14, "bold"))
canvas1.create_line(200,230, 40,25, width=3)
canvas1.create_line(60,35,40,25,45,45, width=2)

canvas1.mainloop()