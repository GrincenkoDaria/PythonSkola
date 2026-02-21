import random
vstup = open("virus.txt", "r")
vystup = open("virus_vystup.txt", "w")
nove_poradie = []
novy_riadok = []
riadky = []
TF = [True, False]

def nahoda():
    odpoved = random.choice(TF)
    return odpoved

for i in vstup:
    print(i, end = '')
    riadky.append(i)

if nahoda():
    random.shuffle(riadky)

for i in riadky:
    i = i.split()
    for j in i:
        if nahoda():
            j = j[::-1]

            
        novy_riadok.append(j)
    if nahoda():
        random.shuffle(novy_riadok)
    nove_poradie.append(" ".join(novy_riadok))
    novy_riadok = []
        
        
for q in nove_poradie:
    vystup.write(q + '\n')




vstup.close()
vystup.close()