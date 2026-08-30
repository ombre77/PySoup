from enum import Enum
from .......run.plugins.PySoup.scripts.pysoup.bukkit import NamespacedKey,RegistryAccess,RegistryKey
from .......run.plugins.PySoup.scripts.pysoup.utils import component_to_str

ENCHANTMENT_REGISTRY = RegistryAccess.registryAccess().getRegistry(RegistryKey.ENCHANTMENT)

class Enchantment(Enum):
    PROTECTION = "protection"
    FIRE_PROTECTION = "fire_protection"
    FEATHER_FALLING = "feather_falling"
    BLAST_PROTECTION = "blast_protection"
    PROJECTILE_PROTECTION = "projectile_protection"
    RESPIRATION = "respiration"
    AQUA_AFFINITY = "aqua_affinity"
    THORNS = "thorns"
    DEPTH_STRIDER = "depth_strider"
    FROST_WALKER = "frost_walker"
    BINDING_CURSE = "binding_curse"
    SHARPNESS = "sharpness"
    SMITE = "smite"
    BANE_OF_ARTHROPODS = "bane_of_arthropods"
    KNOCKBACK = "knockback"
    FIRE_ASPECT = "fire_aspect"
    LOOTING = "looting"
    SWEEPING_EDGE = "sweeping_edge"
    EFFICIENCY = "efficiency"
    SILK_TOUCH = "silk_touch"
    UNBREAKING = "unbreaking"
    FORTUNE = "fortune"
    POWER = "power"
    PUNCH = "punch"
    FLAME = "flame"
    INFINITY = "infinity"
    LUCK_OF_THE_SEA = "luck_of_the_sea"
    LURE = "lure"
    LOYALTY = "loyalty"
    IMPALING = "impaling"
    RIPTIDE = "riptide"
    CHANNELING = "channeling"
    MULTISHOT = "multishot"
    QUICK_CHARGE = "quick_charge"
    PIERCING = "piercing"
    DENSITY = "density"
    BREACH = "breach"
    WIND_BURST = "wind_burst"
    MENDING = "mending"
    VANISHING_CURSE = "vanishing_curse"
    SOUL_SPEED = "soul_speed"
    SWIFT_SNEAK = "swift_sneak"
    LUNGE = "lunge"

    def to_bukkit(self):
        """Resolves this enum member to the live org.bukkit.enchantments.Enchantment,
        which exposes getMaxLevel(), conflictsWith(), displayName(), etc. directly."""
        key = NamespacedKey.minecraft(self.value)
        enchant = ENCHANTMENT_REGISTRY.get(key)
        if enchant is None:
            raise ValueError(f"Enchantment '{self.value}' not found in registry")
        return enchant

    @classmethod
    def from_bukkit(cls, bukkit_enchantment) -> "Enchantment":
        """Wraps a raw Bukkit Enchantment (e.g. from an ItemMeta) as an Enchantment enum member."""
        return cls(bukkit_enchantment.getKey().getKey())

    def get_max_level(self) -> int:
        return self.to_bukkit().getMaxLevel()

    def get_start_level(self) -> int:
        return self.to_bukkit().getStartLevel()

    def is_treasure(self) -> bool:
        return self.to_bukkit().isTreasure()

    def is_cursed(self) -> bool:
        return self.to_bukkit().isCursed()

    def is_tradeable(self) -> bool:
        return self.to_bukkit().isTradeable()

    def is_discoverable(self) -> bool:
        return self.to_bukkit().isDiscoverable()

    def get_min_modified_cost(self, level: int) -> int:
        return self.to_bukkit().getMinModifiedCost(level)

    def get_max_modified_cost(self, level: int) -> int:
        return self.to_bukkit().getMaxModifiedCost(level)

    def get_anvil_cost(self) -> int:
        return self.to_bukkit().getAnvilCost()

    def get_weight(self) -> int:
        return self.to_bukkit().getWeight()

    def conflicts_with(self, other: "Enchantment") -> bool:
        return self.to_bukkit().conflictsWith(other.to_bukkit())

    def can_enchant_item(self, item) -> bool:
        """item: your own ItemStack wrapper - call .to_bukkit() on it internally."""
        return self.to_bukkit().canEnchantItem(item.to_bukkit())

    def display_name(self, level: int) -> str:
        return component_to_str(self.to_bukkit().displayName(level))

    def description(self) -> str:
        return component_to_str(self.to_bukkit().description())

    def get_active_slot_groups(self):
        """Returns the raw Bukkit Set<EquipmentSlotGroup> - not wrapped, since you don't
        have an EquipmentSlotGroup enum yet."""
        return self.to_bukkit().getActiveSlotGroups()

    def get_exclusive_with(self) -> set["Enchantment"]:
        return {
            Enchantment.from_bukkit(e)
            for e in self.to_bukkit().getExclusiveWith()
        }