"""
Třída na práci s řídkými polynomy.
- Polynom je reprezentován seznamem dvojic (exponent, koeficient), 
kde exponent je celé číslo a koeficient je reálné číslo.
- Třída by měla podporovat:
    - Inicializaci ze seznamu dvojic (exponent, koeficient).
    - Rozumný výpis
    - Metodu pro vyhodnocení polynomu v daném bodě x.
    - Metodu pro sčítání dvou polynomů.

Příklady použití:
p1 = RidkyPolynom([(2, 3), (0, 1)])  # 3*x^2 + 1
p2 = RidkyPolynom([(1, 2), (0, 4)])  # 2*x + 4
print(f"Polynom p1: {p1}")
print(f"Polynom p2: {p2}")
print(f"p1(2) = {p1.vyhodnot(2)}")
p3 = p1.secti(p2)
print(f"p1 + p2: {p3}")
"""

class RidkyPolynom:
    def __init__(self, cleny):
        """Inicializace ze seznamu dvojic (exponent, koeficient)."""
        # Seradime cleny podle exponentu sestupně
        cleny.sort(key=lambda x: x[0], reverse=True)
        self.cleny = cleny
    def __str__(self) -> str:
        """Vrátí reprezentaci polynomu jako string. 
        Todo: Misto x^0 pouzijeme jen koeficient, misto x^1 pouzijeme x."""
        return " + ".join(f"{coef}*x^{exp}" for exp, coef in self.cleny)
    def __repr__(self) -> str:
        """Vrátí formální reprezentaci polynomu."""
        return f"RidkyPolynom({self.cleny})"
    def vyhodnot(self, x) -> float:
        """Vyhodnocení polynomu v daném bodě x."""
        pass
    def secti(self, other):
        """Sčítání dvou polynomů."""
        pass
