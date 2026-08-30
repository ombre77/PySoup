import polyglot
from . import events as _events
from . import utils as _utils
from .events import Event, on_event,EventInfos,InteractHand,InteractAction
from .utils import log, get_server,broadcast
from .values import Position,BlockPosition,World,Direction
from .instances.instances import WorldInstance, EntityInstance
from .items.materials import BlockMaterial,EntityMaterial,ItemMaterial
from .component import TextComponent
from .items.max_stack import get_max_stack_size,stackable_to
from .items.item_stack import ItemStack
from .items.item_meta import ItemMeta
from .items.enchantments import Enchantment
from .schedule.scheduler import task,async_task,run_later,repeating,Task

_bridge = polyglot.import_value("bridge")
_events._setBridge(_bridge)
_utils._setBridge(_bridge)
