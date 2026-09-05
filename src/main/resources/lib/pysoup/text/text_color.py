from __future__ import annotations
from enum import Enum
from dataclasses import dataclass
from typing import ClassVar,overload

@dataclass(frozen=True)
class Color:
    r:int
    g:int
    b:int

    def __post_init__(self):
        for c in self.values():
            if not 0<=c<=255:
                raise ValueError(f"Color channel out of range (0-255): {c}")

    def values(self)->tuple[int,int,int]:
        return (self.r,self.g,self.b)

    @classmethod
    def of(cls,r:int,g:int,b:int)->"Color":
        return cls(r,g,b)

    @classmethod
    def from_hex(cls,hex:str)->"Color":
        hex=hex.strip("#")
        if len(hex)!=6:
            raise ValueError(f"Invalid hex color: {hex}")
        return cls(int(hex[0:2],16),int(hex[2:4],16),int(hex[4:6],16))

    def to_hex(self)->str:
        return f"#{self.r:02x}{self.g:02x}{self.b:02x}"

    def as_int(self)->int:
        return (self.r<<16) | (self.g<<8) | (self.b)

    def lerp(self, other: "Color", t: float) -> "Color":
        t = max(0.0, min(1.0, t))
        return Color(
            round(self.r + (other.r - self.r) * t),
            round(self.g + (other.g - self.g) * t),
            round(self.b + (other.b - self.b) * t),
        )

    def nearest_named(self) -> "NamedColor":
        return min(NamedColor, key=lambda n: n._distance_sq(self))

    def _distance_sq(self, other: "Color") -> int:
        return (self.r - other.r) ** 2 + (self.g - other.g) ** 2 + (self.b - other.b) ** 2

    @overload
    def __add__(self,other:"Color")->"Color":
        ...

    @overload
    def __add__(self,other:int)->"Color":
        ...

    def __add__(self, other):
        if isinstance(other,int):
            return Color(self.r+other,self.g+other,self.b+other)
        elif isinstance(other,"Color"):
            return Color(self.r+other.r,self.g+other.g,self.b+other.b)

    @classmethod
    def from_int(cls, value: int) -> "Color":
        return cls((value >> 16) & 0xFF, (value >> 8) & 0xFF, value & 0xFF)

class NamedColor(Color,Enum):
    def __new__(cls, r, g, b, legacy_char):
        obj = object.__new__(cls)
        object.__setattr__(obj, "r", r)   # since Color is frozen, must edit attr this way
        object.__setattr__(obj, "g", g)
        object.__setattr__(obj, "b", b)
        object.__setattr__(obj, "legacy_char", legacy_char)
        obj._value_ = legacy_char
        return obj

    def __init__(self, *args):
        pass  # attrs already set in __new__ — Color's dataclass __init__ would choke on 4 args

    BLACK        = (0, 0, 0, "0")
    DARK_BLUE    = (0, 0, 170, "1")
    DARK_GREEN   = (0, 170, 0, "2")
    DARK_AQUA    = (0, 170, 170, "3")
    DARK_RED     = (170, 0, 0, "4")
    DARK_PURPLE  = (170, 0, 170, "5")
    GOLD         = (255, 170, 0, "6")
    GRAY         = (170, 170, 170, "7")
    DARK_GRAY    = (85, 85, 85, "8")
    BLUE         = (85, 85, 255, "9")
    GREEN        = (85, 255, 85, "a")
    AQUA         = (85, 255, 255, "b")
    RED          = (255, 85, 85, "c")
    LIGHT_PURPLE = (255, 85, 255, "d")
    YELLOW       = (255, 255, 85, "e")
    WHITE        = (255, 255, 255, "f")

    @classmethod
    def from_legacy_char(cls, char: str) -> "NamedColor":
        return cls(char.strip("§"))
