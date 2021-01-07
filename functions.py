import ctypes
import codecs
import ast
import math
import random
import numpy as np
import matplotlib.pyplot as plt
from tabulate import tabulate
import turtle
from PIL import Image, ImageDraw, ImageFont

def popupth(nazwa, tytul):
    popup = ''
    with codecs.open(nazwa, encoding='utf-8') as f:
        for line in f:
            popup = popup + line
    ctypes.windll.user32.MessageBoxW(0, popup, tytul, 1)
    
    
def zjawisko(howtime):
    with open("bibliotekametale.txt", "r") as data:
        bibliotekam = ast.literal_eval(data.read())
    while True:
        try:
            nazwam1 = dajmetal()
            Wev = float(bibliotekam[nazwam1])
        except KeyError:
            print("Podanego metalu nie ma w bibliotece bądź jego nazwa została wprowadzona niepoprawnie; Spróbuj jeszcze raz:")
            continue
        break
    while True:
        try:
            dlugosc = dajfale()
        except ValueError:
            print("Wpisz wartość liczbową")
            continue
        break

    Ek = 0
    v = 0
    # lewa strona rownania:
    c = 2.9979 * 10 ** 8
    f = c / (dlugosc * 10 ** (-9))
    h = float(6.63 * 10 ** (-34))
    foton = h * f

    # prawa strona rownania:
    W = Wev * 1.602 * 10 ** (-19) # W w dżulach

    if foton == W:
        print("Zjawisko fotoelektryczne zachodzi; Elektron nie otrzyma dodatkowej energii kinetycznej")
    elif foton > W:
        # energia kinetyczna:
        Ek = foton - W
        me = 9.109 * 10 ** (-19)
        v = math.sqrt(2 * Ek / me)
        print("Zjawisko fotoelektryczne zachodzi; Maksymalną energią kinetyczną jaką może otrzymać elektron jest:", round(Ek, 22), "dżuli, a jego prędkość wyniesie maksymalnie", round(v, 3), "m/s.")
    else:
        print("Zjawisko fotoelektryczne dla tego układu nie zachodzi")

    # czestotliwosc graniczna:
    f0 = W / h
    dlugosc0 = c / f0 * 10 ** 9
    print("Czy chciał*byś również wiedzieć jaka jest częstotliwość graniczna dla wybranego przez Ciebie metalu?")
    chcesz2 = str(input())
    chcesz2 = chcesz2.lower()
    if chcesz2 == 'tak':
        print("Częstotliwość graniczna dla", nazwam1, "wynosi:", f0, "Hz, co odpowiada", round(dlugosc0, 3), "nm")
    print("Czy chcesz spróbować ponownie?")
    chcesz = str(input())
    chcesz = chcesz.lower()
    listadane = [howtime, nazwam1, f0, dlugosc, round(Ek, 22),round(v, 3) ]
    arravclists = np.array([listadane])
    if howtime == 1:
        global finalarr
        finalarr = np.array([listadane])
    else:
        finalarr = np.append(finalarr, arravclists, axis = 0)
    if chcesz == 'tak':
        howtime = howtime+1
        zjawisko(howtime)
    else:
        print("Dziękujemy za skorzystanie z naszego programu. Oto tabelka podsumowująca Twoje próby:")
        tabletable(finalarr)

def dajmetal():
    print("Wybierz metal, dla którego chciał*byś sprawdzić czy zajdzie zjawisko; Wpisz nazwę lub skrót; Jeżeli chcesz wybrać losowy metal wpisz 'losowy'")
    nazwam = str(input())
    with open("bibliotekametalelosowa1.txt", "r") as data:
        bibliotekam = ast.literal_eval(data.read())
    if nazwam == "losowy":
        nazwam1 = random.choice(list(bibliotekam.keys()))
        print("Wylosowany metal to", nazwam1)
    else:
        nazwam1 = nazwam.lower()
    return(nazwam1)

