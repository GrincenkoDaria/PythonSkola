def spracuj_riadok(vstup):
    pocet = len(vstup)//2
    vystup = ""
    for i in range(pocet):
        odtien = vstup[i*2:i*2+2]
        farba = "0"
        if odtien >"7f":
            farba ="1"
        vystup += farba +' '
    vystup = vystup[:-1] + "\n"
    return vystup
    
subor = open("ciernobiely_obrazok_1.txt", "r")
subor_out = open("konverzia.txt", "w")
riadok = subor.readline()
velkost = riadok.strip().split()
sirka = int(velkost[0])
vyska = int(velkost[1])
subor_out.write(riadok)
print("obrazok ma rozmery {}x{} bodov".format(sirka,vyska))
print("obrazok ma {} pixelov".format(sirka*vyska))
riadok = subor.readline()
print(repr(riadok))

spracovanie = spracuj_riadok(riadok)
print(repr(spracovanie))

subor_out.write(spracovanie)
for riadok in subor:
    subor_out.write(spracuj_riadok(riadok))
subor.close()
subor_out.close()



