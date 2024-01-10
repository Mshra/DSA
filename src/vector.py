import math


class Vector:
    def __init__(self, x=0, y=0, z=0) -> None:
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        new_x = self.x + other.x
        new_y = self.y + other.y
        new_z = self.z + other.z
        return Vector(new_x, new_y, new_z)

    def __sub__(self, other):
        new_x = self.x - other.x
        new_y = self.y - other.y
        new_z = self.z - other.z
        return Vector(new_x, new_y, new_z)

    def modulus(self):
        mod = math.sqrt((self.x*self.x) + (self.y*self.y) + (self.z * self.z))
        return f'{mod} units'

    def __str__(self) -> str:
        return f'({self.x})i + ({self.y})j + ({self.z})k'
