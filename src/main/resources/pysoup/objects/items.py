from material import ItemMaterial
from helpers.decorators import add_init

@add_init
class Item:
    item:ItemMaterial
    amount:int=1