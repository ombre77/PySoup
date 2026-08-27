from lib.pysoup import *

@on_event(Event.PlayerJoin)
def player_join(event:EventInfos.PlayerJoin):
    log(f"a player joined:{event.player.get_name()}")

    pos=event.player.get_position().to_block_pos()
    pos.y-=1

    World.Overworld.set_block(pos,BlockMaterial("stone"))
    log(f"block placed at position: {pos.x} {pos.y} {pos.z}")

@on_event(Event.PlayerChat)
def player_chat(event:EventInfos.PlayerChat):
    event.player.send_message(f"you chatted: '{event.message}'")