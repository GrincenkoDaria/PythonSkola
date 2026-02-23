import random
subory =[]
for i in range(5220,5230):
    s = open(str(i)+".txt", "w")
    subory.append(s)

vstup = open("hlasovanie_1.txt", "r")
poradie = 0
for r in vstup:
    poradie +=1
    cislo = int(r.strip())
    subory[cislo - 5220].write(str(poradie)+"\n")

for s in subory:
    s.close()

print("Celkovy pocet SMS bol: ", poradie)

vstup.close()