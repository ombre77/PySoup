import polyglot

#Dev Utils
from . import events as _events
from . import utils as _utils
#Event
from .events import Event, on_event,EventInfos,InteractHand,InteractAction
#Utils
from .utils import log, get_server,broadcast
#Math and geometry
from .maths.geometry import Vector3
from .maths.logic import Trilean
from .values import Position,BlockPosition,World,Direction
#Instances
from .instances.instances import WorldInstance, EntityInstance
#Item related
from .items.materials import BlockMaterial,EntityMaterial,ItemMaterial
from .items.max_stack import get_max_stack_size,stackable_to
from .items.item_stack import ItemStack
from .items.item_meta import ItemMeta
from .items.enchantments import Enchantment
#Scheduler
from .schedule.scheduler import task,async_task,run_later,repeating,Task
#Text related
from .text.text_style import Style,TextDecoration
from .text.text_color import Color,NamedColor
from .text.component import Component,TextComponent,text
from .text.text_font import FontKey,VanillaFont
from .text.text_hover import HoverEvent,ShowEntity,ShowItem,ShowText,HoverAction

_bridge = polyglot.import_value("bridge")
_events._setBridge(_bridge)
_utils._setBridge(_bridge)
