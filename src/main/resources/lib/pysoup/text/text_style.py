from __future__ import annotations
from dataclasses import dataclass,field,replace
from enum import Enum
from typing import Optional,Mapping,ClassVar,overload
from ..maths.logic import Trilean
from .text_color import Color,NamedColor
from ..bukkit import (
    TextComponentImpl,
    AdventureTextDecoration
)
from .text_font import FontKey,VanillaFont
from .text_hover import HoverEvent

class TextDecoration(Enum):
    BOLD = "bold"
    ITALIC = "italic"
    UNDERLINED = "underlined"
    STRIKETHROUGH = "strikethrough"
    OBFUSCATED = "obfuscated"

_EMPTY_DECORATIONS:Mapping[TextDecoration,Trilean]={}

@dataclass(frozen=True)
class Style:
    color:Optional["Color"]=None
    decorations:Mapping[TextDecoration,Trilean]=field(default_factory=lambda:_EMPTY_DECORATIONS)
    font: Optional[FontKey] = None
    insertion: Optional[str] = None
    hover_event:Optional[HoverEvent] = None

    def with_color(self, color: Optional["Color"]) -> "Style":
        return replace(self, color=color)

    def decorate(self, decoration: TextDecoration, value: bool | Trilean = True) -> "Style":
        state = value if isinstance(value, Trilean) else Trilean.of(value)
        return replace(self, decorations={**self.decorations, decoration: state})

    def with_font(self, font: Optional[FontKey]) -> "Style":
        return replace(self, font=font)

    def decoration(self, decoration: TextDecoration) -> Trilean:
        return self.decorations.get(decoration, Trilean.UNSET)

    def with_hover_event(self, hover_event: Optional[HoverEvent]) -> "Style":
        return replace(self, hover_event=hover_event)

    def merge(self, other: "Style") -> "Style":
        merged_decorations = dict(self.decorations)
        for deco, state in other.decorations.items():
            if state is not Trilean.UNSET:
                merged_decorations[deco] = state
        return Style(
            color=other.color if other.color is not None else self.color,
            decorations=merged_decorations,
            font=other.font if other.font is not None else self.font,
            insertion=other.insertion if other.insertion is not None else self.insertion,
            hover_event=other.hover_event if other.hover_event is not None else self.hover_event,
        )

    def __add__(self, other:"Style|Color|TextDecoration|FontKey")->"Style":
        match other:
            case Style():
                return self.merge(other)
            case Color():
                return self.with_color(other)
            case FontKey():
                return self.with_font(other)
            case TextDecoration():
                return self.decorate(other,True)
            case _:
                return NotImplemented(f"type of {type(other)} + {type(self)} is not implemented")

    @classmethod
    def from_adventure(cls,java_style)->Style:
        java_color = java_style.color()
        color = Color.from_int(java_color.value()) if java_color is not None else None

        decorations = {}
        for deco in TextDecoration:
            adventure_deco = getattr(AdventureTextDecoration, deco.value.upper())
            decorations[deco] = Trilean._from_adventure(java_style.decoration(adventure_deco))

        java_font = java_style.font()
        font = java_font.asString() if java_font is not None else None

        java_insertion = java_style.insertion()
        insertion = str(java_insertion) if java_insertion is not None else None

        return cls(color=color, decorations=decorations, font=font, insertion=insertion)


    EMPTY: ClassVar["Style"]

Style.EMPTY=Style()
