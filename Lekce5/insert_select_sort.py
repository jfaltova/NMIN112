import random
import time

def selection_sort(seznam):
    """
    Selection sort: 
    Prochází pole a hledá nejmenší prvek, 
    který následně prohodí s prvním prvkem pole. 
    Tento proces opakuje pro zbytek pole, 
    dokud není celé pole seřazeno.
    """
    s = seznam.copy()
    n = len(s)
    for i in range(n):
        min_i = i
        for j in range(i+1, n):
            if s[j] < s[min_i]:
                min_i = j
        s[i], s[min_i] = s[min_i], s[i]
    return s


def insertion_sort(seznam):
    """
    Insertion sort:
    Prochází pole od druhého prvku,
    uloží aktuální prvek jako klíč,
    porovná klíč s předchozími prvky a 
    posune větší prvky o jednu pozici doprava,
    vloží klíč na správnou pozici a
    tento proces opakuje pro všechny prvky pole.
    """
    s = seznam.copy()
    for i in range(1, len(s)):
        klic = s[i]
        j = i - 1
        while j >= 0 and s[j] > klic:
            s[j+1] = s[j]
            j -= 1
        s[j+1] = klic
    return s

def cas(sort_func, data):
    """Měří čas potřebný k seřazení dat pomocí zadané řadící funkce."""
    start = time.perf_counter()
    sort_func(data)
    end = time.perf_counter()
    return end - start

if __name__ == "__main__":
    """Testování rychlosti řazení pro náhodná data a téměř seřazená data."""

    rozsah = [100, 500, 1000, 2000]  
    print("Test s náhodnými daty:")
    for n in rozsah:
        data = [random.randint(0,10000) for _ in range(n)]

        t1 = cas(selection_sort, data)
        t2 = cas(insertion_sort, data)

        print(f"n={n}: selection: {t1:.4f}, insertion: {t2:.4f}")

    # Test s téměř seřazenými daty
    data = list(range(2000))
    # malá změna
    data[100], data[101] = data[101], data[100]

    print("Test s téměř seřazenými daty:")
    print("selection:", cas(selection_sort, data)) 
    print("insertion:", cas(insertion_sort, data))
