from lib.pysoup import *

entitys:dict[str,EntityInstance]={}

@on_event(Event.PlayerJoin)
def on_join(event:EventInfos.PlayerJoin):
    player=event.player
    player.send_message("Welcome!")
    broadcast(f"Everyone, welcome {player.get_name()} to the server!")

@on_event(Event.BlockPlace)
def on_place(event:EventInfos.BlockPlace):
    player=event.player
    block=event.block
    player_block_pos=player.get_position()
    new_block_pos=player_block_pos+Position(0,-1,0)
    player.send_message(str(player_block_pos))
    player.send_message(str(player_block_pos.to_block_pos()))
    player.send_message(str(new_block_pos.to_block_pos()))
    player.get_world().get_block(new_block_pos.to_block_pos()).set(BlockMaterial.BEDROCK)

    player.send_message(f"You placed: {block.block.name}")

@on_event(Event.BlockBreak)
def on_break(event:EventInfos.BlockBreak):
    player=event.player
    player.get_inventory().add_item(ItemStack(ItemMaterial.STICK,14))

@on_event(Event.PlayerChat)
def on_char(event:EventInfos.PlayerChat):
    player=event.player
    message=event.message

    player_pos=player.get_position()
    if "tp me" in message:
        player.teleport(player_pos+Position(0,10,0),player.get_direction())
    if "summon" in message:
        entity=player.get_world().summon(player_pos,EntityMaterial("PIG"))
        entitys["pig"]=entity


@on_event(Event.PlayerInteract)
def on_interact(event:EventInfos.PlayerInteract):
    pass
