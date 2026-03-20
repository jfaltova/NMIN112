import random
import time

def merge_sort_iter(seznam):
    """Merge sort iterativně:
    Princip: Rozdělení pole na dvě poloviny, iterativní řešení.
    Postup:
    1. Rozdělíme pole na dvě poloviny.
    2. Postupně sléváme sousední úseky délek 1, 2, 4, ... až do délky pole.
    3. Pro slévání použijeme pomocný seznam, do kterého ukládáme seřazené prvky.
    4. Po každém slévání zkopírujeme obsah pomocného seznamu zpět do původního pole.
    5. Tento proces opakujeme, dokud není celé pole seřazeno.
    """
    n = len(seznam)
    size = 1
    s = seznam.copy()

    while size < n:
        for start in range(0, n, 2*size):
            mid = start + size
            end = min(start + 2*size, n)

            left = s[start:mid]
            right = s[mid:end]

            s[start:end] = merge(left, right)

        size *= 2

    return s

def merge(left, right):
    vysledek = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            vysledek.append(left[i])
            i += 1
        else:
            vysledek.append(right[j])
            j += 1

    vysledek.extend(left[i:])
    vysledek.extend(right[j:])

    return vysledek

def merge_sort(seznam):
    """Merge sort:
    Princip: Rozdělení pole na dvě poloviny, rekurzivní řešení.
    Postup:
    1. Rozdělíme pole na dvě poloviny.
    2. Rekurzivně seřadíme obě poloviny.
    3. Sléváme obě poloviny do jednoho seřazeného pole.
    4. Tento proces opakujeme, dokud není celé pole seřazeno.
    """
    if len(seznam) <= 1:
        return seznam

    mid = len(seznam)//2
    left = merge_sort(seznam[:mid])
    right = merge_sort(seznam[mid:])

    return merge(left, right)

def cas(sort_func, data):
    """Měří čas potřebný k seřazení dat pomocí zadané řadící funkce."""
    start = time.perf_counter()
    sort_func(data)
    end = time.perf_counter()
    return end - start

if __name__ == "__main__":
    """Testování merge sortu a merge sortu iterativně:"""
    rozsah = [1000, 2000, 4000, 8000]

    for n in rozsah:
        print(f"Velikost pole: {n}")
        data = [random.randint(0,100000) for _ in range(n)]
        print(f"Merge sort: {cas(merge_sort, data)}")
        print(f"Merge sort iter: {cas(merge_sort_iter, data)}")




























































































































































































































