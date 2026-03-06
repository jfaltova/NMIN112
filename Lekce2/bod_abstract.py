import math

class Bod:
    """Reprezentuje abstraktní třídu bodů.
    Bod2D a Bod3D jsou konkrétní implementace, které dědí z této třídy.
    """
    def __repr__(self) -> str:
        raise NotImplementedError("Tato metoda musí být implementována v podtřídě.")
    def __str__(self) -> str:
        raise NotImplementedError("Tato metoda musí být implementována v podtřídě.")    
    def vzdalenost_od_pocatku(self) -> float:
        """Vrátí vzdálenost bodu od počátku."""
        raise NotImplementedError("Tato metoda musí být implementována v podtřídě.")
    def vzdalenost(self, other: "Bod") -> float:
        """Vrátí vzdálenost od jiného bodu."""
        raise NotImplementedError("Tato metoda musí být implementována v podtřídě.")
    def posun(self, dx: float, dy: float) -> None:
        """Posune bod o daný vektor."""
        raise NotImplementedError("Tato metoda musí být implementována v podtřídě.")

class Bod2D(Bod):
    """Reprezentuje bod v rovině."""
    def __init__(self, x: float, y: float):
        self.x = float(x)
        self.y = float(y)
    def __repr__(self) -> str:
        return f"Bod2D({self.x:g}, {self.y:g})"
    def __str__(self) -> str:  
        return f"({self.x:g}, {self.y:g})"
    def vzdalenost_od_pocatku(self) -> float:
        """Vrátí vzdálenost bodu od počátku."""
        return math.hypot(self.x, self.y)
    def vzdalenost(self, other: "Bod2D") -> float:
        """Vrátí vzdálenost od jiného bodu."""
        return math.hypot(self.x - other.x, self.y - other.y)
    def posun(self, dx: float, dy: float) -> None:
        """Posune bod o daný vektor."""
        self.x += dx
        self.y += dy
    
class Bod3D(Bod):
    """Bod v prostoru."""
    def __init__(self, x: float, y: float, z: float):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)
    def __repr__(self) -> str:
        return f"Bod3D({self.x:g}, {self.y:g}, {self.z:g})"
    def __str__(self) -> str:
        return f"({self.x:g}, {self.y:g}, {self.z:g})"
    def vzdalenost_od_pocatku(self) -> float:
        """Vrátí vzdálenost bodu od počátku."""
        return math.sqrt(self.x**2 + self.y**2 + self.z**2) 
    def vzdalenost(self, other: "Bod3D") -> float:
        """Vrátí vzdálenost od jiného bodu."""
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2 + (self.z - other.z)**2)
    
