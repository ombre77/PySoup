import math
from dataclasses import dataclass

@dataclass
class Vector3:
    x:float
    y:float
    z:float

    def __add__(self, other: "Vector3") -> "Vector3":
        if not isinstance(other, Vector3):
            raise Exception(f"Cannot add Vector3 and {type(other).__name__}")
        return Vector3(
            self.x + other.x,
            self.y + other.y,
            self.z + other.z
        )

    def __sub__(self, other: "Vector3") -> "Vector3":
        if not isinstance(other, Vector3):
            raise Exception(f"Cannot subtract {type(other).__name__} from Vector3")
        return Vector3(
            self.x - other.x,
            self.y - other.y,
            self.z - other.z
        )

    def __mul__(self, scalar: float) -> "Vector3":
        if not isinstance(scalar, (int, float)):
            raise Exception(f"Cannot multiply Vector3 by {type(scalar).__name__}")
        return Vector3(self.x * scalar, self.y * scalar, self.z * scalar)

    __rmul__ = __mul__

    def __truediv__(self, scalar: float) -> "Vector3":
        if not isinstance(scalar, (int, float)):
            raise Exception(f"Cannot divide Vector3 by {type(scalar).__name__}")
        if scalar == 0:
            raise Exception("Cannot divide Vector3 by zero")
        return Vector3(self.x / scalar, self.y / scalar, self.z / scalar)

    def __neg__(self) -> "Vector3":
        return Vector3(-self.x, -self.y, -self.z)

    def length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

    def length_squared(self) -> float:
        # avoids the sqrt when you only need to compare magnitudes
        return self.x ** 2 + self.y ** 2 + self.z ** 2

    def normalize(self) -> "Vector3":
        length = self.length()
        if length == 0:
            raise Exception("Cannot normalize a zero-length Vector3")
        return Vector3(self.x / length, self.y / length, self.z / length)

    def dot(self, other: "Vector3") -> float:
        if not isinstance(other, Vector3):
            raise Exception(f"Cannot dot Vector3 and {type(other).__name__}")
        return self.x * other.x + self.y * other.y + self.z * other.z

    def cross(self, other: "Vector3") -> "Vector3":
        if not isinstance(other, Vector3):
            raise Exception(f"Cannot cross Vector3 and {type(other).__name__}")
        return Vector3(
            self.y * other.z - self.z * other.y,
            self.z * other.x - self.x * other.z,
            self.x * other.y - self.y * other.x
        )

    def distance_to(self, other: "Vector3") -> float:
        if not isinstance(other, Vector3):
            raise Exception(f"Cannot get distance between Vector3 and {type(other).__name__}")
        return (self - other).length()

    def lerp(self, other: "Vector3", t: float) -> "Vector3":
        if not isinstance(other, Vector3):
            raise Exception(f"Cannot lerp Vector3 and {type(other).__name__}")
        return self + (other - self) * t

    @classmethod
    def zero(cls) -> "Vector3":
        return cls(0.0, 0.0, 0.0)