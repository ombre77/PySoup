import polyglot

_bridge:polyglot.Bridge|None=None

def _setBridge(bridge) -> None:
    _bridge=bridge

def _gBridge() -> polyglot.Bridge: 
    if not _bridge is None :
        return _bridge 
    else:
        raise Exception


def log(message:str)->None:
    _gBridge.log(str(message))

def get_server():
    return _gBridge.getServer()