def dajfale():
    print("Wybierz długość fali, która ma padać na metal [nm]; Jeżeli chcesz wybrać losową długość fali, wpisz 'losowa'")
    dlugosc = str(input())
    if dlugosc == "losowa":
        print("Czy chcesz wybrać konkretny rodzaj promieniowania?")
        rodzaj = str(input())
        rodzaj = rodzaj.lower()
        if rodzaj == 'tak':
            print("Aby otrzymać fale radiowe, wpisz 'radiowe', odpowiedznio: mikorfale = 'mikrofale', podczerwień = 'podczerwien', światło widzialne = 'widzialne', ultrafiolet = 'ultrafiolet', promieniowanie rentgenowskie = 'rentgenowskie'")
            kon = str(input())
            kon = kon.lower()
            if kon == 'radiowe':
                dlugosc = random.randint(10**9, 10**13)
                print("Wylosowana długość fali to", dlugosc, "nm.")
            elif kon == 'mikrofale':
                dlugosc = random.randint(10**6, 10**9)
                print("Wylosowana długość fali to", dlugosc, "nm.")
            elif kon == 'podczerwien':
                dlugosc = random.randint(700, 10**6)
                print("Wylosowana długość fali to", dlugosc, "nm.")
            elif kon == 'ultrafiolet':
                dlugosc = random.randint(10, 380)
                print("Wylosowana długość fali to", dlugosc, "nm.")
            elif kon == 'rentgenowskie':
                dlugosc = random.randint(0.005, 10)
                print("Wylosowana długość fali to", dlugosc, "nm.")
            elif kon == 'widzialne':
                print("Czy chcesz wybrać konkretny kolor światła widzialnego?")
                rodzaj_widzialnego = str(input())
                rodzaj_widzialnego = rodzaj_widzialnego.lower()
                if rodzaj_widzialnego == 'tak':
                    print("Jeżeli chcesz wybrać kolor fioletowy, wpisz 'fiolet', niebieski = 'niebieski', jasnoniebieski = 'jasnoniebieski', zielony = 'zielony', żółty = 'zolty', pomarańczowy = 'pomaranczowy', czerwony = 'czerwony")
                    kolor = str(input())
                    kolor = kolor.lower()
                    if kolor == 'fiolet':
                        dlugosc = random.randint(380, 450)
                        print("Wylosowana długość fali to", dlugosc, "nm.")
                    elif kolor == 'niebieski':
                        dlugosc = random.randint(450, 485)
                        print("Wylosowana długość fali to", dlugosc, "nm.")
                    elif kolor == 'jasnoniebieski':
                        dlugosc = random.randint(485, 500)
                        print("Wylosowana długość fali to", dlugosc, "nm.")
                    elif kolor == 'zielony':
                        dlugosc = random.randint(500, 565)
                        print("Wylosowana długość fali to", dlugosc, "nm.")
                    elif kolor == 'zolty':
                        dlugosc = random.randint(500, 565)
                        print("Wylosowana długość fali to", dlugosc, "nm.")
                    elif kolor == 'pomaranczowy':
                        dlugosc = random.randint(590, 625)
                        print("Wylosowana długość fali to", dlugosc, "nm.")
                    elif kolor == 'czerwony':
                        dlugosc = random.randint(625, 700)
                        print("Wylosowana długość fali to", dlugosc, "nm.")
                else:
                    dlugosc = random.randint(380, 700)
                    print("Wylosowana długość fali to", dlugosc, "nm.")
        else:
            dlugosc = random.random()
            print("Wylosowana długość fali to", dlugosc, "nm.")
    dlugosc = float(dlugosc)
    return(dlugosc)

