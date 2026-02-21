vstup = open("hlasovanie_1.txt", 'r')
vystup = open("hlasovanie_vypadnuti.txt", "w")
pocet_SMS = 0
pocet_kazdy = [0] * 10
dalej = []

for i in vstup:
    pocet_SMS += 1
    i = i.strip()
    pocet_kazdy[int(i[-1])] += 1

for i in range(len(pocet_kazdy)):
    if pocet_kazdy[i] != 0:
        dalej.append([i,pocet_kazdy[i]])
print(pocet_kazdy)
print(dalej)
najvatsie = 0
for i in dalej:
    if i[1]>najvatsie:
        najvatsie = i[1]
    
dalej = [x for x in dalej if x[1] != najvatsie]
for i in dalej:
    vystup.write("522"+str(i[0]) + "\n")


print(pocet_SMS)