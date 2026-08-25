import polyglot
from enum import Enum

_bridge:polyglot.Bridge|None=None

def _setBridge(bridge) -> None:
    _bridge=bridge

def _gBridge() -> polyglot.Bridge: 
    if not _bridge is None :
        return _bridge 
    else:
        raise Exception

class Event(Enum):
    PlayerJoin="org.bukkit.event.player.PlayerJoinEvent"
    PlayerQuit="org.bukkit.event.player.PlayerQuitEvent"
    PlayerChat="io.papermc.paper.event.player.AsyncChatEvent"
    BlockBreak="org.bukkit.event.block.BlockBreakEvent"
    BlockPlace="org.bukkit.event.block.BlockPlaceEvent"
    PlayerInteract="org.bukkit.event.player.PlayerInteractEvent"
    EntityDamage="org.bukkit.event.entity.EntityDamageEvent"

def on_event(event:Event):
    event_class=event.value

    def decorator(fn):
        _gBridge.registerEvent(event_class,fn)

    return decorator