def wykresy():
    # f0 jest wartością przykladową
    f = np.arange(-10, 100, 0.1)
    f0 = 30
    h = 6.62
    e = 1.9
    funkcje = []
    funkcje.append((f-f0)*h/e)
    funkcje.append((f-f0)*h)
    okno = plt.figure(figsize=(12, 8), dpi=100)
    okno.suptitle("Wykresy zależności Uh oraz Ek od częstotliwości", color="black", fontsize=16, fontweight="bold")
    listafunkcji = []
    listafunkcji.append(plt.subplot(2, 1, 1))
    plt.ylim(0, 100)
    plt.xlabel("f [Hz]", fontsize=11)
    plt.ylabel("Uh [V]", fontsize=11)
    plt.scatter(f0, 0, s=30, c="black")
    plt.annotate("f0, częstotliwość graniczna", (f0, 0), (f0 - 25, 5))
    plt.xticks([])
    plt.yticks([])
    listafunkcji.append(plt.subplot(2, 1, 2))
    plt.ylim(0, 100)
    plt.xlabel("f [Hz]", fontsize=11)
    plt.ylabel("Ek [J]", fontsize=11)
    plt.scatter(f0, 0, s=30, c="black")
    plt.annotate("f0, częstotliwość graniczna", (f0, 0), (f0 - 25, 5))
    plt.xticks([])
    plt.yticks([])
    kolor = ("red", "blue")
    grubosclinii = (2, 2)
    etykiety = ("$Uh=h/e(f-f0); Uh(f)$", "$Ek=h*(f-f0); Uh(f)$")
    for i in range(2):
        listafunkcji[i].plot(f, funkcje[i], color=kolor[i], lw=grubosclinii[i])
        listafunkcji[i].set_title(etykiety[i])
    plt.show()
    
def tabletable(variablist):
    a = np.array([['Przykład', 'terb', 724886877828054.4, 0.746745362463718, 2.656888e-16, 24.153]])
    newArray = np.append(a, variablist, axis=0)
    listfromarr = newArray.tolist()
    print(tabulate(listfromarr, headers=['L.Prób', 'Metal', 'cz.gran[Hz]', 'Dł.fali[nm]', 'Ek[J]', 'v[m/s]']))

def obrazki():
    im = Image.open('nice.jpg')
    im2 = Image.open('fotokomorka.jpg')
    font_type = ImageFont.truetype('arial.ttf', 19)
    draw = ImageDraw.Draw(im)
    draw.text(xy=(30, 30), text='Przykładowa fotokomórka:', fill=(0, 0, 0), font=font_type, encoding='utf-8')
    draw2 = ImageDraw.Draw(im2)
    draw2.text(xy=(20, 20), text='Uproszczony schemat fotokomórki:', fill=(0, 0, 0), font=font_type, encoding='utf-8')
    im.show()
    im2.show()
    font_type = ImageFont.truetype('arial.ttf', 40)
    font_type1 = ImageFont.truetype('arial.ttf', 60)
    im3 = Image.open('wzory.jpg')
    draw = ImageDraw.Draw(im3)
    draw.text(xy=(20, 50), text='OPIS MATEMATYCZNY', fill=(0, 0, 0), font=font_type1, encoding='utf-8')
    draw = ImageDraw.Draw(im3)
    draw.text(xy=(20, 150), text='Zjawisko fotoelektryczne zewnętrzne łatwo jest opisać następującym wzorem:',
              fill=(0, 0, 0), font=font_type, encoding='utf-8')
    draw.text(xy=(20, 500),
              text='Lewa strona równania opisuje FOTON (częstotliwość promieniowania wymnożoną przez stałą Plancka h), \nnatomiast prawa - wybity ELEKTRON (suma pracy wyjścia W oraz energii kinetycznej Ek).',
              fill=(0, 0, 0), font=font_type, encoding='utf-8')
    draw.text(xy=(20, 650),
              text='Nasz program obliczy maksymalną energię kinetyczną jaką może uzyskać wybity elektron oraz jego \nmaksymalną prędkość dla takiej energii zgodnie ze wzorami:',
              fill=(0, 0, 0), font=font_type, encoding='utf-8')
    draw.text(xy=(20, 1200), text='Oraz częstotliwość graniczną wedle następującego wzoru:', fill=(0, 0, 0),
              font=font_type, encoding='utf-8')
    im3.show()

