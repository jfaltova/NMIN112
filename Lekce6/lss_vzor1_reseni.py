class Uzel:
    """
    Trida pro uzel s atributy info (informace) a dalsi (odkaz na dalsi uzel)
    """
    def __init__(self, info):
        self.info = info
        self.dalsi = None

def vytvor():
    """
    Funkce pro vytvoreni spojoveho seznamu ze vstupu tohoto typu:
    1. pocet prvku seznamu
    2. cisla oddelena mezerou
    """
    pocet = int(input())   # Pocet uzlu
    if pocet == 0:         # Prazdny seznam
        return None
    seznam = list(map(int, input().split()))
    p = Uzel(seznam[0])
    zacatek = p          # odkaz na prvni prvek ulozime do zacatek
    pred = p             # ulozime si odkaz na uzel p do pomocne promenne
    for i in range(1, pocet):
        p = Uzel(seznam[i])    # novy uzel
        pred.dalsi = p         # odkaz ulozime do predchazejiciho uzlu
        pred = p               # posunume ukazatel
    return zacatek
    
def vypis(zacatek):
    """
    Vypis linearniho spojoveho seznamu
    - pokud je seznam prazdny, vypise se slovo "PRAZDNY"
    """
    p = zacatek
    if p == None:
        print('PRAZDNY')
        return
    while p != None:
        print(p.info, end = " ")
        p = p.dalsi
    print()

def pocet_max(zacatek):
    p = zacatek
    if p == None:
        return 0
    maximum = p.info
    pocet_max = 0
    while p != None:
        if p.info > maximum:
            maximum = p.info
            pocet_max = 1
        elif p.info == maximum:
            pocet_max += 1
        p = p.dalsi
    return pocet_max

def zrus_vsechny_max(zacatek):
    p = zacatek
    if p == None:
        return None
    maximum = p.info
    while p != None:
        if p.info > maximum:
            maximum = p.info
        p = p.dalsi
    while zacatek.info == maximum:
        zacatek = zacatek.dalsi
        if zacatek == None:
            return None
    pred = zacatek
    p = pred.dalsi
    while p != None:
        if p.info == maximum:
            pred.dalsi = p.dalsi
            p = p.dalsi
        else:
            pred = p
            p = p.dalsi
    return zacatek

lss = vytvor()
vypis(lss)
print(pocet_max(lss))
lss = zrus_vsechny_max(lss)  
vypis(lss)