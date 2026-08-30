from typing import Callable
from ..items.item_stack import ItemStack
from ..items.item_groups import FUEL_MATERIAL
from ..items.materials import ItemMaterial

SlotFilterFunc=Callable[[ItemStack],bool]

_REGITRY:dict[str,SlotFilterFunc]={}

def slot_filter(id:str):
    def decorator(func:SlotFilterFunc)->SlotFilterFunc:
        if id in _REGITRY:
            raise ValueError(f"Slot filter '{id}' already registered")
        _REGITRY[id]=func
        return func
    return decorator


def get_slot_filter(id:str)->SlotFilterFunc:
    return _REGITRY[id]

#Slot filters

@slot_filter("blank")
def is_all(item:ItemStack)->bool:
    return item.material in ItemMaterial

# Furnaces
@slot_filter("fuel")
def is_fuel(item:ItemStack)->bool:
    return item.material in FUEL_MATERIAL