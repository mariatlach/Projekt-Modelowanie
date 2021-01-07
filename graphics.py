import numpy as np
import matplotlib.pyplot as plt

def wykresy():
    # f0 jest wartoscia przykladowa
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
wykresy()