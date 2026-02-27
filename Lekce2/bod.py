import math

class Bod:
    """Reprezentuje bod v rovině."""

    def __init__(self, x: float, y: float):
        self.x = float(x)
        self.y = float(y)

    def __repr__(self) -> str:
        return f"Bod({self.x:g}, {self.y:g})"

    def __str__(self) -> str:  
        return f"({self.x:g}, {self.y:g})"

    def __eq__(self, other: "Bod") -> bool:
        # TODO
        pass

    def vzdalenost_od_pocatku(self) -> float:
        """Vrátí vzdálenost bodu od počátku."""
        return math.hypot(self.x, self.y)

    def vzdalenost(self, other: "Bod") -> float:
        """Vrátí vzdálenost od jiného bodu."""
        return math.hypot(self.x - other.x, self.y - other.y)

    def posun(self, dx: float, dy: float) -> None:
        """Posune bod o daný vektor."""
        self.x += dx
        self.y += dy

class BarevnyBod(Bod):
    """Bod v rovině, který má navíc barvu."""

    def __init__(self, x: float, y: float, barva: str):
        super().__init__(x, y)
        self.barva = barva

    def __repr__(self) -> str:
        return f"BarevnyBod({self.x:g}, {self.y:g}, '{self.barva}')"
    
    def __str__(self) -> str:
        return f"({self.x:g}, {self.y:g}, '{self.barva}')"
    
