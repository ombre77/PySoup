from dataclasses import dataclass
from typing import Optional
from ..maths.geometry import BlockPosition, Position, Direction
from ..utils import get_server
from ..items.materials import BlockMaterial,EntityMaterial
from ..inventory.player_inventory import PlayerInventory

import java

_Material = java.type("org.bukkit.Material")
_UUID = java.type("java.util.UUID")
_BukkitLocation = java.type("org.bukkit.Location")


@dataclass(frozen=True)
class WorldInstance:
    world:str

    def set_block(self, position: BlockPosition, material: BlockMaterial) -> None:
        """material is a Bukkit Material name, e.g. 'STONE', 'OAK_PLANKS'."""
        bukkit_world = self._bukkit_world()
        block = bukkit_world.getBlockAt(position.x, position.y, position.z)
        block.setType(_Material.valueOf(material.name.upper()))

    def get_block(self,position:BlockPosition) -> "BlockInstance":
        bukkit_world=self._bukkit_world()
        block=bukkit_world.getBlockAt(position.x,position.y,position.z)
        return BlockInstance.from_bukkit(block)

    def summon(self,position:Position,entity:EntityMaterial):
        bukkit_world=self._bukkit_world()
        bukkit_entity_type=java.type("org.bukkit.entity.EntityType").fromName(entity.name)
        entity=bukkit_world.spawnEntity(position.to_bukkit(self._bukkit_world()),bukkit_entity_type)
        return EntityInstance.from_bukkit(entity)

    def _bukkit_world(self):
        bukkit_world = get_server().getWorld(self.world)
        if bukkit_world is None:
            raise ValueError(f"World '{self.world}' is not loaded")
        return bukkit_world

    @classmethod
    def from_bukkit(cls,world):
        return WorldInstance(
            world.getName()
        )


@dataclass(frozen=True)
class EntityInstance:

    entity_id:str

    @classmethod
    def from_bukkit(cls, entity):
        """Wraps a raw Bukkit Entity (e.g. from event.getEntity()) as an EntityInstance."""
        return cls(str(entity.getUniqueId()))

    def _live(self):
        entity = get_server().getEntity(_UUID.fromString(self.entity_id))
        if entity is None or not entity.isValid():
            raise ValueError(f"Entity {self.entity_id} no longer exists")
        return entity

    def is_valid(self) -> bool:
        entity = get_server().getEntity(_UUID.fromString(self.entity_id))
        return entity is not None and entity.isValid()

    def get_position(self) -> Position:
        loc = self._live().getLocation()
        return Position(loc.getX(), loc.getY(), loc.getZ())

    def get_direction(self) -> Direction:
            loc=self._live().getLocation()
            return Direction(loc.getYaw(),loc.getPitch())

    def get_world(self) -> WorldInstance:
        return WorldInstance(self._live().getWorld().getName())

    def teleport(
        self,
        position: Position,
        direction: Optional[Direction] = None,
        world: Optional[WorldInstance] = None,
    ) -> None:
        """Teleports the entity. Stays in its current world unless `world` is given."""
        entity = self._live()
        bukkit_world = world._bukkit_world() if world is not None else entity.getWorld()
        yaw = direction.yaw if direction is not None else 0.0
        pitch = direction.pitch if direction is not None else 0.0
        entity.teleport(_BukkitLocation(bukkit_world, position.x, position.y, position.z, yaw, pitch))

    def remove(self) -> None:
        self._live().remove()

@dataclass(frozen=True)
class PlayerInstance(EntityInstance):

    inventory:PlayerInventory

    def get_inventory(self)->PlayerInventory:
        return self.inventory

    def push_inventory(self):
        self._live().setInventory(self.inventory.to_bukkit())

    def get_name(self) -> str:
        return self._live().getName()

    def send_message(self, message: str) -> None:
        self._live().sendMessage(message)

    @classmethod
    def from_bukkit(cls, entity):
        return cls(str(entity.getUniqueId()),PlayerInventory.from_bukkit(entity.getInventory()))

@dataclass(frozen=True)
class BlockInstance:
    block:BlockMaterial
    position:BlockPosition
    world:WorldInstance

    @classmethod
    def from_bukkit(cls,block):
        return BlockInstance(
            BlockMaterial.from_bukkit(block.getType()),
            BlockPosition.from_bukkit(block.getLocation()),
            WorldInstance.from_bukkit(block.getWorld())
        )

    def set(self,block:BlockMaterial):
        self.world.set_block(self.position,block)