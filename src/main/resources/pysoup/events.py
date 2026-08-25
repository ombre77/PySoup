import polyglot
from enum import Enum
from typing import Any, Optional
from dataclasses import dataclass

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
    PlayerChat = "io.papermc.paper.event.player.AsyncChatEvent"
    BlockBreak = "org.bukkit.event.block.BlockBreakEvent"
    BlockPlace = "org.bukkit.event.block.BlockPlaceEvent"
    PlayerInteract = "org.bukkit.event.player.PlayerInteractEvent"
    EntityDamage = "org.bukkit.event.entity.EntityDamageEvent"

def on_event(event: Event):
    event_class = event.value

    def decorator(fn):
        _gBridge().registerEvent(event_class, fn)
        return fn

    return decorator

@dataclass
class EventInfos:
    class PlayerJoin:
        player