from enum import Enum
from typing import Optional
from ..bukkit import DecorationState

class Trilean(Enum):
    """Three states boolean"""
    TRUE=0
    FALSE=1
    UNSET=2

    @classmethod
    def of(cls, value: Optional[bool]) -> "Trilean":
        return cls(value)

    def _to_adventure_state(self):
        if self is Trilean.TRUE:
            return DecorationState.TRUE
        if self is Trilean.FALSE:
            return DecorationState.FALSE
        return DecorationState.NOT_SET

    @classmethod
    def _from_adventure(cls,java_state)->Trilean:
        if java_state == DecorationState.TRUE:
            return cls.TRUE
        if java_state==DecorationState.FALSE:
            return cls.FALSE
        return cls.UNSET