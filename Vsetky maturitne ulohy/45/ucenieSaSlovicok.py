subor=open('subory/ucenie_sa_slovicok.txt','r')
slovicka=subor.readlines()
sk=slovicka[::2]
en=slovicka[1::2]
subor.close()
jazyk=input('Ak ti mám zadávať slovenské slová zadaj A')
slovenske=jazyk='A'
a,b=en[:],sk[:]
if slovenske:
    a,b=b,a

zle=0
while len(a)>0:
    slovo1=a.pop(0).strip()
    slovo2=b.pop(0).strip()
    odpoved=input('Zadaj preklad slova '+slovo1+':')
    if odpoved!=slovo2:
        a.append(slovo1)
        b.append(slovo2)
        zle+=1
        print('Nesprávne')
    else:
        print('Správne')
print('Počet nesprpávnych odpovedí:' +str(zle))
