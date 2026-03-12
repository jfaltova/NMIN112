"""
Spocte integral funkce v intervalu [0, 1] metodou Riemannova integralu. 
Napoveda: Provedte jemne deleni intervalu.
Postup:
- Deleni intervalu pomoci np.linspace
- Vyhodnoceni funkce v bodech deleni
- Soucet hodnot funkce v bodech deleni a vynasobeni delky intervalu mezi deleni
"""

import numpy as np

def f(x):
    """Funkce, jejíž integrál chceme spočítat."""
    return x**2

# Dělení intervalu [0, 1] na n částí
n = 1000
x = np.linspace(0, 1, n + 1)  # n+1 bodů včetně 0 a 1

# Vyhodnocení funkce v bodech dělení
y = f(x)

# Výpočet Riemannova integrálu
delta_x = 1. / n  # délka intervalu
integral = np.sum(y) * delta_x  

print(f"Riemannův integrál funkce x^2 je přibližně: {integral:.6f}")
