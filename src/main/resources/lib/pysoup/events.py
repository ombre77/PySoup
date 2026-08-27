import polyglot
from enum import Enum
from typing import Any, Optional,Callable
from dataclasses import dataclass
from .instances import PlayerInstance,BlockInstance
from .utils import component_to_str

_bridge: Optional[Any] = None

def _setBridge(bridge) -> None:
    global _bridge
    _bridge = bridge

def _gBridge() -> Any:
    if _bridge is not None:
        return _bridge
    else:
        raise Exception("pysoup bridge not set - _setBridge() was never called")


class Event(Enum):
    PlayerJoin = "org.bukkit.event.player.PlayerJoinEvent"
    PlayerQuit = "org.bukkit.event.player.PlayerQuitEvent"
    PlayerChat = "io.papermc.paper.event.player.ChatEvent" #TODO: eventually switch back to AsyncChatEvent and make the listener create a bukkit scheduler
    BlockBreak = "org.bukkit.event.block.BlockBreakEvent"
    BlockPlace = "org.bukkit.event.block.BlockPlaceEvent"
    PlayerInteract = "org.bukkit.event.player.PlayerInteractEvent"
    EntityDamage = "org.bukkit.event.entity.EntityDamageEvent"

def on_event(event: Event):
    event_class = event.value
    extractor = _EVENT_EXTRACTORS.get(event)

    def decorator(fn):
        if extractor is not None:
            confirmed_extractor = extractor

            def handler(raw_event):
                fn(confirmed_extractor(raw_event))
        else:
            handler = fn  # fallback if no infos, return raw bukkit event

        _gBridge().registerEvent(event_class, handler)
        return fn

    return decorator

class EventInfos:

    @dataclass
    class PlayerJoin:
        player:PlayerInstance

    @dataclass
    class PlayerQuit:
        player:PlayerInstance

    @dataclass
    class PlayerChat:
        player:PlayerInstance
        message:str

    @dataclass
    class BlockBreak:
        player:PlayerInstance
        block:BlockInstance

    @dataclass
    class BlockPlace:
        player:PlayerInstance
        block:BlockInstance


_EVENT_EXTRACTORS: dict[Event, Callable[[Any], Any]] = {
    Event.PlayerJoin: lambda e: EventInfos.PlayerJoin(
        player=PlayerInstance.from_bukkit(e.getPlayer())
    ),
    Event.PlayerQuit: lambda e: EventInfos.PlayerQuit(
        player=PlayerInstance.from_bukkit(e.getPlayer())
    ),
    Event.PlayerChat: lambda e: EventInfos.PlayerChat(
        player=PlayerInstance.from_bukkit(e.getPlayer()),
        message=component_to_str(e.message())
    ),
    Event.BlockBreak: lambda e: EventInfos.BlockBreak(
        player=PlayerInstance.from_bukkit(e.getPlayer()),
        block=BlockInstance.from_bukkit(e.getBlock())
    ),
    Event.BlockPlace: lambda e: EventInfos.BlockPlace(
        player=PlayerInstance.from_bukkit(e.getPlayer()),
        block=BlockInstance.from_bukkit(e.getBlock())
    )
}