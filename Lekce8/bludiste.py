"""
Hledani nejkratsi cesty v bludisti (pocet kroku od startu do cile)
   '.' značí volné políčko
   'X' značí zeď
   'S' je startovní políčko
   'C' je cílové políčko, ke kterému chceme dojít

Priklad bludiste:
...X....
XXX...X.
..S...XX
XXX..X..
...X..XX
XX...C..
..XXX...
.XX...X.
"""

import sys

class Bludiste:
	def __init__(self):
		# Ctvercove bludiste
		self.mapa = []
		self.rozmer = 0

	def nacti(self):
		# Nacitani pomoci stdin
		for radek in sys.stdin:
			self.mapa.append(list(radek.strip()))
		# Rozmer bludiste
		self.rozmer = len(self.mapa)

	def najdi_start(self):
		for i in range(self.rozmer):
			for j in range(self.rozmer):
				if self.mapa[i][j]=='S':
					return (i,j)

	def cesta(self, r, s, vypis = False):

		# Pomocna funkce: kontrola, jestli nejsme mimo pole
		def zkontroluj_hranice(i1, i2):
			if i1 < 0 or i2 < 0:
				return False
			if i1 >= self.rozmer or i2 >= self.rozmer:
				return False
			return True
		
		# Pomocna funkce: vraci souradnice ciloveho policka
		def najdi_cil():
			for i in range(self.rozmer):
				for j in range(self.rozmer):
					if self.mapa[i][j] == 'C':
						return (i, j)

		# Mozne tahy
		tahy = [(1, 0), (-1, 0), (0, 1), (0, -1)]

		# Vzdalenost pole od startu
		vzdalenost = [[-1]*self.rozmer for _ in range(self.rozmer)]
		
		# Reseni pres frontu
		fronta = []
		fronta.append((r,s))
		vzdalenost[r][s] += 1
		# Souradnice cile
		c1, c2 = najdi_cil()
		print('Souradnice ciloveho policka: ', c1, c2)

		"""
		TODO:
		- Hledani cesty:
			- Odeberte prvek z fronty
			- Vyzkousejte vsechny mozne tahy 
			- Zkontrolujte, jestli nejste v cili
			- Pokud jste na policku jeste nebyli, oznacte si ho,
			ulozte si vzdalenost od startu a pridejte bod do fronty 
		"""

		if vypis:
			pass
			"""
			Zkuste pridat vypis nejkratsi cesty 
			Pokud je moznosti vice, pak vypiste jednu z nich
			- Projdete bludiste od ciloveho policka a hledate policka, 
			ktera jsou o krok blize ke startu
			"""

b = Bludiste()
b.nacti()            
s1, s2 = b.najdi_start()
print("Souradnice startovniho policka: ", s1, s2)
#print("Pocet kroku:" , b.cesta(s1, s2))