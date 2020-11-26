# -*- coding: utf-8 -*-
import ctypes
import codecs
# tutaj jest mala funkcja ktora otwiera nasze okienko z wyjasnieniem Z POLSKIMI ZNAKAMI :))))))
popup = ''
with codecs.open('fotokom.txt', encoding='utf-8') as f:
    for line in f:
        popup = popup + line
ctypes.windll.user32.MessageBoxW(0, popup, "Wyjasnienie", 1)
