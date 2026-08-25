import polyglot
import events as _events
import utils as _utils
from events import Event, on_event
from utils import log, get_server
from values import Position,BlockPosition,World,Direction,Location

_bridge = polyglot.import_value("bridge")
_events._setBridge(_bridge)
_utils._setBridge(_bridge)
