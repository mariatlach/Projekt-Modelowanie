import functions

functions.popupth('fotokom.txt', "Wyjasnienie")
print('Czy chciał*bys wyswietlic bibliografie?')
bibl = str(input())
if bibl == 'tak' or bibl == 'TAK' or bibl =='Tak':
    functions.popupth('bibliografia.txt', "Bibliografia")
