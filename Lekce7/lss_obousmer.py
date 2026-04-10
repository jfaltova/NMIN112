"""
Obousměrný LSS
-obsahuje informaci (data)
-ukazatel na předchozí a příští prvek
Vhodné např. pro implementaci zásobníku, fronty, seznamu
"""
class Node:
    def __init__(self, data):
        self.data = data
        self.pred = None
        self.dalsi = None

class LSS:
    def __init__(self):
        self.hlava = None
        self.posledni = None

    def pridej(self, data):
        new_node = Node(data)
        if self.hlava is None:
            self.hlava = new_node
            self.posledni = new_node
        else:
            self.posledni.dalsi = new_node
            new_node.pred = self.posledni
            self.posledni = new_node

    def vytvor(self):
        vstup = list(map(int, input().split()))
        for data in vstup:
            self.pridej(data)

    def vypis(self):
        p = self.hlava
        while p != None:
            print(p.data, end=' ')
            p = p.dalsi
        print()

    def smaz(self, node):
        if node.pred:
            node.pred.dalsi = node.dalsi
        else:
            self.hlava = node.dalsi
        if node.dalsi:
            node.dalsi.pred = node.pred
        else:
            self.posledni = node.pred

    def smaz_hodnota(self, data):
        """
        Smazání všech prvků s danou hodnotou. 
        """
        return

    def obrat(self):
        """ Obrácení pořadí prvků v seznamu. """
        return
    
if __name__ == "__main__":
    """
    Testovací program pro obousměrný LSS
    """
    lss = LSS()
    lss.vytvor()
    lss.vypis()
    # Smazání prvního a posledního prvku
    if lss.hlava:
        lss.smaz(lss.hlava)
    if lss.posledni:
        lss.smaz(lss.posledni)
    lss.vypis()
    # Obrácení seznamu
    lss.obrat()
    lss.vypis()
    # Smazání prvku s hodnotou 3
    lss.smaz_hodnota(3)
    lss.vypis()
