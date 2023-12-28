import math

class Vector:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def modulus(self):
        return math.sqrt(self.x**2 + self.y**2)

    def add(self, other_vector):
        new_x = self.x + other_vector.x
        new_y = self.y + other_vector.y
        return Vector(new_x, new_y)

    def __str__(self) -> str:
        return f'{self.x}i + {self.y}j'

a = Vector(3, 4)
b = Vector(1, 1)
print(Vector.add(a, b))

