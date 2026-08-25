import polyglot
from typing import Any, Optional

_bridge: Optional[Any] = None

def _setBridge(bridge) -> None:
    global _bridge
    _bridge = bridge

def _gBridge() -> Any:
    if _bridge is not None:
        return _bridge
    else:
        raise Exception("pysoup bridge not set - _setBridge() was never called")


def log(message: str) -> None:
    _gBridge().log(str(message))

def get_server():
    return _gBridge().getServer()
