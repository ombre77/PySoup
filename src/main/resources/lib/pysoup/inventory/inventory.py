from typing import Optional
from ..items.item_stack import ItemStack
from .slot_filter import get_slot_filter
from ..items.max_stack import get_max_stack_size
from ..items.materials import ItemMaterial
from ..items.item_meta import ItemMeta
from ..bukkit import Bukkit


class Inventory:
    def __init__(self, size: int, slot_filters: Optional[dict[int, str]] = None, bukkit_inventory=None) -> None:
        self.size = size
        self.slots: list[Optional[ItemStack]] = [None] * size
        self.slot_filter_ids = slot_filters or {}
        self.bukkit_inventory = bukkit_inventory  # None for a detached/virtual inventory

    def can_place(self, index: int, item: ItemStack) -> bool:
        filter_id = self.slot_filter_ids.get(index)
        if filter_id is None:
            return True
        return get_slot_filter(filter_id)(item)

    def get_slot(self, index: int) -> Optional[ItemStack]:
        return self.slots[index]

    def _push_to_bukkit(self, index: int, item: Optional[ItemStack]) -> None:
        if self.bukkit_inventory is not None:
            self.bukkit_inventory.setItem(index, item.to_bukkit() if item else None)

    def set_slot(self, index: int, item: Optional[ItemStack]) -> None:
        if item is not None and not self.can_place(index, item):
            raise ValueError(f"Item {item.material} is not allowed in slot {index}")
        self.slots[index] = item
        self._push_to_bukkit(index, item)

    def _set_slot_from_event(self, index: int, item: Optional[ItemStack]) -> None:
        """Update slots from a Bukkit-side change (event bridge). Skips push-back to avoid feedback loops."""
        self.slots[index] = item

    def add_item(self, item: ItemStack) -> Optional[ItemStack]:
        """Try to add an ItemStack to the inventory.

        Returns
        - The remaining amount of the item that couldn't be added in the form of an ItemStack
        - None if the item was fully added"""

        remaining = item.amount

        for i, slot in enumerate(self.slots):
            if remaining <= 0:
                break
            if (slot is not None #slot not empty
                and slot.material == item.material #same item
                and slot.meta==item.meta #same meta
                and self.can_place(i, item)): #check filters
                space = get_max_stack_size(item.material) - slot.amount
                if space > 0: #slot not full
                    added = min(space, remaining)
                    slot.amount += added
                    remaining -= added
                    self._push_to_bukkit(i, slot)

        for i, slot in enumerate(self.slots):
            if remaining <= 0:
                break
            if slot is None and self.can_place(i, item):
                place_amount = min(remaining, get_max_stack_size(item.material))
                new_stack = ItemStack(item.material, place_amount,item.meta)
                self.slots[i] = new_stack
                remaining -= place_amount
                self._push_to_bukkit(i, new_stack)

        if remaining <= 0:
            return None
        return ItemStack(item.material, remaining,item.meta)

    def remove_item(self, index: int, amount: int) -> Optional[ItemStack]:
        slot = self.slots[index]
        if slot is None:
            return None
        removed_amount = min(amount, slot.amount)
        removed = ItemStack(slot.material, removed_amount,slot.meta)
        slot.amount -= removed_amount
        if slot.amount <= 0:
            self.slots[index] = None
            self._push_to_bukkit(index, None)
        else:
            self._push_to_bukkit(index, slot)
        return removed

    def find_first(self, material:ItemMaterial,meta:Optional[ItemMeta]=None) -> Optional[int]:
        for i, slot in enumerate(self.slots):
            if (slot is not None #if slot not empty
                and slot.material == material #if is same item
                and (meta is None or slot.meta==meta)): #if same meta
                return i
        return None

    def is_full(self) -> bool:
        return all(
            slot is not None and slot.amount >= get_max_stack_size(slot.material)
            for slot in self.slots
        )

    def refresh(self) -> None:
        """Re-pull slots from the live bukkit inventory (use when external changes may have happened)."""
        if self.bukkit_inventory is None:
            return
        for i in range(self.size):
            self.slots[i] = ItemStack.from_bukkit(self.bukkit_inventory.getItem(i))

    def to_bukkit(self, bukkit_inventory=None):
        """Build/populate a bukkit inventory from current slots. Mainly useful for detached inventories."""
        target = bukkit_inventory or self.bukkit_inventory or Bukkit.createInventory(None, self.size)
        for i, stack in enumerate(self.slots):
            target.setItem(i, stack.to_bukkit() if stack else None)
        return target

    @classmethod
    def from_bukkit(cls, bukkit_inventory, slot_filters: Optional[dict[int, str]] = None) -> "Inventory":
        inv = cls(size=bukkit_inventory.getSize(), slot_filters=slot_filters, bukkit_inventory=bukkit_inventory)
        inv.refresh()
        return inv

    def __iter__(self):
        return iter(self.slots)
