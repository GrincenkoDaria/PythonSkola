import random 
vstup = open("poprehadzovany_text1_vstup.txt", 'r')
vystup = open("poprehadzovany_text1.txt", 'w')
def scrabled(riadok):
    hotovy_riadok = ''
    riadok = riadok.split()
    for i in riadok:
        if 0<len(i)<4 :
            hotovy_riadok += i + ' '

        else:
            prve_pismeno= i[0]
            posledne_pismeno = i[-1]
            i= list(i[1:-1])
            random.shuffle(i)
            stred = ''
            for j in i:
                stred += j 
            hotovy_riadok += prve_pismeno+ stred + posledne_pismeno + ' '
            
    return hotovy_riadok + '\n'

for i in vstup:
    vystup.write(scrabled(i))
    
vstup.close()
vystup.close()