import functions
from PIL import Image, ImageDraw, ImageFont

functions.popupth('fotokom.txt', "Wyjasnienie")

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
draw.text(xy=(20, 150), text='Zjawisko fotoelektryczne zewnętrzne łatwo jest opisać następującym wzorem:', fill=(0, 0, 0), font=font_type, encoding='utf-8')
draw.text(xy=(20, 500), text='Lewa strona równania opisuje FOTON (częstotliwość promieniowania wymnożoną przez stałą Plancka h), \nnatomiast prawa - wybity ELEKTRON (suma pracy wyjścia W oraz energii kinetycznej Ek).', fill=(0, 0, 0), font=font_type, encoding='utf-8')
draw.text(xy=(20, 650), text='Nasz program obliczy maksymalną energię kinetyczną jaką może uzyskać wybity elektron oraz jego \nmaksymalną prędkość dla takiej energii zgodnie ze wzorami:', fill=(0, 0, 0), font=font_type, encoding='utf-8')
draw.text(xy=(20, 1200), text='Oraz częstotliwość graniczną wedle następującego wzoru:', fill=(0, 0, 0), font=font_type, encoding='utf-8')
im3.show()

print("Czy chcesz wyświetlić, którąć z bibliotek?")
bibl1 = str(input())
bibl1= bibl1.lower()
if bibl1 == 'tak':
    print("Jeśli chcesz wyświetlić bibliotekę metali wpisz: 'metale', jeśli częstotliwości promieniowań, wpisz: 'fale'; Jeżeli chcesz wyświtlić obie biblioteki, wpisz 'obie'")
    ktora = str(input())
    if ktora == 'metale':
        functions.popupth('bibliotekametalenice.txt', "Biblioteka prac wyjścia dla wybranych metali:")
    elif ktora == 'fale':
        functions.popupth('bibliotekafale.txt', "Biblioteka cdługości fal dla odpowiednich promieniowań:")
    elif ktora == 'obie':
        functions.popupth('bibliotekametalenice.txt', "Biblioteka prac wyjścia dla wybranych metali:")
        functions.popupth('bibliotekafale.txt', "Biblioteka cdługości fal dla odpowiednich promieniowań:")
functions.zjawisko()


print('Czy chciał*bys wyswietlic bibliografie?')
bibl = str(input())
bibl = bibl.lower()
if bibl == 'tak':
    functions.popupth('bibliografia.txt', "Bibliografia")
