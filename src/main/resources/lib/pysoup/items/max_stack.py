from .materials import ItemMaterial
from .item_groups import (
    SIGNS, HANGING_SIGNS, TOOLS, ARMOR,
    FILLED_BUCKETS, POTIONS, BOOKS, BOATS_ALL,
    MINECARTS, SHULKER_BOXES, MOB_ARMOR, MISC_UNSTACKABLE,
)

def stackable_to(material:ItemMaterial,amount:int)->bool:
    if amount<0:return False
    if material in _STACK_1:
        return amount<=1
    if material in _STACK_16:
        return amount<=16
    return amount<=64

def get_max_stack_size(material:ItemMaterial)->int:
    if material in _STACK_1:
        return 1
    if material in _STACK_16:
        return 16
    return 64

# 16
_STACK_16: set[ItemMaterial] = {
    ItemMaterial.SNOWBALL,
    ItemMaterial.EGG,
    ItemMaterial.ENDER_PEARL,
    ItemMaterial.BUCKET,
    *SIGNS,
    *HANGING_SIGNS,
    ItemMaterial.HONEY_BOTTLE,
}

# 1
_STACK_1: set[ItemMaterial] = {
    *TOOLS,
    *ARMOR, ItemMaterial.ELYTRA,
    ItemMaterial.SHIELD,
    ItemMaterial.TRIDENT,
    ItemMaterial.BOW,
    ItemMaterial.CROSSBOW,
    ItemMaterial.FISHING_ROD,
    ItemMaterial.FLINT_AND_STEEL,
    ItemMaterial.SHEARS,
    ItemMaterial.CARROT_ON_A_STICK,
    ItemMaterial.WARPED_FUNGUS_ON_A_STICK,
    ItemMaterial.BRUSH,

    *FILLED_BUCKETS,
    *POTIONS,

    *BOOKS,
    *BOATS_ALL,
    *MINECARTS,
    *SHULKER_BOXES,
    *MOB_ARMOR,
    *MISC_UNSTACKABLE,
}