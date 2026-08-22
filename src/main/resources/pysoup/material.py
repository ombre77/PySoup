from dataclasses import dataclass
import _pysoup_internal # type: ignore

@dataclass
class BlockMaterial:
    block:str

    def _to_bukkit_material(self):
        _pysoup_internal.resolver.resolveMaterial(self.block)

    @classmethod
    def _from_bukkit(cls,bukkit_material)->"BlockMaterial":
        return cls(bukkit_material.name())


@dataclass
class EntityMaterial:
    entity:str
    health:float=20

@dataclass
class ItemMaterial:
    item:str
    name:str|None=None
