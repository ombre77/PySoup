from locations import Location
from material import EntityMaterial
from helpers.decorators import add_init

@add_init
class Entity:
    entity:EntityMaterial
    location:Location