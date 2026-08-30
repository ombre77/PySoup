from dataclasses import dataclass,field
from .materials import ItemMaterial
from ..bukkit import BukkitItemStack
from .enchantments import Enchantment
from typing import Optional
from .item_meta import ItemMeta

@dataclass
class ItemStack:
    material: ItemMaterial
    amount: int = 1
    meta: ItemMeta = field(default_factory=ItemMeta)

    def to_bukkit(self):
        bukkit_material = self.material.to_bukkit()
        stack = BukkitItemStack(bukkit_material, self.amount)
        bukkit_meta = stack.getItemMeta()
        if bukkit_meta is not None:
            self.meta.apply_to_bukkit(bukkit_meta)
            stack.setItemMeta(bukkit_meta)
        return stack

    @classmethod
    def from_bukkit(cls, bukkit_stack) -> Optional["ItemStack"]:
        if bukkit_stack is None:
            return None
        material = ItemMaterial.from_bukkit(bukkit_stack.getType())
        meta = ItemMeta.from_bukkit(bukkit_stack.getItemMeta())
        return cls(material, bukkit_stack.getAmount(), meta)