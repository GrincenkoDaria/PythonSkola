vstup = open('spokojnost_1.txt', 'r')
pocet = 0
sphodiny = [0]*24
nshodiny = [0]*24
for i in vstup:
    pocet +=1
    if i.strip()[-1]=="o":
        sphodiny[int(i[:2])] +=1
    else:
        nshodiny[int(i[:2])] +=1
print(pocet, "zakaznikov sa vijadrilo")
print("Najviac spokojni klienti boli o", sphodiny.index(max(sphodiny)))
print("Najviac nespokojni klienti boli o", nshodiny.index(max(nshodiny)))

precenta =[]
celok = 0
for i in range(len(sphodiny)):
    if sphodiny[i]!=0:
        precenta.append([i, sphodiny[i]])
        celok += sphodiny[i]

vysledok = ''
for i in precenta:
    vysledok += str(i[0])+". "+str(round(i[1]/celok*100, 2))+"% "
print("Precenta spokojnych zakaznikov po hodinam "+vysledok.strip())














vstup.close()