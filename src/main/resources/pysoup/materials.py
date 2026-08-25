from dataclasses import dataclass


@dataclass
class EntityMaterial:
    name:str
    health:int=20

@dataclass
class BlockMaterial:
    name:str
    state:str

@dataclass
class ItemMaterial:
    name:str
    nbt:str