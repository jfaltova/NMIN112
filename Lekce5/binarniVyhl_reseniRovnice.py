"""
Využijte binární vyhledávání k nalezení řešení rovnice x = cos(x).
Postup:
1. Definujte funkci f(x) = x - cos(x).
2. Určete interval, ve kterém se řešení nachází (například [0, 1]). Zkontrolujte, 
že f(0) a f(1) mají opačné znaménko, což znamená, že řešení se nachází mezi těmito hodnotami.
3. Použijte binární vyhledávání k iterativnímu zúžení intervalu,
 dokud nenaleznete řešení s požadovanou přesností.
"""
import math

def binarniVyhl(funkce, a=0, b=1, presnost=1e-3):
    
    if funkce(a) * funkce(b) >= 0:
        raise ValueError("Funkce musí mít opačné znaménko na koncích intervalu.")
    
    while (b - a) > presnost:  # požadovaná přesnost
        stred = (a + b) / 2
        if funkce(stred) == 0:
            return stred  # nalezeno přesné řešení
        elif funkce(a) * funkce(stred) < 0:
            b = stred  # řešení je v levé polovině
        else:
            a = stred  # řešení je v pravé polovině
    
    return (a + b) / 2  # vracíme střed jako přibližné řešení

if __name__ == "__main__":
    """Testování"""
    presnost = [1e-3, 1e-5, 1e-7]
    for p in presnost:
        reseni = binarniVyhl(lambda x: x - math.cos(x), 0, 1, p)
        print(f"Řešení rovnice x = cos(x) je přibližně: {reseni:.4f}")
