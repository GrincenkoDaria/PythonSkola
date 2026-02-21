import random 
vstup = open("loteria_1.txt", "r")
vstup_od_ucasnika = input("Zadaj 6 cisel: ")

od_ucasnika = []
for i in vstup_od_ucasnika.split():
        od_ucasnika.append(int(i))
        
cisla_osob =[]
for riadok in vstup:
    osoba = []
    for i in riadok.split():
        osoba.append(int(i))
    cisla_osob.append(osoba)
    
vstup.close()

cisla = []
for i in range(1,50):
    cisla.append(i)
random.shuffle(cisla)
vyzrebovane = cisla[:6]
print(vyzrebovane)

def porovnovanie(a,b):
    pocet = 0
    text = ""
    for i in a:
        if i in b:
            text += str(i)+ " "
            pocet += 1
    return text.strip(), str(pocet)
text, pocet = porovnovanie(od_ucasnika, vyzrebovane)
print("Mas:", text, "(uhádnute cisla:", pocet, ")")

pocet_uhadnuti = {1:0, 2:0, 3:0, 5:0, 6:0}
for a in cisla_osob:
    text, pocet = porovnovanie(a, vyzrebovane)
    if pocet in pocet_uhadnuti:
        pocet_uhadnuti[pocet] += 1

print("Počet účastníkov, ktorí uhádli:")
print("1 číslo:", pocet_uhadnuti[1])
print("2 čísla: ", pocet_uhadnuti[2])
print("3 čísla: ", pocet_uhadnuti[3])
print("5 čísiel:", pocet_uhadnuti[5])
print("6 čísiel:", pocet_uhadnuti[6])
