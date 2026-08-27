from dataclasses import dataclass
from typing import overload
import math
import java

@dataclass
class Vector3:
    x:float
    y:float
    z:float

    def __add__(self, other: "Vector3") -> "Vector3":
        return Vector3(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other: "Vector3") -> "Vector3":
        return Vector3(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, scalar: float) -> "Vector3":
        return Vector3(self.x * scalar, self.y * scalar, self.z * scalar)

    __rmul__ = __mul__

    def __truediv__(self, scalar: float) -> "Vector3":
        return Vector3(self.x / scalar, self.y / scalar, self.z / scalar)

    def __neg__(self) -> "Vector3":
        return Vector3(-self.x, -self.y, -self.z)

    def dot(self, other: "Vector3") -> float:
        return self.x * other.x + self.y * other.y + self.z * other.z

    def cross(self, other: "Vector3") -> "Vector3":
        return Vector3(
            self.y * other.z - self.z * other.y,
            self.z * other.x - self.x * other.z,
            self.x * other.y - self.y * other.x,
        )

    def length(self) -> float:
        return math.sqrt(self.dot(self))

    def length_squared(self) -> float:
        """Cheaper than length() when you only need to compare distances -
        skips the sqrt."""
        return self.dot(self)

    def normalized(self) -> "Vector3":
        length = self.length()
        if length == 0:
            raise ValueError("Cannot normalize a zero-length vector")
        return self / length

    def distance_to(self, other: "Vector3") -> float:
        return (self - other).length()

    def as_tuple(self) -> tuple[float, float, float]:
        return (self.x, self.y, self.z)

    @classmethod
    def zero(cls) -> "Vector3":
        return cls(0.0, 0.0, 0.0)


@dataclass
class Position:
    x:float
    y:float
    z:float

    def to_vector(self) -> "Vector3":
        return Vector3(self.x, self.y, self.z)

    def ceil(self)->"Position":
        return Position(
            math.ceil(self.x),
            math.ceil(self.y),
            math.ceil(self.z)
        )
    
    def to_block_pos(self) -> "BlockPosition":
        return BlockPosition(
            math.floor(self.x),
            math.floor(self.y),
            math.floor(self.z)
        )

    @staticmethod
    def from_vector(vector3:"Vector3")->"Position":
        return Position(vector3.x,vector3.y,vector3.z)

    @overload
    def __add__(self,other:"Position") -> "Position":...

    @overload
    def __add__(self,other:"Vector3") -> "Position":...

    def __add__(self, other:"Position|Vector3") :
        return Position(self.x + other.x, self.y + other.y, self.z + other.z)

    @overload
    def __sub__(self, other: "Position") -> Vector3: ...
    @overload
    def __sub__(self, other: Vector3) -> "Position": ...

    def __sub__(self, other):
        """Position - Position = Vector3 (the displacement between them).
        Position - Vector3 = Position (moved backwards by the displacement)."""
        if isinstance(other, Position):
            return Vector3(self.x - other.x, self.y - other.y, self.z - other.z)
        return Position(self.x - other.x, self.y - other.y, self.z - other.z)

    def distance_to(self, other: "Position") -> float:
        distance: Vector3 = self - other
        return distance.length()

    @classmethod
    def from_bukkit(cls,location):
        return cls(location.x(),location.y(),location.z())

    def to_bukkit(self, world):
        Location = java.type("org.bukkit.Location")
        return Location(world, self.x, self.y, self.z)

@dataclass
class BlockPosition(Position):
    x:int
    y:int
    z:int

@dataclass
class Direction:
    yaw:float
    pitch:float

    def __add__(self, other: "Direction") -> "Direction":
        return Direction(self.yaw + other.yaw, self.pitch + other.pitch)

    def __sub__(self, other: "Direction") -> "Direction":
        return Direction(self.yaw - other.yaw, self.pitch - other.pitch)

    def to_vector(self) -> Vector3:
        """Unit vector this yaw/pitch points towards - matches Bukkit's
        Location.getDirection()."""
        yaw_rad = math.radians(self.yaw)
        pitch_rad = math.radians(self.pitch)
        xz = math.cos(pitch_rad)
        return Vector3(
            -xz * math.sin(yaw_rad),
            -math.sin(pitch_rad),
            xz * math.cos(yaw_rad),
        )

    @classmethod
    def from_vector(cls, vector: Vector3) -> "Direction":
        """Inverse of to_vector() - matches Bukkit's Location.setDirection().

        Yaw is undefined for a purely vertical vector, so defaults to 0.0."""
        if vector.x == 0 and vector.z == 0:
            return cls(0.0, -90.0 if vector.y > 0 else 90.0)

        two_pi = 2 * math.pi
        theta = math.atan2(-vector.x, vector.z)
        yaw = math.degrees((theta + two_pi) % two_pi)

        xz = math.sqrt(vector.x ** 2 + vector.z ** 2)
        pitch = math.degrees(math.atan(-vector.y / xz))

        return cls(yaw, pitch)