def animacja():
    window = turtle.Screen()
    window.bgcolor("black")
    window.title("Symulacja zjawiska fotoelektrycznego")
    font = ("Arial", 22)

    metal = turtle.Turtle()
    metal.speed(0)
    metal.shape("square")
    metal.color("white")
    metal.shapesize(stretch_wid=1, stretch_len=9)
    metal.penup()

    napismetal = turtle.Turtle()
    napismetal.hideturtle()
    napismetal.penup()
    napismetal.color("white")
    napismetal.setposition(150, 0)
    napismetal.write("Metal", font=font)

    foton = turtle.Turtle()
    foton.shape("circle")
    foton.color("yellow")
    foton.shapesize(0.5, 0.5)
    foton.penup()
    foton.speed(0)
    foton.setposition(0, 220)
    foton.dy = -8

    napisfoton = turtle.Turtle()
    napisfoton.hideturtle()
    napisfoton.penup()
    napisfoton.color("yellow")
    napisfoton.setposition(30, 250)
    napisfoton.write("Foton", font=font)

    e = turtle.Turtle()
    e.shape("circle")
    e.color("white")
    e.penup()
    e.speed(0)
    e.setposition(0, 0)

    napise = turtle.Turtle()
    napise.hideturtle()
    napise.penup()
    napise.color("blue")
    napise.setposition(30, 250)

    klik = turtle.Turtle()
    klik.hideturtle()
    klik.penup()
    klik.color("white")
    klik.setposition(0, -220)
    klik.write("Kliknij w ekran aby foton uderzył po kątem", font=font, align="center")

    def fxn(x, y):
        foton.hideturtle()
        foton.setposition(200, 200)
        napisfoton.clear()
        e.hideturtle()
        napise.clear()
        klik.clear()

        foton2 = turtle.Turtle()
        foton2.shape("circle")
        foton2.color("yellow")
        foton2.shapesize(0.5, 0.5)
        foton2.penup()
        foton2.speed(0)
        foton2.setposition(-220, 220)

        napisfoton.setposition(-190, 220)
        napisfoton.write("Foton", font=font)

        e2 = turtle.Turtle()
        e2.shape("circle")
        e2.color("white")
        e2.penup()
        e2.speed(0)
        e2.setposition(0, 0)

        klik.write("Po zakończeniu animacji kliknij w ekran aby odtworzyć ponownie", font=font, align="center")

        while True:
            foton2.sety(foton2.ycor())
            e2.sety(e2.ycor())
            e2.left(45)
            foton2.right(45)
            while True:
                foton2.forward(3)
                if foton2.distance(metal) < 10:
                    foton2.color("white")
                    foton2.shapesize(0.01, 0.01)
                    napisfoton.clear()
                    e2.color("blue")
                    napise.setposition(120, 220)
                    napise.write("Elektron", font=font)
                    while True:
                        e2.forward(2.5)
                        if e2.distance(metal) > 600:
                            napise.clear()

    turtle.onscreenclick(fxn, 1)

    while True:
        metal.sety(metal.ycor())
        napismetal.sety(napismetal.ycor())
        foton.sety(foton.ycor()+foton.dy)
        napisfoton.sety(napisfoton.ycor())
        e.sety(e.ycor())
        napise.sety(napise.ycor())
        if foton.distance(metal) < 10:
            foton.dy = 0
            foton.color("white")
            foton.shapesize(0.01, 0.01)
            napisfoton.clear()
            e.dy = 7
            e.color("blue")
            e.sety(e.ycor() + e.dy)
            napise.write("Elektron", font=font)