from objects.blocks import Block as _Block
from material import BlockMaterial as _BlockMaterial
from locations import Location as _Location
from locations import BlockPosition as _BlockPosition
from enum import Enum as _Enum
import _pysoup_internal # type: ignore


class WorldActions:
    @staticmethod
    def set_block(block:_BlockMaterial,location:_Location):
        """Sets the block in a specific location"""
        if not isinstance(location.position,_BlockPosition):
            raise Exception("Position of location for set_block must be BlockPosition!")
        _pysoup_internal.world.setBlock(
            location.world.name,location.position.x,location.position.y,location.position.z
            ,block._to_bukkit_material()
        )

    @staticmethod
    def get_block(location:_Location)->_Block:
        """Gets the Block instance at a given location"""
        if not isinstance(location.position,_BlockPosition):
            raise Exception("Position of location for get_block must be BlockPosition!")
        bkBlock=_pysoup_internal.world.getBlock(location.world.name,location.position.x,location.position.y,location.position.z)
        return _Block._from_bukkit(bkBlock)

class PluginActions:

    class LogLevel(_Enum):
        INFO=1
        WARN=2

    @staticmethod
    def log(level:LogLevel,content:str):
        """Sends a message in the server log"""
        _pysoup_internal.plugin.log(level.value,content)