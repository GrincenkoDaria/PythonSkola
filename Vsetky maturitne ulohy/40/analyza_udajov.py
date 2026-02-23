vstup = open("spokojnost_1.txt", "r")
pocet = 0
hodiny = [0] * 24
dni = []
aktualny_den_pocet = 0

predchadzajuci_cas = "00:00"

for riadok in vstup:
    riadok = riadok.strip()
    info = riadok.split()
    cas = info[0]

    hodina = int(cas.split(":")[0])

    pocet += 1
    aktualny_den_pocet += 1
    hodiny[hodina] += 1

    if cas < predchadzajuci_cas:
        dni.append(aktualny_den_pocet - 1)
        aktualny_den_pocet = 1

    predchadzajuci_cas = cas

dni.append(aktualny_den_pocet)

vstup.close()

for i in range(len(dni)):
    print(str(i + 1) + ". deň - počet reakcií:" + str(dni[i]))

print("Počet všetkých vyjadrení:", pocet)

for i in range(24):
    if hodiny[i] > 0:
        print("Hodina:", i, "Reakcií zákazníkov:", hodiny[i])

print("Počet dní:", len(dni))