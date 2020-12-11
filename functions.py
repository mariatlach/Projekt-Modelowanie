import ctypes
import codecs
import ast
import math

def popupth(nazwa, tytul):
    # tutaj jest mala funkcja ktora otwiera nasze okienko z wyjasnieniem Z POLSKIMI ZNAKAMI :))))))
    popup = ''
    with codecs.open(nazwa, encoding='utf-8') as f:
        for line in f:
            popup = popup + line
    ctypes.windll.user32.MessageBoxW(0, popup, tytul, 1)
def zjawisko():
    with open("bibliotekametale.txt", "r") as data:
        bibliotekam = ast.literal_eval(data.read())
    while True:
        try:
            nazwam1 = dajmetal()
            Wev = float(bibliotekam[nazwam1])
            # print(bibliotekam[nazwam1])
        except KeyError:
            print("Podanego metalu nie ma w bibliotece bądź jego nazwa została wprowadzona niepoprawnie; Spróbuj jeszcze raz:")
            #nazwam1 = dajmetal()
            continue
        break
    while True:
        try:
            dlugosc = dajfale()
            # print(dlugosc)
        except ValueError:
            print("Wpisz wartość liczbową")
            #dlugosc = dajfale()
            continue
        break


    # lewa strona rownania:
    c = 2.9979 * 10 ** 8
    f = c / (dlugosc * 10 ** (-9))
    h = float(6.63 * 10 ** (-34))
    foton = h * f
    # print(foton)

    # prawa strona rownania:
    W = Wev * 1.602 * 10 ** (-19) # W w dżulach

    if foton == W:
        print("Zjawisko fotoelektryczne zachodzi; Elektron nie otrzyma dodatkowej energii kinetycznej")
    elif foton > W:
        # energia kinetyczna:
        Ek = foton - W
        me = 9.109 * 10 ** (-19)
        v = math.sqrt(2 * Ek / me)
        print("Zjawisko fotoelektryczne zachodzi; Maksymalną energią kinetyczną jaką może otrzymać elektron jest:", round(Ek, 22), "dzuli, a jego prędkość wyniesie maksymalnie", round(v, 3), "m/s.")
    else:
        print("Zjawisko elektryczne dla tego układu nie zachodzi")

    # czestotliwosc graniczna:
    f0 = W / h
    dlugosc0 = c / f0 * 10 ** 9
    print("Czy chciałbyś również wiedzieć jaka jest częstotliwość graniczna dla wybranego przez Ciebie metalu?")
    chcesz2 = str(input())
    chcesz2 = chcesz2.lower()
    if chcesz2 == 'tak':
        print("Częstotliwość graniczna dla", nazwam1, "wynosi:", f0, "Hz, co odpowiada", round(dlugosc0, 3), "nm")
    print("Czy chcesz spróbować ponownie?")
    chcesz = str(input())
    chcesz = chcesz.lower()
    if chcesz == 'tak':
        zjawisko()
    else:
        print("Dziękujemy za wypróbowanie naszego wspaniałego programu :)")

def dajmetal():
    print("Wybierz metal, dla którego chciałbyś sprawdzić czy zajdzie zjawisko; Wpisz nazwę lub skrót")
    nazwam = str(input())
    nazwam1 = nazwam.lower()
    return(nazwam1)
def dajfale():
    print("Wybierz długość fali, która ma padać na metal [nm]")
    dlugosc = float(input())
    return(dlugosc)    
        