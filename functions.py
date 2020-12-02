import ctypes
import codecs

def popupth(nazwa, tytul):
    # tutaj jest mala funkcja ktora otwiera nasze okienko z wyjasnieniem Z POLSKIMI ZNAKAMI :))))))
    popup = ''
    with codecs.open(nazwa, encoding='utf-8') as f:
        for line in f:
            popup = popup + line
    ctypes.windll.user32.MessageBoxW(0, popup, tytul, 1)
