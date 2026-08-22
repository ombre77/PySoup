from dataclasses import dataclass
from enum import Enum
from math_utils import Vector3


@dataclass
class Position:
    x:float
    y:float
    z:float

    @classmethod
    def from_vector3(cls,vector3:Vector3)->"Position":
        return Position(vector3.x,vector3.y,vector3.z)

    @property
    def vector3(self)->Vector3:
        return Vector3(self.x,self.y,self.z)

@dataclass
class BlockPosition(Position):
    x:int
    z:int
    y:int

    @classmethod
    def from_vector3(cls,vector3:Vector3)->"Position":
        return Position(int(vector3.x),int(vector3.y),int(vector3.z))

    @property
    def vector3(self)->Vector3:
        return Vector3(self.x,self.y,self.z)

class World(Enum):
    OVERWORLD="world"
    NETHER="world_the_nether"
    END="world_the_end"

@dataclass
class Location:
    position:Position
    world:World