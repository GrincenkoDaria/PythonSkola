import tkinter

canvas = tkinter.Canvas(width=800, height=300, background="white")
canvas.pack()

entry1 = tkinter.Entry()
entry1.pack()

def vykresli():
    canvas.delete("all")

    vstup = open("zastavba_na_ulici.txt", "r")
    limit = int(entry1.get())

    y_base = 200
    x = 10

    vyska2 = None 

    for riadok in vstup:
        vyska, sirka = map(int, riadok.split())

        if vyska > 0:
            canvas.create_rectangle(
                x, y_base - vyska,
                x + sirka, y_base,
                fill="grey", outline="black"
            )
        else:
            # --- voľné miesto ---
            canvas.create_line(
                x, y_base,
                x + sirka, y_base,
                fill="green", width=4
            )

        if vyska2 is not None:
            if vyska != 0 and vyska2 != 0:
                if abs(vyska - vyska2) > limit:
                    canvas.create_line(
                        x, y_base - vyska2,
                        x, y_base - vyska,
                        fill="red", width=3
                    )

        vyska2 = vyska
        x += sirka

    vstup.close()


button = tkinter.Button(text="Vykresli", command=vykresli)
button.pack()

canvas.mainloop()