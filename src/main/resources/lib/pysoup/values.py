from dataclasses import dataclass
from .instances.instances import WorldInstance
from .maths.geometry import Position, BlockPosition, Direction

class World:
    Overworld=WorldInstance("world")
    Nether=WorldInstance("world_nether")
    End=WorldInstance("world_the_end")
