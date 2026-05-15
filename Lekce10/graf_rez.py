"""
Strom s ohodnocenymi hranami. Soucet cen vsech hran je cena stromu.
Pokud strom rozrizneme smazanim jedne hrany, vzniknou dva podstromy. 
Maximum z jejich cen nazveme cenou rezu.

Formát vstupu: Na prvním řádku standardního vstupu je číslo nn: počet vrcholů stromu. 
Na dalších n-1 řádkách jsou popsané jednotlivé hrany stromu trojicemi čísel u v c, 
kde u a v jsou vrcholy spojené hranou (vrcholy číslujeme od 1 do nn) a c cena této hrany.

Formát výstupu: Výstupem je jediné celé číslo: minimální možná cena řezu.

Řešení: prohledáme strom pomocí procházení do hloubky (DFS) a pro každou hranu spočítáme cenu řezu, 
kterou získáme jejím rozříznutím.
"""

import sys

sys.setrecursionlimit(50000)    # zvetsime limit pro rekurzi

def nacti_vstup():
    # nacteme vstup a vytvorime seznam sousedu pro kazdy vrchol
    n = int(input())
    sousede = [[] for _ in range(n)]
    cena_vse = 0
    for _ in range(n - 1):
        u, v, c = map(int, input().split())
        u -= 1    # prevedeme na indexy od 0
        v -= 1              
        sousede[u].append((v, c))
        sousede[v].append((u, c))
        cena_vse += c
    # vracime mapu sousedu a cenu vsech hran
    return sousede, cena_vse

def dfs(id, rodic, sousede):
    # prohledavame strom a pocitame cenu rezu pro kazdou hranu
    # vracime cenu podstromu a aktualizujeme globalni minimum rezu
    global minimum_rezu
    cena_podstromu = 0     # cena podstromu, kterou pocitame pro aktualni vrchol id
    for v, c in sousede[id]:     # prochazime sousedy vrcholu id
        if v != rodic:           # nevracime se zpet k rodici
            cena1 = dfs(v, id, sousede)      # cena 1. podstromu vznikleho po rozriznuti hrany mezi id a v
            cena2 = cena_total - c - cena1   # cena 2. podstromu vznikleho po rozriznuti hrany mezi id a v
            minimum_rezu = min(minimum_rezu, max(cena1, cena2))   # aktualizujeme minimum rezu
            # Proc se k cene podstromu pricitaji cena1 a c? Protoze cena podstromu vznikleho po rozriznuti hrany mezi id 
            # a v se sklada z ceny podstromu vznikleho po rozriznuti hrany mezi id a v (cena1) a ceny hrany 
            # mezi id a v (c).
            cena_podstromu += cena1 + c      # cena podstromu vznikleho po rozriznuti hrany mezi id a v
    return cena_podstromu                   

strom, cena_total = nacti_vstup()
minimum_rezu = float('inf')   # inicializujeme minimum rezu jako nekonecno
dfs(0, -1, strom)   # prohledame strom od vrcholu 0
print(minimum_rezu)
