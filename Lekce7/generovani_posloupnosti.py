"""
Vygenerujte všechny posloupnosti čísel 0 a 1 délky *n*

Další pod-úlohy
- Zjistěte počet posloupností z tohoto příkladu bez toho, abyste je generovali
- Generujte pouze takové posloupnosti, kde je právě *k* jedniček.
"""

def posloupnost(n, p):
    if n == 0:
        print("".join(map(str, p)))
    else:
        posloupnost(n-1, p + [0])
        posloupnost(n-1, p + [1])

def pocet(n):
    if n == 0:
        return 1
    else:
        return 2 * pocet(n-1)

def posloupnost_k(n, k, p):
    if n == 0:
        if k == 0:
            print("".join(map(str, p)))
    else:
        if k < n:
            posloupnost_k(n-1, k, p + [0])
        if k > 0:
            posloupnost_k(n-1, k-1, p + [1])

if __name__ == "__main__":
    n = int(input("Zadejte delku posloupnosti "))
    posloupnost(n, [])
    print(f"Pocet posloupnosti: {pocet(n)}")
    k = int(input("Zadejte pocet jednicek "))
    posloupnost_k(n, k, [])
    
