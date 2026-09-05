from __future__ import annotations
from dataclasses import dataclass, field, replace
from typing import ClassVar, Optional

from ..maths.logic import Trilean
from .text_color import Color
from .text_style import Style, TextDecoration

from ..bukkit import (
    AdventureComponent,
    AdventureTextColor,
    AdventureTextDecoration,
    AdventureKey,
    ArrayList,
    TextComponentImpl,
    PlainTextSerializer
    )

@dataclass(frozen=True)
class Component:
    style: Style = field(default_factory=lambda: Style.EMPTY)
    children: tuple["Component", ...] = ()

    EMPTY: ClassVar["Component"]

    # Style
    def color(self, color: Optional[Color]) -> "Component":
        return replace(self, style=self.style.with_color(color))

    def decorate(self, decoration: TextDecoration, value: bool | Trilean = True) -> "Component":
        return replace(self, style=self.style.decorate(decoration, value))

    def bold(self, value: bool | Trilean = True) -> "Component":
        return self.decorate(TextDecoration.BOLD, value)

    def italic(self, value: bool | Trilean = True) -> "Component":
        return self.decorate(TextDecoration.ITALIC, value)

    def underlined(self, value: bool | Trilean = True) -> "Component":
        return self.decorate(TextDecoration.UNDERLINED, value)

    def strikethrough(self, value: bool | Trilean = True) -> "Component":
        return self.decorate(TextDecoration.STRIKETHROUGH, value)

    def obfuscated(self, value: bool | Trilean = True) -> "Component":
        return self.decorate(TextDecoration.OBFUSCATED, value)

    def font(self, font: Optional[str]) -> "Component":
        return replace(self, style=self.style.with_font(font))

    def with_style(self, style: Style) -> "Component":
        return replace(self, style=style)

    # Tree
    def append(self, *children: "Component") -> "Component":
        return replace(self, children=self.children + children)

    def __add__(self, other: "Component") -> "Component":
        return self.append(other)

    # Style resolution (parent →/← child)
    def _resolved_children(self, parent_style: Style) -> tuple["Component", ...]:
        return tuple(
            replace(child, style=parent_style.merge(child.style))
            for child in self.children
        )

    # Java conversion
    def to_adventure(self, inherited: Style = Style.EMPTY):
        if type(self) is Component:
            return AdventureComponent.empty()
        raise NotImplementedError(f"{type(self).__name__} must implement to_adventure")


Component.EMPTY = Component()


@dataclass(frozen=True)
class TextComponent(Component):
    content: str = ""

    EMPTY:ClassVar["TextComponent"]

    @classmethod
    def of(cls, content: str) -> "TextComponent":
        return cls(content=content)

    def to_adventure(self, inherited: Style = Style.EMPTY):
        effective = inherited.merge(self.style)
        java_component = AdventureComponent.text(self.content)

        if effective.color is not None:
            java_component = java_component.color(AdventureTextColor.color(effective.color.as_int()))

        for deco,state in effective.decorations.items():
            if state is Trilean.UNSET:
                continue
            adventure_deco=getattr(AdventureTextDecoration,deco.value.upper())
            java_component=java_component.decoration(adventure_deco,state._to_adventure_state())

        if effective.font is not None:
            java_component=java_component.font(AdventureKey.key(effective.font))

        if effective.insertion is not None:
            java_component=java_component.insertion(effective.insertion)

        for child in self._resolved_children(effective):
            java_component = java_component.append(child.to_adventure(effective))

        return java_component

    @classmethod
    def from_adventure(cls,java_component)->TextComponent:
        style=Style.from_adventure(java_component.style())

        if isinstance(java_component,TextComponentImpl):
            content=java_component.content()
            children=tuple(TextComponent.from_adventure(c) for c in java_component.children())
            return TextComponent(style,children,content)

        plain=PlainTextSerializer.plainText().serialize(java_component)
        return TextComponent(style,(),plain)

TextComponent.EMPTY=TextComponent()

def to_java_list(components:tuple[Component,...]):
    result=ArrayList()
    for c in components:
        result.add(c.to_adventure)
    return result

def text(content: str) -> TextComponent:
    return TextComponent.of(content)