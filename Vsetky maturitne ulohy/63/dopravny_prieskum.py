subor = open("dopravny_prieskum.txt", "r", encoding="utf-8")
zastavky = []
pocet = 0
maxpocet = 0
for riadok in subor:
    casti =  riadok.split(";")
    nastup = int(casti[0])
    vystup = int(casti[1])
    pocet += nastup
    pocet -= vystup
    maxpocet= max(maxpocet, pocet)
    zastavky.append((casti[2].strip(),pocet, pocet>=10, nastup<3 and vystup<3))
subor.close()
print("Zoznam zastavok a pocet cestujucich")
for zastavka in zastavky:

    print(zastavka[0], '-', zastavka[1])
print("Odporucany typ elektircky: ")
if maxpocet>100:
    print("dlha")
elif maxpocet>50:
    print("standartna")
else:
    print("kratka")


print("Zastavky s automatom:")
for i in zastavky:
    if i[2]:
        print(i[0])

print("Zastavky naznamenie: ")
for i in zastavky:
    if i[3]:
        print(i[0])