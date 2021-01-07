import functions

functions.popupth('fotokom.txt', "Wyjasnienie")

functions.popupth('program.txt', "Działanie programu")

functions.wykresy()

functions.animacja()

functions.obrazki()

print("Czy chcesz wyświetlić, którąś z bibliotek?")
bibl1 = str(input())
bibl1 = bibl1.lower()
if bibl1 == 'tak':
    print("Jeśli chcesz wyświetlić bibliotekę metali wpisz: 'metale', jeśli częstotliwości promieniowań, wpisz: 'fale'; Jeżeli chcesz wyświtlić obie biblioteki, wpisz 'obie'")
    ktora = str(input())
    if ktora == 'metale':
        functions.popupth('bibliotekametalenice.txt', "Biblioteka prac wyjścia dla wybranych metali:")
    elif ktora == 'fale':
        functions.popupth('bibliotekafale.txt', "Biblioteka długości fal dla odpowiednich promieniowań:")
    elif ktora == 'obie':
        functions.popupth('bibliotekametalenice.txt', "Biblioteka prac wyjścia dla wybranych metali:")
        functions.popupth('bibliotekafale.txt', "Biblioteka cdługości fal dla odpowiednich promieniowań:")
functions.zjawisko(1)

print('Czy chciał*bys wyswietlic bibliografie?')
bibl = str(input())
bibl = bibl.lower()
if bibl == 'tak':
    functions.popupth('bibliografia.txt', "Bibliografia")