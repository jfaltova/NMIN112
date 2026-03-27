class Uzel:
    """
    Trida pro uzel s atributy info (informace) a dalsi (odkaz na dalsi uzel)
    """
    def __init__(self, info):
        self.info = info
        self.dalsi = None


class Lss:
    def __init__(self, zacatek = None):
        self.zacatek = zacatek

    def vytvor(self):
        """
        vytvoreni spojoveho seznamu ze vstupu
        vstup:
        1. pocet prvku seznamu
        2. cisla oddelena mezerou
        """
        pocet = int(input())
        if pocet == 0:
            return None
        seznam = list(map(int, input().split()))
        p = Uzel(seznam[0])
        self.zacatek = p          # odkaz na prvni prvek ulozime do zacatek
        pred = p             # ulozime si odkaz na uzel p do pomocne promenne
        for i in range(1, pocet):
            p = Uzel(seznam[i])    # novy uzel
            pred.dalsi = p         # odkaz ulozime do predchazejiciho uzlu
            pred = p               # posunume ukazatel
    
    def vypis(self):
        """
        Vypis linearniho spojoveho seznamu
        - pokud je seznam prazdny, vypise se slovo "PRAZDNY"
        """
        p = self.zacatek
        if p == None:
            print('PRAZDNY')
            return
        while p != None:
            print(p.info, end = " ")
            p = p.dalsi
        print()

    def pocet_max(self):
        """
        Funkce spocte pocet vyskytu nejvetsi hodnoty v seznamu
        - Vraci pocet vyskytu
        """
        if self.zacatek == None:
            return 0
        max_hodnota = self.zacatek.info
        pocet = 1
        p = self.zacatek.dalsi
        while p != None:
            if p.info > max_hodnota:
                max_hodnota = p.info
                pocet = 1
            elif p.info == max_hodnota:
                pocet += 1
            p = p.dalsi
        return pocet

    def zrus_vsechny_max(self):
        """
        Funkce vynecha vsechny prvky obsahujici nejvetsi ze 
        vsech cisel v danem seznamu. 
        - Vraci upraveny seznam
        """
        if self.zacatek == None:
            return
        max_hodnota = self.zacatek.info
        p = self.zacatek.dalsi
        while p != None:
            if p.info > max_hodnota:
                max_hodnota = p.info
            p = p.dalsi
        # odstraneni prvku s hodnotou max_hodnota
        while self.zacatek != None and self.zacatek.info == max_hodnota:
            self.zacatek = self.zacatek.dalsi
        p = self.zacatek
        while p != None and p.dalsi != None:
            if p.dalsi.info == max_hodnota:
                p.dalsi = p.dalsi.dalsi
            else:
                p = p.dalsi
      
lss = Lss()
lss.vytvor()
lss.vypis()
print(lss.pocet_max())
lss.zrus_vsechny_max()
lss.vypis()
