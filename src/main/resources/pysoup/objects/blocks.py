from locations import BlockPosition,World,Location
from material import BlockMaterial

import _pysoup_internal # type: ignore

class Block:
    postion: BlockPosition
    world:World
    material: BlockMaterial

    def __init__(self,position:BlockPosition,world:World,material:BlockMaterial) -> None:
        self.postion=position
        self.world=world
        self.material=material
    
    @classmethod
    def _from_bukkit(cls, bukkit_block):
        world=World(bukkit_block.getWorld().getName())
        position=BlockPosition(
            x=bukkit_block.getX(),
            y=bukkit_block.getY(),
            z=bukkit_block.getZ()
        )
    
        material = BlockMaterial._from_bukkit(bukkit_block.getType())
        return cls(position,world,material)