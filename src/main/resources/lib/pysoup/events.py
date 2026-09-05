import polyglot
from enum import Enum
from typing import Any, Optional,Callable
from dataclasses import dataclass,field
from .instances.instances import PlayerInstance,BlockInstance,EntityInstance
from .utils import component_to_str
from .text.component import TextComponent

_bridge: Optional[Any] = None

def _setBridge(bridge) -> None:
    global _bridge
    _bridge = bridge

def _gBridge() -> Any:
    if _bridge is not None:
        return _bridge
    else:
        raise Exception("pysoup bridge not set -> _setBridge() was never called")


class Event(Enum):
    PlayerJoin = "org.bukkit.event.player.PlayerJoinEvent"
    PlayerQuit = "org.bukkit.event.player.PlayerQuitEvent"
    PlayerChat = "io.papermc.paper.event.player.AsyncChatEvent"
    BlockBreak = "org.bukkit.event.block.BlockBreakEvent"
    BlockPlace = "org.bukkit.event.block.BlockPlaceEvent"
    PlayerInteract = "org.bukkit.event.player.PlayerInteractEvent"
    EntityDamage = "org.bukkit.event.entity.EntityDamageEvent"

def on_event(event: Event):
    event_class = event.value
    extractor = _EVENT_EXTRACTORS.get(event)

    def decorator(fn:Callable):
        if extractor is not None:
            confirmed_extractor = extractor

            def handler(raw_event):
                fn(confirmed_extractor(raw_event))
        else:
            handler = fn  # fallback if no infos, return raw bukkit event

        _gBridge().registerEvent(event_class, handler)
        return fn

    return decorator

#some different event for PlayerInteract
class InteractAction(Enum):
    LEFT_CLICK_AIR = "LEFT_CLICK_AIR"
    LEFT_CLICK_BLOCK = "LEFT_CLICK_BLOCK"
    RIGHT_CLICK_AIR = "RIGHT_CLICK_AIR"
    RIGHT_CLICK_BLOCK = "RIGHT_CLICK_BLOCK"
    PHYSICAL = "PHYSICAL"

    @classmethod
    def from_bukkit(cls, bukkit_action) -> "InteractAction":
        return cls(bukkit_action.name())

class InteractHand(Enum):
    MAIN_HAND = "MAIN_HAND"
    OFF_HAND = "OFF_HAND"

    @classmethod
    def from_bukkit(cls, bukkit_equipment_slot) -> Optional["InteractHand"]:
        """Bukkit's PlayerInteractEvent.getHand() returns an EquipmentSlot
        (HAND or OFF_HAND) - or null for actions where a hand doesn't apply
        (e.g. PHYSICAL, like stepping on a pressure plate)."""
        if bukkit_equipment_slot is None:
            return None
        name = bukkit_equipment_slot.name()
        return cls.MAIN_HAND if name == "HAND" else cls(name)



class EventInfos:
    #some utils first
    @dataclass
    class CancellableEvent:
        """Base for events that can be cancelled
        Not meant to be directly used"""

        _raw_event:Any=field(repr=False,compare=False) #avoid compare issue

        def cancel(self)->None:
            self._raw_event.setCancelled(True)

        def is_cancelled(self)->bool:
            return self._raw_event.isCancelled()

        def set_cancelled(self,cancelled:bool)->None:
            self._raw_event.setCancelled(cancelled)

    #event infos

    @dataclass
    class PlayerJoin:
        player:PlayerInstance

    @dataclass
    class PlayerQuit:
        player:PlayerInstance

    @dataclass
    class PlayerChat(CancellableEvent):
        player:PlayerInstance
        message:TextComponent

    @dataclass
    class BlockBreak(CancellableEvent):
        player:PlayerInstance
        block:BlockInstance

    @dataclass
    class BlockPlace(CancellableEvent):
        player:PlayerInstance
        block:BlockInstance

    @dataclass
    class PlayerInteract(CancellableEvent):
        player:PlayerInstance
        block:Optional[BlockInstance]
        action:InteractAction
        hand:Optional[InteractHand]

        def is_left_click(self) -> bool:
            return self.action in (InteractAction.LEFT_CLICK_AIR, InteractAction.LEFT_CLICK_BLOCK)

        def is_right_click(self) -> bool:
            return self.action in (InteractAction.RIGHT_CLICK_AIR, InteractAction.RIGHT_CLICK_BLOCK)

        def is_block_interact(self) -> bool:
            return self.action in (InteractAction.LEFT_CLICK_BLOCK, InteractAction.RIGHT_CLICK_BLOCK)

        def is_air_interact(self) -> bool:
            return self.action in (InteractAction.LEFT_CLICK_AIR, InteractAction.RIGHT_CLICK_AIR)

        def is_physical(self) -> bool:
            return self.action == InteractAction.PHYSICAL

    @dataclass
    class EntityDamage(CancellableEvent):
        entity: EntityInstance
        damage: float
        cause: str



_EVENT_EXTRACTORS: dict[Event, Callable[[Any], Any]] = {
    Event.PlayerJoin: lambda e: EventInfos.PlayerJoin(
        player=PlayerInstance.from_bukkit(e.getPlayer())
    ),
    Event.PlayerQuit: lambda e: EventInfos.PlayerQuit(
        player=PlayerInstance.from_bukkit(e.getPlayer())
    ),
    Event.PlayerChat: lambda e: EventInfos.PlayerChat(
        _raw_event=e,
        player=PlayerInstance.from_bukkit(e.getPlayer()),
        message=TextComponent.from_adventure(e.message())
    ),
    Event.BlockBreak: lambda e: EventInfos.BlockBreak(
        _raw_event=e,
        player=PlayerInstance.from_bukkit(e.getPlayer()),
        block=BlockInstance.from_bukkit(e.getBlock())
    ),
    Event.BlockPlace: lambda e: EventInfos.BlockPlace(
        _raw_event=e,
        player=PlayerInstance.from_bukkit(e.getPlayer()),
        block=BlockInstance.from_bukkit(e.getBlock())
    ),
    Event.PlayerInteract: lambda e: EventInfos.PlayerInteract(
        _raw_event=e,
        player=PlayerInstance.from_bukkit(e.getPlayer()),
        block=BlockInstance.from_bukkit(e.getClickedBlock()) if e.getClickedBlock() is not None else None,
        action=InteractAction.from_bukkit(e.getAction()),
        hand=InteractHand.from_bukkit(e.getHand())
    ),
    Event.EntityDamage: lambda e: EventInfos.EntityDamage(
        _raw_event=e,
        entity=EntityInstance.from_bukkit(e.getEntity()),
        damage=e.getDamage(),
        cause=e.getCause().name()
    )
}