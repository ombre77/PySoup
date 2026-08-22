from pysoup import *

block=material.BlockMaterial("stone")
item=material.ItemMaterial("stick")

pos=locations.BlockPosition(1,1,1)
world=locations.World.OVERWORLD
loc=locations.Location(pos,world)

actions.WorldActions.set_block(block,loc)

loc.position.x+=1
selected=actions.WorldActions.get_block(loc)
