from dataclasses import dataclass,field
from .enchantments import Enchantment

def _empty_enchantments() -> dict[Enchantment, int]:
    return {}

@dataclass
class ItemMeta:
    enchantments: dict[Enchantment, int] = field(default_factory=_empty_enchantments)
    # display_name: Optional[Component] = None   <- TODO: later implement the whole Component text system

    def apply_to_bukkit(self, bukkit_meta) -> None:
        for enchant, level in self.enchantments.items():
            bukkit_meta.addEnchant(enchant.to_bukkit(), level, True)

    @classmethod
    def from_bukkit(cls, bukkit_meta) -> "ItemMeta":
        enchantments = {}
        if bukkit_meta is not None and bukkit_meta.hasEnchants():
            for e, lvl in bukkit_meta.getEnchants().entrySet():
                enchantments[Enchantment.from_bukkit(e)] = int(lvl)
        return cls(enchantments)