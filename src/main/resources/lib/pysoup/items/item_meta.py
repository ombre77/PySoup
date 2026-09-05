from dataclasses import dataclass,field
from .enchantments import Enchantment
from typing import Optional,Any
from ..text.component import TextComponent,to_java_list

def _empty_enchantments() -> dict[Enchantment, int]:
    return {}

@dataclass
class ItemMeta:
    enchantments: dict[Enchantment, int] = field(default_factory=_empty_enchantments)
    display_name:Optional[TextComponent] = field(default_factory=lambda:TextComponent.EMPTY)
    lore:list[TextComponent]=field(default_factory=list)

    def add_enchant(self,enchant:Enchantment,level:int=1,replace:bool=False,override:bool=True):
        """* enchant: the enchant to add
        * level: the enchantment level
        * replace: wether or not to replace same type echants
        * override: if replace, wether or not to replace the enchant even if the new level is lower"""
        current = self.enchantments.get(enchant)

        if current is None:
            self.enchantments[enchant] = level
            return

        if not replace:
            return

        if override or level > current:
            self.enchantments[enchant] = level

    def remove_enchant(self,enchant:Enchantment,level:int|None=None)->bool:
        current=self.enchantments.get(enchant)
        if current is None: #alr removed
            return False

        if (level is not None and current==level) or (level is None):
            del self.enchantments[enchant]
            return True

        return False

    def set_display_name(self,new_name:TextComponent):
        self.display_name=new_name

    def set_lore(self,lore:list[TextComponent]):
        self.lore=lore

    def set_lore_index(self, text: TextComponent, index: int):
        if index >= len(self.lore):
            self.lore.append(text)
        else:
            self.lore[index] = text

    def apply_to_bukkit(self, bukkit_meta) -> None:
        for enchant, level in self.enchantments.items():
            bukkit_meta.addEnchant(enchant.to_bukkit(), level, True)
        if self.display_name is not None:
            bukkit_meta.displayName(self.display_name.to_adventure())
        if self.lore:
            bukkit_meta.lore(to_java_list(tuple(self.lore)))

    @classmethod
    def from_bukkit(cls, bukkit_meta) -> "ItemMeta":
        enchantments = {}
        if bukkit_meta is not None and bukkit_meta.hasEnchants():
            for e, lvl in bukkit_meta.getEnchants().entrySet():
                enchantments[Enchantment.from_bukkit(e)] = int(lvl)

        display_name = None
        if bukkit_meta is not None and bukkit_meta.hasDisplayName():
            display_name = TextComponent.from_adventure(bukkit_meta.displayName())

        lore=[]
        if bukkit_meta is not None and bukkit_meta.hasLore():
            lore=[TextComponent.from_adventure(java_c) for java_c in bukkit_meta.lore()]
        
        return cls(enchantments,display_name,lore)