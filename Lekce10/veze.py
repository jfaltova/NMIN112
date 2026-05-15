"""
Spočítejte, kolika způsoby můžeme rozestavět nn šachových věží 
na šachovnici nxn tak, aby se navzájem neohrožovaly.
Pokud je políčko označeno X, znamená to, že tam věž postavit nelze.
Pro vstup

    3
    ...
    ...
    ...
je správný výstup

    6
"""

def nacti_vstup():
    n = int(input())
    board = [list(input().strip()) for _ in range(n)]
    return board

def umisti(i, volne_sloupce, board):
    # umistujeme vez do i-teho radku
    n = len(board)
    if i == n:     # umistili jsme veze do vsech radku, nasli jsme jedno reseni
        return 1
    pocet = 0      # pocet reseni pro i-ty radek
    for j in range(n):                                 # prochazime sloupce                               
        if board[i][j] == '.' and volne_sloupce[j]:    # volne policko a volny sloupec
            board[i][j] = '#'                          # umistime vez
            volne_sloupce[j] = False                   # oznacime sloupec jako obsazeny
            pocet += umisti(i + 1, volne_sloupce, board)   # rekurzivne umistujeme vez do dalsiho radku
            volne_sloupce[j] = True                    # oznacime sloupec jako volny                                     
            board[i][j] = '.'                          # odstranime vez
    return pocet      # vratime pocet reseni pro i-ty radek

mapa = nacti_vstup()

volne_sloupce = [True] * len(mapa) 
pocet = umisti(0, volne_sloupce, mapa)
print(pocet)
