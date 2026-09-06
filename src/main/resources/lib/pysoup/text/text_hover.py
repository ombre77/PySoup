from __future__ import annotations
from dataclasses import dataclass
from enum import Enum
from typing import Optional,TYPE_CHECKING
from uuid import UUID
from ..bukkit import AdventureKey,AdventureHoverEvent,JavaUUID

if TYPE_CHECKING:
    from .component import Component
    from ..items.materials import ItemMaterial,EntityMaterial

class HoverAction(Enum):
    SHOW_TEXT="show_text"
    SHOW_ITEM="show_item"
    SHOW_ENTITY="show_entity"

@dataclass(frozen=True)
class ShowText:
    component:"Component"

    def to_adventure(self):
        return self.component.to_adventure()

@dataclass(frozen=True)
class ShowItem:
    material:"ItemMaterial"
    count:int =1

    def to_adventure(self):
        key=AdventureKey.key(self.material.to_bukkit_key())
        return AdventureHoverEvent.showItem(key,self.count)

@dataclass(frozen=True)
class ShowEntity:
    entity:"EntityMaterial"
    uuid: UUID
    name: Optional["Component"] = None

    def to_adventure(self):
        key = AdventureKey.key(self.entity.to_bukkit_key())
        java_uuid = JavaUUID.fromString(str(self.uuid))
        adventure_name = self.name.to_adventure() if self.name is not None else None
        return AdventureHoverEvent.showEntity(key, java_uuid, adventure_name)


@dataclass(frozen=True)
class HoverEvent:
    content: ShowText | ShowItem | ShowEntity

    @classmethod
    def show_text(cls, component: "Component") -> "HoverEvent":
        return cls(ShowText(component))

    @classmethod
    def show_item(cls, material: "ItemMaterial", count: int = 1) -> "HoverEvent":
        return cls(ShowItem(material, count))

    @classmethod
    def show_entity(cls, entity:"EntityMaterial", uuid: UUID, name: Optional["Component"] = None) -> "HoverEvent":
        return cls(ShowEntity(entity, uuid, name))

    def to_adventure(self):
        return self.content.to_adventure()