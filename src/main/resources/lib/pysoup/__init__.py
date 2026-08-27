import polyglot
from . import events as _events
from . import utils as _utils
from .events import Event, on_event,EventInfos
from .utils import log, get_server,broadcast
from .values import Position,BlockPosition,World,Direction,Location
from .instances import WorldInstance, EntityInstance
from .materials import BlockMaterial,EntityMaterial
from .component import TextComponent

_bridge = polyglot.import_value("bridge")
_events._setBridge(_bridge)
_utils._setBridge(_bridge)