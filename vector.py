from dataclasses import dataclass


@dataclass
class Vector:
    x: float
    y: float
    
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def __mul__(self, scalar: float):
        return Vector(self.x * scalar, self.y * scalar)
    
    def __rmul__(self, scalar: float):
        return self.__mul__(scalar)
    
    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)
    
    def get_tuple(self) -> tuple[float, float]:
        return self.x, self.y