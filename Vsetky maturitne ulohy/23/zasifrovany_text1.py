kluc = input('Zadaj sifrovaci kluc ')
dlzka_kluca = len(kluc)
vstup = input('Zadaj textovy retazec ').strip()
dlzka_vstupu = len(vstup)
prilozeny_kluc = dlzka_vstupu //dlzka_kluca * kluc + kluc[:dlzka_vstupu % dlzka_kluca]
vystup = ''
posuny = ''
for i in range(dlzka_vstupu):
    if vstup[i] == ' ':
        vystup += " "
        posun = "-"
        print(posun)
    else:
        posun = ord(prilozeny_kluc[i]) - 96
        
        vystup += chr(posun + ord(vstup[i]))
    posuny += str(posun)

print('vstup: ', vstup)
print('kľúč: ', kluc)
print('priložený kľúč: ', prilozeny_kluc) 
print('posun:  ', posuny)
print('výstup: ', vystup)
    
    