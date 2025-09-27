print("Vymysli nahodne cislo")
od = int(input("Zadaj interval, v ktorom sa nachadza tvoje cislo. od "))
do = int(input("do "))
cislo = od+(do - od)//2 # cislo uprostred intervalu

"""ozaj = input("tak ake cislo si si vymysliel? ")
if ozaj.isdigit(): #kontrola ci odpoved bola v cislicach
    print("Ozaj? Som myslela, ze to bude trvat dlhsie")"""

print("Dalej ak tvoje cislo bude vatsie ako to ktore ti ukazem pis V ako mensie M alebo JE ked uhadnem")

while True:
    if od>do: #aby cislo neslo za hranice intervalu 
        print("asi niekde doslo ku chybe")
        break
    print("Tvoje cislo je " + str(cislo) + "?")
    odpoved = input()
    
    if odpoved == "M":
        do = cislo - 1 # cislo je urcite mensie ako to co bolo pred tym preto zmensime hranice intervalu
        cislo = od + (do - od)//2  

    elif odpoved == "V":
        od = cislo + 1 # tak isto ako hore iba z opacneho konca intervalu
        cislo = od + (do - od)//2   
    elif odpoved == "JE":
        print("Nasli sme, tvoje cislo je: " + str(cislo))
        break
