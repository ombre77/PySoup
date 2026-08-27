from dataclasses import dataclass
from .utils import component_to_str

@dataclass
class TextComponent:
    content:str

    @classmethod
    def from_bukkit(cls,component) -> "TextComponent":
        return TextComponent(component_to_str(component))