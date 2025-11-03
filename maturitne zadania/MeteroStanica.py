vstup = open("meterostanice.txt", "r")
teploty = []
pocet = 0
teplotaMax = 0
spolu = 0
for riadok in vstup:
    pocet +=1
    if riadok[21] == '+':
        teplota = float(riadok[22:26].replace(",", "."))
    else:
        teplota = -1*float(riadok[22:26].replace(",", "."))
    if teplotaMax < teplota:
        teplotaMax = teplota
        stanica = riadok[0:3]
    spolu = spolu + teplota
    teploty.append(teplota)  
print("Pocet merani bol:", pocet)
print("Merane teploty:",teploty)
print("Maksimalna teplota:",max(teploty),", ktora bola merana na stanici:", stanica)
print("Priemerna teplota:", round(spolu/pocet,2))
vstup.close()