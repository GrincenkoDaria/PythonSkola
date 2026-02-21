subor = open("dekompresia_obrazka_1.txt", "r")
subor_out = open("dekompresia_obrazku_vystup.txt", "w")
riadok = subor.readline()
subor_out.write(riadok)
velkost = riadok.strip().split()
sirka = int(velkost[0])
vyska = int(velkost[1])


def spracuj_riadok(riadok):
    nula = True
    riadok = riadok.split()
    vystup = ''
    for i in riadok:
        for j in range(int(i)):
            
            if i == "0":
                nula = not nula
            if nula:
                vystup += "0"
            else: 
                vystup +="1"
        nula = not nula
    subor_out.write(vystup+'\n')

for riadok in subor:
    spracuj_riadok(riadok)
    
subor_out.close()
subor.close()