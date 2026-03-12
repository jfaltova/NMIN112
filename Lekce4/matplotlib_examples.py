"""
Ukazka knihovny MatPlotLib
"""
import matplotlib.pyplot as plt
import numpy as np
import math

# Prvni ukazka: vykresleni funkce sinus
def plot1():
    # Rozsah x
    x = np.linspace(0, 2 * np.pi, 100)
    # Hodnoty y
    y = np.sin(x)

    # Graf x versus y
    plt.plot(x, y)
    # Vykresli
    plt.show()

# Vykresleni dvou krivek
# Ruzne typy car
# Popis os, nazev grafu
def plot2():
    # Nastaveni stylu obrazku
    #plt.style.use('fivethirtyeight')
    # Styl komiksu xkcd.com
    #plt.xkcd()

    x = np.linspace(0, 2 * np.pi, 10)
    """ 
    Parametry plt.plot
    1. x
    2. f(x)
    3. typ markeru, barva, typ cary
    4. label - text do legendy
    """
    # Typy car, markeru, barvy: http://bit.ly/Matplotlib-Fmt-Str
    # b--: modra carkovana cara
    plt.plot(x, np.sin(x), 'b--', label='sin(x)')
    #plt.plot(x, np.sin(x), 'bx', label='sin(x)')
    # barva zapsana pomoci hex color codes (seda)
    # tloustka cary 3 (defaultni hodnota je 1)
    plt.plot(x, np.cos(x), color='#444444', linestyle='-.', linewidth=3, label='cos(x)')

    # Nazev grafu, popis os
    plt.title('Goniometricke funkce')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    # Vykresleni legendy
    plt.legend()
    # Vykresleni site
    plt.grid(True)

    # Ulozeni obrazku
    #plt.savefig('plot2.png')
    # Vykresleni obrazku
    plt.show()

# Sloupcový graf
# Horizontalni a vertikalni cary, popisky
def plot3():
    x = np.linspace(0, 2 * np.pi, 30)
    plt.bar(x, np.sin(x), color='blue', edgecolor='black', width=0.2)

    # Dve horizontalni cary
    plt.hlines([-1.0, 1.0], xmin=0., xmax=2 * np.pi)
    # Jedna vertikalni cara
    plt.vlines([np.pi], ymin=-1., ymax=1.)
    # Pridame popisky
    plt.text(5.0, 0.85, "sin(x)=1", fontsize=12)
    plt.annotate("sin(x)=-1", (0.1, -0.95), xytext=(0.15, -0.8), arrowprops={'arrowstyle': '->'}, fontsize=12)

    # Popis os, titulek
    plt.title('Ukazka: sloupcovy graf')
    plt.xlabel('x')
    plt.ylabel('sin(x)')
    plt.show()


# Histogram
def plot4():
    # Gaussovo rozdeleni
    y = np.random.normal(0, 1, 10000)
    # Histogram (bins: pocet binu, range: rozsah na ose x)
    plt.hist(y, bins=30, range=(-3.,3.), edgecolor='black')
    # Popis os, titulek
    plt.title('Histogram: Gaussovo rozdeleni')
    plt.xlabel('x')
    plt.ylabel('Cetnost')
    plt.show()

# Rozdeleni obrazku na nekolik podobrazku
def plot5():
    x = np.linspace(0, 2, 100)
    # Prvni podobrazek
    # (221) nebo (2,2,1): Pocet radku, sloupcu, kolikate okno
    plt.subplot(221)
    plt.plot(x, x)
    plt.xlabel('x')
    plt.ylabel('x')
    # Druhy podobrazek
    plt.subplot(222)
    plt.plot(x, x**2)
    plt.xlabel('x')
    plt.ylabel('x**2')
    # Treti
    plt.subplot(223)
    plt.plot(x, x**3)
    plt.xlabel('x')
    plt.ylabel('x**3')
    # A ctvrty
    plt.subplot(224)
    plt.plot(x, x**4)
    plt.xlabel('x')
    plt.ylabel('x**4')

    # Pro vetsi mezery mezi obrazky
    #plt.tight_layout()
    plt.show()

# Nekolik obrazku: sdileni os
def plot6():
    x = np.linspace(0, 10, 1000)
    # Budeme mit 3 podobrazky
    # Zalozeni 1. obrazku
    ax = plt.subplot(311)
    plt.plot(x, np.sin(2*math.pi*x))
    #ax.set_xlabel('x')
    #ax.set_ylabel('k*sin(l*x)')
    # Sdileni os (na vsech obrazcich bude stejne meritko)
    plt.subplot(312, sharex=ax, sharey=ax)
    plt.plot(x, 0.5*np.sin(3*math.pi*x))
    plt.subplot(313, sharex=ax, sharey=ax)
    # Pro srovnani bez sdileni os
    #plt.subplot(313)
    plt.plot(x, 0.7*np.sin(5*math.pi*x))

    plt.show()

# Objektove rozhrani
def plot7():
    # fig je typu Figure (cely obrazek)
    # ax typu Axes (to je jeden graf)
    fig, ax = plt.subplots()

    # Nastaveni globalnich vlasnosti obrazku
    fig.set_facecolor('#ccccff')

    # Nakreslime krivku
    x = np.linspace(0, 5, 1000)
    # tuple -> p je typu matplotlib.lines.Line2D
    p, = ax.plot(x, np.cos(10*x))

    # Nastaveni vlastnosti krivky
    p.set_color('red')
    p.set_linewidth(2)

    # Upravime popisky na ose x (pootoceni)
    for tick in ax.get_xticklabels():
        tick.set_rotation(55)

    # Nastaveni nazvu grafu, popis os
    ax.set_title('Cosinus')
    ax.set_xlabel('x')
    ax.set_ylabel('Cos(10x)')
    plt.show()

plot4()