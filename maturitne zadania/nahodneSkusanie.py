import random
def chyba(z,o):
    if z>o:
        print("Pocet ziakov je vatcsi ako otazok")
        o = int(input("Zadaj pocet otazok:"))
        chyba(z,o)
def skuskaParnosti(parne, otazkaCislo):
    if parne:
        if otazkaCislo%2 != 0:
            otazkaCislo = random.choice(otazky)
            skuska(parne,otazkaCislo)
    else: 
        if otazkaCislo%2 == 0:
            otazkaCislo = random.choice(otazky)
            skuska(parne,otazkaCislo)
def pridaj(c,cislo):
    for i in range(c):
        cislo.append(i+1)

    print(cislo)
z = int(input("Zadaj pocet studentov:"))
o = int(input("Zadaj pocet otazok:"))
ziaci =[]
otazky = []
chyba(z,o)
pridaj(z,ziaci)
pridaj(o,otazky)
dlzka = len(ziaci)
parne = True
for i in range(dlzka):
    ziakCislo = random.choice(ziaci)
    ziaci.remove(ziakCislo)
    otazkaCislo = random.choice(otazky)
    #skuskaParnosti(parne,otazkaCislo)
    otazky.remove(otazkaCislo)
    print(i+1,". student: ", ziakCislo,", otazka:", otazkaCislo)