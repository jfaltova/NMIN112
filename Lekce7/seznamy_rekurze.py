"""
Rekurze a seznamy.
Napište funkci, která 
- vezme seznam čísel a vrátí součet všech čísel v seznamu pomocí rekurze.
- zjistí délku seznamu pomocí rekurze
- otočí pořadí prvků v seznamu pomocí rekurze.
"""

def soucet(seznam):
    if len(seznam) == 0:
        return 0
    else:
        return seznam[0] + soucet(seznam[1:])

def delka(seznam):
    if len(seznam) == 0:
        return 0
    else:
        return 1 + delka(seznam[1:])

def otoc(seznam):
    if len(seznam) == 0:
        return []
    else:
        return [seznam[-1]] + otoc(seznam[:-1])

