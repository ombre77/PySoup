from typing import Optional
from ..items.item_stack import ItemStack
from ..inventory.inventory import Inventory

# Bukkit's PlayerInventory layout: 
# 0-8 are hotbar, 9-35 are main storage,
# 36-39 are armor, 40 is offhand
HOTBAR_RANGE = range(0, 9)
MAIN_STORAGE_RANGE = range(9, 36)
ARMOR_RANGE = range(36, 40)  # 36=boots, 37=leggings, 38=chestplate, 39=helmet
OFFHAND_SLOT = 40

PLAYER_INVENTORY_SIZE = 41

class PlayerInventory(Inventory):
    def __init__(self, slot_filters: Optional[dict[int, str]] = None, bukkit_inventory=None) -> None:
        super().__init__(size=PLAYER_INVENTORY_SIZE, slot_filters=slot_filters, bukkit_inventory=bukkit_inventory)
        self.held_slot: int = 0

    def get_held_item(self) -> Optional[ItemStack]:
        return self.get_slot(self.held_slot)

    def set_held_item(self, item: Optional[ItemStack]) -> None:
        self.set_slot(self.held_slot, item)

    def get_hotbar(self) -> list[Optional[ItemStack]]:
        return [self.slots[i] for i in HOTBAR_RANGE]

    def get_helmet(self) -> Optional[ItemStack]:
        return self.get_slot(39)

    def set_helmet(self, item: Optional[ItemStack]) -> None:
        self.set_slot(39, item)

    def get_chestplate(self) -> Optional[ItemStack]:
        return self.get_slot(38)

    def set_chestplate(self, item: Optional[ItemStack]) -> None:
        self.set_slot(38, item)

    def get_leggings(self) -> Optional[ItemStack]:
        return self.get_slot(37)

    def set_leggings(self, item: Optional[ItemStack]) -> None:
        self.set_slot(37, item)

    def get_boots(self) -> Optional[ItemStack]:
        return self.get_slot(36)

    def set_boots(self, item: Optional[ItemStack]) -> None:
        self.set_slot(36, item)

    def get_armor_contents(self) -> list[Optional[ItemStack]]:
        return [self.slots[i] for i in ARMOR_RANGE]

    def get_offhand(self) -> Optional[ItemStack]:
        return self.get_slot(OFFHAND_SLOT)

    def set_offhand(self, item: Optional[ItemStack]) -> None:
        self.set_slot(OFFHAND_SLOT, item)

    @classmethod
    def from_bukkit(cls, bukkit_inventory, slot_filters: Optional[dict[int, str]] = None) -> "PlayerInventory":
        inv = cls(slot_filters=slot_filters, bukkit_inventory=bukkit_inventory)
        inv.refresh()
        inv.held_slot = bukkit_inventory.getHeldItemSlot()
        return inv