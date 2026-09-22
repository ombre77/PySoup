from enum import Enum
from ..bukkit import DamageCauseEnum,NamespacedKey,Registry

class DamageCause(Enum):

    BLOCK_EXPLOSION = "BLOCK_EXPLOSION"
    CAMPFIRE = "CAMPFIRE"
    CONTACT = "CONTACT"
    CRAMMING = "CRAMMING"
    CUSTOM = "CUSTOM"
    DRAGON_BREATH = "DRAGON_BREATH"
    DROWNING = "DROWNING"
    DRYOUT = "DRYOUT"
    ENTITY_ATTACK = "ENTITY_ATTACK"
    ENTITY_EXPLOSION = "ENTITY_EXPLOSION"
    ENTITY_SWEEP_ATTACK = "ENTITY_SWEEP_ATTACK"
    FALL = "FALL"
    FALLING_BLOCK = "FALLING_BLOCK"
    FIRE = "FIRE"
    FIRE_TICK = "FIRE_TICK"
    FLY_INTO_WALL = "FLY_INTO_WALL"
    FREEZE = "FREEZE"
    HOT_FLOOR = "HOT_FLOOR"
    KILL = "KILL"
    LAVA = "LAVA"
    LIGHTNING = "LIGHTNING"
    MAGIC = "MAGIC"
    MELTING = "MELTING"
    POISON = "POISON"
    PROJECTILE = "PROJECTILE"
    SONIC_BOOM = "SONIC_BOOM"
    STARVATION = "STARVATION"
    SUFFOCATION = "SUFFOCATION"
    SUICIDE = "SUICIDE"
    THORNS = "THORNS"
    VOID = "VOID"
    WITHER = "WITHER"
    WORLD_BORDER = "WORLD_BORDER"

    def to_bukkit(self):
        return getattr(DamageCauseEnum, self.value)

    @classmethod
    def from_bukkit(cls, cause) -> "DamageCause":
        return cls(cause.name())


class DamageType(Enum):

    ARROW = "arrow"
    BAD_RESPAWN_POINT = "bad_respawn_point"
    CACTUS = "cactus"
    CAMPFIRE = "campfire"
    CRAMMING = "cramming"
    DRAGON_BREATH = "dragon_breath"
    DROWN = "drown"
    DRY_OUT = "dry_out"
    ENDER_PEARL = "ender_pearl"
    EXPLOSION = "explosion"
    FALL = "fall"
    FALLING_ANVIL = "falling_anvil"
    FALLING_BLOCK = "falling_block"
    FALLING_STALACTITE = "falling_stalactite"
    FIREBALL = "fireball"
    FIREWORKS = "fireworks"
    FLY_INTO_WALL = "fly_into_wall"
    FREEZE = "freeze"
    GENERIC = "generic"
    GENERIC_KILL = "generic_kill"
    HOT_FLOOR = "hot_floor"
    IN_FIRE = "in_fire"
    IN_WALL = "in_wall"
    INDIRECT_MAGIC = "indirect_magic"
    LAVA = "lava"
    LIGHTNING_BOLT = "lightning_bolt"
    MACE_SMASH = "mace_smash"
    MAGIC = "magic"
    MOB_ATTACK = "mob_attack"
    MOB_ATTACK_NO_AGGRO = "mob_attack_no_aggro"
    MOB_PROJECTILE = "mob_projectile"
    ON_FIRE = "on_fire"
    OUT_OF_WORLD = "out_of_world"
    OUTSIDE_BORDER = "outside_border"
    PLAYER_ATTACK = "player_attack"
    PLAYER_EXPLOSION = "player_explosion"
    SONIC_BOOM = "sonic_boom"
    SPIT = "spit"
    STALAGMITE = "stalagmite"
    STARVE = "starve"
    STING = "sting"
    SWEET_BERRY_BUSH = "sweet_berry_bush"
    THORNS = "thorns"
    THROWN = "thrown"
    TRIDENT = "trident"
    UNATTRIBUTED_FIREBALL = "unattributed_fireball"
    WIND_CHARGE = "wind_charge"
    WITHER = "wither"
    WITHER_SKULL = "wither_skull"

    def to_bukkit(self):
        key = NamespacedKey.minecraft(self.value)
        bukkit_type = Registry.DAMAGE_TYPE.get(key)
        if bukkit_type is None:
            raise ValueError(f"DamageType '{self.value}' not found in registry")
        return bukkit_type

    @classmethod
    def from_bukkit(cls, damage_type) -> "DamageType":
        return cls(damage_type.getKey().getKey())