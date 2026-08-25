from pysoup import *

@on_event(Event.PlayerJoin)
def player_join():
    log("a player joined")