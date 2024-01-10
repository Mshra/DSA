class Vector:
    def __init__(self, x, y, z) -> None:
        self.x = x
        self.y = y
        self.z = z

    def __str__(self) -> str:
        return f'{self.x}i + {self.y}j + {self.z}k'


z = Vector(1, 1, 1)
print(z)
