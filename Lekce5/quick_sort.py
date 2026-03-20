import random
import time

def quick_sort(seznam):
    """Quick sort:
    Princip: Výběr pivotu a rozdělení pole na části menší a větší než pivot, rekurzivní řešení.
    Postup:
    1. Vybereme pivot (například prostřední prvek pole).
    2. Rozdělíme pole na tři části: prvky menší než pivot, 
    prvky rovné pivotu a prvky větší než pivot.
    3. Rekurzivně seřadíme části menší a větší než pivot.
    4. Sléváme seřazené části a pivot do jednoho seřazeného pole.
    5. Tento proces opakujeme, dokud není celé pole seřazeno.
    """

    if len(seznam) <= 1:
        return seznam

    pivot = seznam[len(seznam)//2]

    left = [x for x in seznam if x < pivot]
    middle = [x for x in seznam if x == pivot]
    right = [x for x in seznam if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)

def quick_sort_pivot(seznam, pivot_index):
    """Quick sort s výběrem pivotu podle indexu.
    Pokud je index 0: výběr prvního prvku pole jako pivotu.
    Pokud je index 1: výběr prostředního prvku pole jako pivotu.
    Pokud je index 2: výběr posledního prvku pole jako pivotu."""
    if len(seznam) <= 1:
        return seznam

    if pivot_index == 0:
        pivot_i = 0
    elif pivot_index == 1:
        pivot_i = len(seznam) // 2
    elif pivot_index == 2:
        pivot_i = len(seznam) - 1
    else:
        raise ValueError("Neplatný index pivotu. Použijte 0, 1 nebo 2.")
    pivot = seznam[pivot_i]

    left = [x for x in seznam if x < pivot]
    middle = [x for x in seznam if x == pivot]
    right = [x for x in seznam if x > pivot]

    return quick_sort_pivot(left, pivot_index) + middle + quick_sort_pivot(right, pivot_index)

def quick_sort_iter(seznam):
    """
    Iterativní verze quick sortu:
    Princip: Výběr pivotu a rozdělení pole na části menší a
      větší než pivot, iterativní řešení.
    Postup:
    1. Vybereme pivot (například prostřední prvek pole).
    2. Rozdělíme pole na tři části: prvky menší než pivot, 
      prvky rovné pivotu a prvky větší než pivot.
    3. Použijeme zásobník pro iterativní zpracování částí pole.
    4. Tento proces opakujeme, dokud není celé pole seřazeno.
    """
    s = seznam.copy()
    stack = [(0, len(s)-1)]

    while stack:
        low, high = stack.pop()

        if low < high:
            p = partition(s, low, high)

            stack.append((low, p-1))
            stack.append((p+1, high))

    return s


def partition(s, low, high):
    pivot = s[high//2]
    i = low

    for j in range(low, high):
        if s[j] < pivot:
            s[i], s[j] = s[j], s[i]
            i += 1

    s[i], s[high] = s[high], s[i]
    return i

def cas(sort_func, data):
    """Měří čas potřebný k seřazení dat pomocí zadané řadící funkce."""
    start = time.perf_counter()
    sort_func(data)
    end = time.perf_counter()
    return end - start

if __name__ == "__main__":
    """Testování quick sortu a quick sortu iterativně:"""
    rozsah = [1000, 2000, 4000, 8000]

    for n in rozsah:
        print(f"Velikost pole: {n}")
        data = [random.randint(0,100000) for _ in range(n)]
        print(f"Quick sort: {cas(quick_sort, data)}")
        print(f"Quick sort iter: {cas(quick_sort_iter, data)}")
        for i in range(3):
            print(f"Quick sort pivot {i}: {cas(lambda d: quick_sort_pivot(d, i), data)}")

     # Test s téměř seřazenými daty
    data = list(range(500))
    # malá změna
    data[100], data[101] = data[101], data[100]

    print("Test s téměř seřazenými daty:")
    for i in range(3):
        print(f"Quick sort pivot {i}: {cas(lambda d: quick_sort_pivot(d, i), data)}")
   

