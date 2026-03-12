import numpy as np

vektor1 = np.array([1, 2, 3])

# Normalizace vektoru
norma = np.linalg.norm(vektor1)
if norma != 0:
    vektor_normalizovany = vektor1 / norma
    print(f"Normalizovany vektor: {vektor_normalizovany}")
else:
    print("Norma vektoru je nula, nelze normalizovat.")

# Matice tvaru R × S vyplněná číslem X .
R = int(input("Zadejte počet řádků (R): "))
S = int(input("Zadejte počet sloupců (S): "))
X = int(input("Zadejte číslo (X): "))
matice = np.ones((R, S)) * X
print(matice)

# Matice tvaru R × S, která bude mít v i-tém řádku samá čísla i
cisla = np.arange(1, R + 1)
# Jednotkova matice tvaru S × R
matice_jednotkova = np.ones((S, R))
print(matice_jednotkova)
# Vynasobíme jednotkovou matici s vektorem čísel a transponujeme výsledek
matice_2 = (matice_jednotkova * cisla).T
print(matice_2)
