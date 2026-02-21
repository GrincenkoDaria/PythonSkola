vstup = open("vstupny_text.txt", "r")
vystup = open("zasifrovany_text_2.txt", "w")

abeceda = "abcdefghijklmnopqrstuvwxyz"
posun = int(input("Zadaj posun: "))

novy_text = ""

for riadok in vstup:
    for i in riadok:
        if i in abeceda:
            index = (ord(i) - 97 + posun) % 26
            novy_text += chr(index + 97)
        else:
            novy_text += i

vystup.write(novy_text)

vstup.close()
vystup.close()