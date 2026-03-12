import matplotlib.pyplot as plt
import numpy as np

"""
Vykreslete do jednoho obrázku funkci sin(x) a 
několik členů jejího Taylorova rozvoje v okolí bodu x = 0 
na intervalu [-3, 3].
"""
def plot_taylor():
    x = np.linspace(-3, 3, 400)
    plt.plot(x, np.sin(x), label='sin(x)')
    plt.plot(x, x, label='1. stupeň')
    plt.plot(x, x - x**3 / 6, label='3. stupeň')
    plt.plot(x, x - x**3 / 6 + x**5 / 120, label='5. stupeň')
    plt.legend()
    plt.title('Taylorův rozvoj sin(x) kolem x=0')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.grid()
    plt.savefig('taylor.png')
    plt.show()

"""
Vygenerujte náhodné koeficienty v rozumném rozsahu pro polynom 
5. stupně. Vykreslete tento polynom v intervalu [-3, 3].
"""

def plot_polynom(stupen):
    x = np.linspace(-3, 3, 1000)
    # náhodné koeficienty (mezi 0 a 1)
    koeficienty = np.random.uniform(0, 1, stupen + 1)  
    print(f"Koeficienty polynomu {stupen}. stupně: {koeficienty}")
    y = np.polyval(koeficienty, x)  # vyhodnocení polynomu
    plt.plot(x, y, label=f'Polynom {stupen}. stupně')
    plt.legend()
    plt.title(f'Polynom {stupen}. stupně')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.grid()
    plt.savefig(f'polynom_{stupen}.png')
    plt.show()
    
"""
Vykreslete kružnici a přímku do jednoho obrázku. 
Střed kružnice a přímku zadá uživatel. Pohledem zjistěte, 
jestli zadaná přímka protíná kružnici.
"""

def plot_circle_and_line():
    # Přímka ve tvaru y = mx + k
    m = float(input(f"Zadejte směrnici přímky: "))
    k = float(input(f"Zadejte průsečík s osou y: "))
    y_line = m * x + k
    x = np.linspace(-r-1, r+1, 100)
    plt.plot(x, y_line, label='Přímka')
    
    #Kružnice se středem v počátku a poloměrem r
    r = int(input(f"Zadejte poloměr kružnice: "))
    """
    # Jedna možnost
    circle = plt.Circle((0, 0), r, color='orange', fill=False, label='Kružnice')
    plt.gca().add_artist(circle)
    """
    # Druhá možnost
    t = np.linspace(0,2*np.pi,400)
    x_c = np.cos(t)
    y_c = np.sin(t)
    plt.plot(x_c, y_c, label='Kružnice')

    plt.legend()
    plt.title('Kružnice a přímka')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.axis("equal")
    plt.grid()
    plt.savefig('kruznice.png')
    plt.show()

if __name__ == "__main__":
    plot_taylor()
    plot_polynom(5)
    plot_circle_and_line()