from dataclasses import dataclass
from enum import Enum
from instances import WorldInstance

class World(Enum):
    Overworld=WorldInstance("world")
    Nether=WorldInstance("world_the_nether")
    End=WorldInstance("world_the_end")

@dataclass
class Position:
    x:float
    y:float
    z:float

@dataclass
class BlockPosition(Position):
    x:int
    y:int
    z:int

@dataclass
class Direction:
    yaw:float
    pitch:float

@dataclass
class Location:
    position:Position
    world:World
    direction:Direction