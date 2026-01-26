vstup = open("poprehadzovany_text_vstup2.txt", "r")
vystup = open("poprehadzovany_text.txt", "w")
import random
def pomiesaj(retazec):
    pismenka = list(retazec)
    random.shuffle(pismenka)
    return ''.join(pismenka)
znaky = '.,!?():#@~[]0123456789<>{}^%*-+/\\'
def pis(riadok):
    riadok = riadok.split()
    novy_riadok = ''
    for i in riadok:
        znak1 = ""
        znak2 = ''
        if i[0] in znaky:
            znak1 = i[0]
            prve_pismeno = i[1]
            retazec = i[2:]
        else:
            prve_pismeno = i[0]
            retazec = i[1:]
        if i[-1] in znaky:
            znak2 = i[-1]
            posledne_pismeno = i[-2]
            retazec = i[1:-2]
        else:
            posledne_pismeno = i[-1]
            retazec = i[1:-1]
        print(znak1 , prve_pismeno,pomiesaj(retazec),posledne_pismeno,znak2)
        novy_riadok += znak1 + prve_pismeno+pomiesaj(retazec)+posledne_pismeno+znak2 + ' '
    return novy_riadok + "\n"
"""def ocisti_slovo(slovo):
    ciste_slovo = ''
    zly_zaciatok = ""
    zly_koniec = ''
    i = 0 
    while i < slovo[i] in vynechat:
        zly_zaciatok +=slovo[1]
        i+=1
    while i < len(slovo) and not (slovo[i] in vynechat):
        ciste_slovo += slovo[i]
        i+=1
    zly_koniec = slovo[1:]
    return zly_zaciatok, ciste_slovo, zly_koniec"""
for riadok in vstup:
    vystup.write(pis(riadok))

vstup.close()
vystup.close()


