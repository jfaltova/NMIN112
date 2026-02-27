"""
Trida Zlomek
Požadavky:
    - zlomek zadáváme jeho čitatelem a jmenovatelem (typ int)
    - zlomky chceme sčítat (vraci Zlomek)
    - zlomky chceme porovnávat (operator ==, vraci bool)
    - chceme převrácenou hodnotu zlomku (zmeni atributy, vraci None)
    - chceme pěkný výpis (operator str)

# Priklady
z1 = Zlomek(3,7)
z2 = Zlomek(8,3)
z1 == z2    # porovnani (__eq__)
z1 + z2     # scitani (__add__)
z1.prevrat()   # prevraceny zlomek
print(z1)      # vypis

# Potrebujeme osetrit
z = Zlomek(4,0)
z = Zlomek(3,-7)
"""

import math

class Zlomek:
    """Třída reprezentující zlomek s čitatelem a jmenovatelem."""
    def __init__(self, citatel: int, jmenovatel:int) -> None:
        """Inicializace zlomku s čitatelem a jmenovatelem."""

        """Ošetření speciálních případu"""
        if jmenovatel == 0:
            raise ValueError("Jmenovatel nesmí být nula.")

        # Nezáporný jmenovatel
        if jmenovatel < 0:
            citatel *= -1
            jmenovatel *= -1

        # Zlomek v základním tvaru - společný dělitel
        gcd = math.gcd(citatel, jmenovatel)

        self.citatel = citatel//gcd
        self.jmenovatel = jmenovatel//gcd

    def __str__(self) -> str:
        """Vrací rozumný výpis zlomku."""
        return f"{self.citatel}/{self.jmenovatel}"

    def __repr__(self) -> str:
        """Vrací řetězcovou reprezentaci zlomku."""
        return f"Zlomek({self.citatel}, {self.jmenovatel})"

    def __eq__(self, other) -> bool:
        """Porovnává dva zlomky - zlomky máme v základním tvaru, 
        takže porovnáme čitatele a jmenovatele."""
        return (self.citatel == other.citatel and \
                self.jmenovatel == other.jmenovatel)

    def __add__(self, other) -> "Zlomek":
        """Sčítá dva zlomky a vrací nový zlomek v základním tvaru."""
        citatel = self.citatel * other.jmenovatel + \
                   other.citatel * self.jmenovatel
        jmenovatel = self.jmenovatel * other.jmenovatel
        return Zlomek(citatel, jmenovatel)

    def prevrat(self) -> None:
        """Převrátí zlomek: výměna čitatele a jmenovatele"""
        self.jmenovatel, self.citatel = self.citatel, self.jmenovatel    
    
if __name__ == '__main__':
    """Testovací kód pro třídu Zlomek."""
    z1 = Zlomek(3,7)
    z2 = Zlomek(3,8)
    print(z1 == z2)    # porovnani (__eq__)
    print(z1 + z2)     # scitani (__add__)
    z1.prevrat()   # prevraceny zlomek
    print(z1)      # vypis

    # Co speciální případy?
    #print(Zlomek(4,0))    # vrací ValueError
    print(Zlomek(3,-7))
    print(Zlomek(3,-6))
