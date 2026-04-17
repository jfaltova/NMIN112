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

	def start(self):
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
		def cil():
			for i in range(self.rozmer):
				for j in range(self.rozmer):
					if self.mapa[i][j] == 'C':
						return (i, j)

		# Mozne tahy
		tahy = [(1, 0), (-1, 0), (0, 1), (0, -1)]
		# Vzdalenost pole od startu
		vzdalenost = [[-1]*self.rozmer for _ in range(self.rozmer)]
		fronta = []
		fronta.append((r,s))
		vzdalenost[r][s] += 1
		# Souradnice cile
		c1, c2 = cil()
		print('Souradnice ciloveho policka: ', c1, c2)

		while fronta:
			#print(fronta)
			r, s = fronta.pop(0)
			krok = vzdalenost[r][s] + 1
			# Vyzkousime mozne tahy
			for (i, j) in tahy:
				rr = r+i
				ss = s+j
				if zkontroluj_hranice(rr,ss):
					if self.mapa[rr][ss] == 'C':       # Jsme v cili, pruchod konci
						vzdalenost[rr][ss] = krok
						return vzdalenost[rr][ss]
					if self.mapa[rr][ss] == '.':      # Pokud jsme na policku jeste nebyli:
						self.mapa[rr][ss] = 'o'       # - oznacime ho, ulozime vzdalenost a pridame do fronty
						vzdalenost[rr][ss] = krok
						fronta.append((rr,ss))

		return -1   # Nenalezena zadna cesta

b = Bludiste()
b.nacti()          
s1, s2 = b.start()
print(f"Souradnice startovniho policka: {s1}, {s2}")
print(f"Pocet kroku: {b.cesta(s1, s2)}")
