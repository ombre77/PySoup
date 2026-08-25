import polyglot
import events as _events
from events import Event

_bridge:polyglot.Bridge=polyglot.import_value("bridge")
_events._setBridge(_bridge)

