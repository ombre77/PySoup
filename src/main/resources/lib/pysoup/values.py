from dataclasses import dataclass
from .instances import WorldInstance
from .geometry import Position, BlockPosition, Direction

class World:
    Overworld=WorldInstance("world")
    Nether=WorldInstance("world_nether")
    End=WorldInstance("world_the_end")

@dataclass
class Location:
    position:Position
    world:World
    direction:Direction
