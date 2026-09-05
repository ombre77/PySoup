from __future__ import annotations
from dataclasses import dataclass,field,replace
from enum import Enum
from typing import Optional,Mapping,ClassVar
from ..maths.logic import Trilean
from .text_color import Color
from ..bukkit import (
    TextComponentImpl,
)

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
    font: Optional[str] = None
    insertion: Optional[str] = None

    def with_color(self, color: Optional["Color"]) -> "Style":
        return replace(self, color=color)

    def decorate(self, decoration: TextDecoration, value: bool | Trilean = True) -> "Style":
        state = value if isinstance(value, Trilean) else Trilean.of(value)
        return replace(self, decorations={**self.decorations, decoration: state})

    def with_font(self, font: Optional[str]) -> "Style":
        return replace(self, font=font)

    def decoration(self, decoration: TextDecoration) -> Trilean:
        return self.decorations.get(decoration, Trilean.UNSET)

    def merge(self, other: "Style") -> "Style":
        """other wins where it's explicitly set; NOT_SET/None falls through to self."""
        merged_decorations = dict(self.decorations)
        for deco, state in other.decorations.items():
            if state is not Trilean.UNSET:
                merged_decorations[deco] = state
        return Style(
            color=other.color if other.color is not None else self.color,
            decorations=merged_decorations,
            font=other.font if other.font is not None else self.font,
            insertion=other.insertion if other.insertion is not None else self.insertion,
        )

    @classmethod
    def from_adventure(cls,java_style)->Style:
        java_color = java_style.color()
        color = Color.from_int(java_color.value()) if java_color is not None else None

        decorations = {}
        for deco in TextDecoration:
            adventure_deco = getattr(TextComponentImpl, deco.value.upper())
            decorations[deco] = Trilean._from_adventure(java_style.decoration(adventure_deco))

        java_font = java_style.font()
        font = java_font.asString() if java_font is not None else None

        java_insertion = java_style.insertion()
        insertion = str(java_insertion) if java_insertion is not None else None

        return cls(color=color, decorations=decorations, font=font, insertion=insertion)


    EMPTY: ClassVar["Style"]

Style.EMPTY=Style()