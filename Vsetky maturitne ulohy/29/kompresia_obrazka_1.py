vstup = open("kompresia_obrazka_1.txt", "r")
vystup = open("kompresia_obrazka_vystup.txt", "w")
riadok = vstup.readline()
vystup.write(riadok)
riadok = riadok.split()
sirka = int(riadok[0])
vyska = int(riadok[1])

def spracuj_riadok(i):
    i = i.strip()
    novy_riadok = ''
    nuly = 0
    jednotky = 0
    nula = True
    for j in i:
        if nula:
            if j == '1':
                jednotky += 1
                novy_riadok += str(nuly) + ' '
                nuly = 0
                nula = False
            else:
                nuly += 1
        else:
            if j == '0':
                nuly += 1
                novy_riadok += str(jednotky) + ' '
                jednotky = 0
                nula = True
            else:
                jednotky += 1
    if nula:
        novy_riadok +=str(nuly)
    else:
        novy_riadok +=str(jednotky)
    
    return novy_riadok

print(" Sirka obrazku je:", sirka, '\n', "Vyska obrazka je:", vyska, "\n", "Teda pocet pixelov obrazku je:", sirka*vyska)

for i in vstup:
    vystup.write(spracuj_riadok(i) + "\n")

vstup.close()
vystup.close()
