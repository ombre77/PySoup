from .materials import ItemMaterial
from .item_stack import ItemStack

def in_group(item:ItemStack,group:set[ItemMaterial])-> bool:
    return item.material in group

LOGS:set[ItemMaterial]={
    ItemMaterial.OAK_LOG,
    ItemMaterial.SPRUCE_LOG,
    ItemMaterial.JUNGLE_LOG,
    ItemMaterial.ACACIA_LOG,
    ItemMaterial.MANGROVE_LOG,
    ItemMaterial.DARK_OAK_LOG,
    ItemMaterial.CHERRY_LOG,
    ItemMaterial.PALE_OAK_LOG
}

STRIPPED_LOGS:set[ItemMaterial]={
    ItemMaterial.STRIPPED_OAK_LOG,
    ItemMaterial.STRIPPED_SPRUCE_LOG,
    ItemMaterial.STRIPPED_JUNGLE_LOG,
    ItemMaterial.STRIPPED_ACACIA_LOG,
    ItemMaterial.STRIPPED_MANGROVE_LOG,
    ItemMaterial.STRIPPED_DARK_OAK_LOG,
    ItemMaterial.STRIPPED_CHERRY_LOG,
    ItemMaterial.STRIPPED_PALE_OAK_LOG
}

OAK_SET:set[ItemMaterial]={
    ItemMaterial.OAK_LOG,
    ItemMaterial.STRIPPED_OAK_LOG,
    ItemMaterial.OAK_WOOD,
    ItemMaterial.STRIPPED_OAK_WOOD,
    ItemMaterial.OAK_PLANKS,
    ItemMaterial.OAK_STAIRS,
    ItemMaterial.OAK_SLAB,
    ItemMaterial.OAK_FENCE,
    ItemMaterial.OAK_FENCE_GATE,
    ItemMaterial.OAK_DOOR,
    ItemMaterial.OAK_TRAPDOOR,
    ItemMaterial.OAK_PRESSURE_PLATE,
    ItemMaterial.OAK_BUTTON,
    ItemMaterial.OAK_SIGN,
    ItemMaterial.OAK_WALL_SIGN,
    ItemMaterial.OAK_HANGING_SIGN,
    ItemMaterial.OAK_WALL_HANGING_SIGN,
    ItemMaterial.OAK_BOAT,
    ItemMaterial.OAK_CHEST_BOAT,
    ItemMaterial.OAK_SHELF,
    ItemMaterial.OAK_LEAVES,
    ItemMaterial.OAK_SAPLING
}

DARK_OAK_SET:set[ItemMaterial]={
    ItemMaterial.DARK_OAK_LOG,
    ItemMaterial.STRIPPED_DARK_OAK_LOG,
    ItemMaterial.DARK_OAK_WOOD,
    ItemMaterial.STRIPPED_DARK_OAK_WOOD,
    ItemMaterial.DARK_OAK_PLANKS,
    ItemMaterial.DARK_OAK_STAIRS,
    ItemMaterial.DARK_OAK_SLAB,
    ItemMaterial.DARK_OAK_FENCE,
    ItemMaterial.DARK_OAK_FENCE_GATE,
    ItemMaterial.DARK_OAK_DOOR,
    ItemMaterial.DARK_OAK_TRAPDOOR,
    ItemMaterial.DARK_OAK_PRESSURE_PLATE,
    ItemMaterial.DARK_OAK_BUTTON,
    ItemMaterial.DARK_OAK_SIGN,
    ItemMaterial.DARK_OAK_WALL_SIGN,
    ItemMaterial.DARK_OAK_HANGING_SIGN,
    ItemMaterial.DARK_OAK_WALL_HANGING_SIGN,
    ItemMaterial.DARK_OAK_BOAT,
    ItemMaterial.DARK_OAK_CHEST_BOAT,
    ItemMaterial.DARK_OAK_SHELF,
    ItemMaterial.DARK_OAK_LEAVES,
    ItemMaterial.DARK_OAK_SAPLING
}

SPRUCE_SET:set[ItemMaterial]={
    ItemMaterial.SPRUCE_LOG,
    ItemMaterial.STRIPPED_SPRUCE_LOG,
    ItemMaterial.SPRUCE_WOOD,
    ItemMaterial.STRIPPED_SPRUCE_WOOD,
    ItemMaterial.SPRUCE_PLANKS,
    ItemMaterial.SPRUCE_STAIRS,
    ItemMaterial.SPRUCE_SLAB,
    ItemMaterial.SPRUCE_FENCE,
    ItemMaterial.SPRUCE_FENCE_GATE,
    ItemMaterial.SPRUCE_DOOR,
    ItemMaterial.SPRUCE_TRAPDOOR,
    ItemMaterial.SPRUCE_PRESSURE_PLATE,
    ItemMaterial.SPRUCE_BUTTON,
    ItemMaterial.SPRUCE_SIGN,
    ItemMaterial.SPRUCE_WALL_SIGN,
    ItemMaterial.SPRUCE_HANGING_SIGN,
    ItemMaterial.SPRUCE_WALL_HANGING_SIGN,
    ItemMaterial.SPRUCE_BOAT,
    ItemMaterial.SPRUCE_CHEST_BOAT,
    ItemMaterial.SPRUCE_SHELF,
    ItemMaterial.SPRUCE_LEAVES,
    ItemMaterial.SPRUCE_SAPLING
}

ACACIA_SET:set[ItemMaterial]={
    ItemMaterial.ACACIA_LOG,
    ItemMaterial.STRIPPED_ACACIA_LOG,
    ItemMaterial.ACACIA_WOOD,
    ItemMaterial.STRIPPED_ACACIA_WOOD,
    ItemMaterial.ACACIA_PLANKS,
    ItemMaterial.ACACIA_STAIRS,
    ItemMaterial.ACACIA_SLAB,
    ItemMaterial.ACACIA_FENCE,
    ItemMaterial.ACACIA_FENCE_GATE,
    ItemMaterial.ACACIA_DOOR,
    ItemMaterial.ACACIA_TRAPDOOR,
    ItemMaterial.ACACIA_PRESSURE_PLATE,
    ItemMaterial.ACACIA_BUTTON,
    ItemMaterial.ACACIA_SIGN,
    ItemMaterial.ACACIA_WALL_SIGN,
    ItemMaterial.ACACIA_HANGING_SIGN,
    ItemMaterial.ACACIA_WALL_HANGING_SIGN,
    ItemMaterial.ACACIA_BOAT,
    ItemMaterial.ACACIA_CHEST_BOAT,
    ItemMaterial.ACACIA_SHELF,
    ItemMaterial.ACACIA_LEAVES,
    ItemMaterial.ACACIA_SAPLING
}

BIRCH_SET:set[ItemMaterial]={
    ItemMaterial.BIRCH_LOG,
    ItemMaterial.STRIPPED_BIRCH_LOG,
    ItemMaterial.BIRCH_WOOD,
    ItemMaterial.STRIPPED_BIRCH_WOOD,
    ItemMaterial.BIRCH_PLANKS,
    ItemMaterial.BIRCH_STAIRS,
    ItemMaterial.BIRCH_SLAB,
    ItemMaterial.BIRCH_FENCE,
    ItemMaterial.BIRCH_FENCE_GATE,
    ItemMaterial.BIRCH_DOOR,
    ItemMaterial.BIRCH_TRAPDOOR,
    ItemMaterial.BIRCH_PRESSURE_PLATE,
    ItemMaterial.BIRCH_BUTTON,
    ItemMaterial.BIRCH_SIGN,
    ItemMaterial.BIRCH_WALL_SIGN,
    ItemMaterial.BIRCH_HANGING_SIGN,
    ItemMaterial.BIRCH_WALL_HANGING_SIGN,
    ItemMaterial.BIRCH_BOAT,
    ItemMaterial.BIRCH_CHEST_BOAT,
    ItemMaterial.BIRCH_SHELF,
    ItemMaterial.BIRCH_LEAVES,
    ItemMaterial.BIRCH_SAPLING
}

JUNGLE_SET:set[ItemMaterial]={
    ItemMaterial.JUNGLE_LOG,
    ItemMaterial.STRIPPED_JUNGLE_LOG,
    ItemMaterial.JUNGLE_WOOD,
    ItemMaterial.STRIPPED_JUNGLE_WOOD,
    ItemMaterial.JUNGLE_PLANKS,
    ItemMaterial.JUNGLE_STAIRS,
    ItemMaterial.JUNGLE_SLAB,
    ItemMaterial.JUNGLE_FENCE,
    ItemMaterial.JUNGLE_FENCE_GATE,
    ItemMaterial.JUNGLE_DOOR,
    ItemMaterial.JUNGLE_TRAPDOOR,
    ItemMaterial.JUNGLE_PRESSURE_PLATE,
    ItemMaterial.JUNGLE_BUTTON,
    ItemMaterial.JUNGLE_SIGN,
    ItemMaterial.JUNGLE_WALL_SIGN,
    ItemMaterial.JUNGLE_HANGING_SIGN,
    ItemMaterial.JUNGLE_WALL_HANGING_SIGN,
    ItemMaterial.JUNGLE_BOAT,
    ItemMaterial.JUNGLE_CHEST_BOAT,
    ItemMaterial.JUNGLE_SHELF,
    ItemMaterial.JUNGLE_LEAVES,
    ItemMaterial.JUNGLE_SAPLING
}

MANGROVE_SET:set[ItemMaterial]={
    ItemMaterial.MANGROVE_LOG,
    ItemMaterial.STRIPPED_MANGROVE_LOG,
    ItemMaterial.MANGROVE_WOOD,
    ItemMaterial.STRIPPED_MANGROVE_WOOD,
    ItemMaterial.MANGROVE_PLANKS,
    ItemMaterial.MANGROVE_STAIRS,
    ItemMaterial.MANGROVE_SLAB,
    ItemMaterial.MANGROVE_FENCE,
    ItemMaterial.MANGROVE_FENCE_GATE,
    ItemMaterial.MANGROVE_DOOR,
    ItemMaterial.MANGROVE_TRAPDOOR,
    ItemMaterial.MANGROVE_PRESSURE_PLATE,
    ItemMaterial.MANGROVE_BUTTON,
    ItemMaterial.MANGROVE_SIGN,
    ItemMaterial.MANGROVE_WALL_SIGN,
    ItemMaterial.MANGROVE_HANGING_SIGN,
    ItemMaterial.MANGROVE_WALL_HANGING_SIGN,
    ItemMaterial.MANGROVE_BOAT,
    ItemMaterial.MANGROVE_CHEST_BOAT,
    ItemMaterial.MANGROVE_SHELF,
    ItemMaterial.MANGROVE_LEAVES,
    ItemMaterial.MANGROVE_PROPAGULE,
    ItemMaterial.MANGROVE_ROOTS,
    ItemMaterial.MUDDY_MANGROVE_ROOTS
}


CHERRY_SET:set[ItemMaterial]={
    ItemMaterial.CHERRY_LOG,
    ItemMaterial.STRIPPED_CHERRY_LOG,
    ItemMaterial.CHERRY_WOOD,
    ItemMaterial.STRIPPED_CHERRY_WOOD,
    ItemMaterial.CHERRY_PLANKS,
    ItemMaterial.CHERRY_STAIRS,
    ItemMaterial.CHERRY_SLAB,
    ItemMaterial.CHERRY_FENCE,
    ItemMaterial.CHERRY_FENCE_GATE,
    ItemMaterial.CHERRY_DOOR,
    ItemMaterial.CHERRY_TRAPDOOR,
    ItemMaterial.CHERRY_PRESSURE_PLATE,
    ItemMaterial.CHERRY_BUTTON,
    ItemMaterial.CHERRY_SIGN,
    ItemMaterial.CHERRY_WALL_SIGN,
    ItemMaterial.CHERRY_HANGING_SIGN,
    ItemMaterial.CHERRY_WALL_HANGING_SIGN,
    ItemMaterial.CHERRY_BOAT,
    ItemMaterial.CHERRY_CHEST_BOAT,
    ItemMaterial.CHERRY_SHELF,
    ItemMaterial.CHERRY_LEAVES,
    ItemMaterial.CHERRY_SAPLING
}

PALE_OAK_SET:set[ItemMaterial]={
    ItemMaterial.PALE_OAK_LOG,
    ItemMaterial.STRIPPED_PALE_OAK_LOG,
    ItemMaterial.PALE_OAK_WOOD,
    ItemMaterial.STRIPPED_PALE_OAK_WOOD,
    ItemMaterial.PALE_OAK_PLANKS,
    ItemMaterial.PALE_OAK_STAIRS,
    ItemMaterial.PALE_OAK_SLAB,
    ItemMaterial.PALE_OAK_FENCE,
    ItemMaterial.PALE_OAK_FENCE_GATE,
    ItemMaterial.PALE_OAK_DOOR,
    ItemMaterial.PALE_OAK_TRAPDOOR,
    ItemMaterial.PALE_OAK_PRESSURE_PLATE,
    ItemMaterial.PALE_OAK_BUTTON,
    ItemMaterial.PALE_OAK_SIGN,
    ItemMaterial.PALE_OAK_WALL_SIGN,
    ItemMaterial.PALE_OAK_HANGING_SIGN,
    ItemMaterial.PALE_OAK_WALL_HANGING_SIGN,
    ItemMaterial.PALE_OAK_BOAT,
    ItemMaterial.PALE_OAK_CHEST_BOAT,
    ItemMaterial.PALE_OAK_SHELF,
    ItemMaterial.PALE_OAK_LEAVES,
    ItemMaterial.PALE_OAK_SAPLING
}


CRIMSON_SET:set[ItemMaterial]={
    ItemMaterial.CRIMSON_STEM,
    ItemMaterial.STRIPPED_CRIMSON_STEM,
    ItemMaterial.CRIMSON_HYPHAE,
    ItemMaterial.STRIPPED_CRIMSON_HYPHAE,
    ItemMaterial.CRIMSON_PLANKS,
    ItemMaterial.CRIMSON_STAIRS,
    ItemMaterial.CRIMSON_SLAB,
    ItemMaterial.CRIMSON_FENCE,
    ItemMaterial.CRIMSON_FENCE_GATE,
    ItemMaterial.CRIMSON_DOOR,
    ItemMaterial.CRIMSON_TRAPDOOR,
    ItemMaterial.CRIMSON_PRESSURE_PLATE,
    ItemMaterial.CRIMSON_BUTTON,
    ItemMaterial.CRIMSON_SIGN,
    ItemMaterial.CRIMSON_WALL_SIGN,
    ItemMaterial.CRIMSON_HANGING_SIGN,
    ItemMaterial.CRIMSON_WALL_HANGING_SIGN,
    ItemMaterial.CRIMSON_SHELF,
}

WARPED_SET:set[ItemMaterial]={
    ItemMaterial.WARPED_STEM,
    ItemMaterial.STRIPPED_WARPED_STEM,
    ItemMaterial.WARPED_HYPHAE,
    ItemMaterial.STRIPPED_WARPED_HYPHAE,
    ItemMaterial.WARPED_PLANKS,
    ItemMaterial.WARPED_STAIRS,
    ItemMaterial.WARPED_SLAB,
    ItemMaterial.WARPED_FENCE,
    ItemMaterial.WARPED_FENCE_GATE,
    ItemMaterial.WARPED_DOOR,
    ItemMaterial.WARPED_TRAPDOOR,
    ItemMaterial.WARPED_PRESSURE_PLATE,
    ItemMaterial.WARPED_BUTTON,
    ItemMaterial.WARPED_SIGN,
    ItemMaterial.WARPED_WALL_SIGN,
    ItemMaterial.WARPED_HANGING_SIGN,
    ItemMaterial.WARPED_WALL_HANGING_SIGN,
    ItemMaterial.WARPED_SHELF,
}

BAMBOO_SET:set[ItemMaterial]={
    ItemMaterial.BAMBOO_BLOCK,
    ItemMaterial.STRIPPED_BAMBOO_BLOCK,
    ItemMaterial.BAMBOO_PLANKS,
    ItemMaterial.BAMBOO_STAIRS,
    ItemMaterial.BAMBOO_MOSAIC,
    ItemMaterial.BAMBOO_MOSAIC_STAIRS,
    ItemMaterial.BAMBOO_MOSAIC_SLAB,
    ItemMaterial.BAMBOO_SLAB,
    ItemMaterial.BAMBOO_FENCE,
    ItemMaterial.BAMBOO_FENCE_GATE,
    ItemMaterial.BAMBOO_DOOR,
    ItemMaterial.BAMBOO_TRAPDOOR,
    ItemMaterial.BAMBOO_PRESSURE_PLATE,
    ItemMaterial.BAMBOO_BUTTON,
    ItemMaterial.BAMBOO_SIGN,
    ItemMaterial.BAMBOO_WALL_SIGN,
    ItemMaterial.BAMBOO_HANGING_SIGN,
    ItemMaterial.BAMBOO_WALL_HANGING_SIGN,
    ItemMaterial.BAMBOO_SHELF,
    ItemMaterial.BAMBOO_RAFT,
    ItemMaterial.BAMBOO_CHEST_RAFT
}

WOOD:set[ItemMaterial]=OAK_SET|ACACIA_SET|BIRCH_SET|JUNGLE_SET|DARK_OAK_SET|CHERRY_SET|SPRUCE_SET|PALE_OAK_SET|MANGROVE_SET

BOATS:set[ItemMaterial]={
    ItemMaterial.OAK_BOAT,
    ItemMaterial.SPRUCE_BOAT,
    ItemMaterial.BIRCH_BOAT,
    ItemMaterial.DARK_OAK_BOAT,
    ItemMaterial.ACACIA_BOAT,
    ItemMaterial.JUNGLE_BOAT,
    ItemMaterial.MANGROVE_BOAT,
    ItemMaterial.CHERRY_BOAT,
    ItemMaterial.BAMBOO_RAFT
}

CHEST_BOATS:set[ItemMaterial]={
    ItemMaterial.OAK_CHEST_BOAT,
    ItemMaterial.SPRUCE_CHEST_BOAT,
    ItemMaterial.BIRCH_CHEST_BOAT,
    ItemMaterial.DARK_OAK_CHEST_BOAT,
    ItemMaterial.ACACIA_CHEST_BOAT,
    ItemMaterial.JUNGLE_CHEST_BOAT,
    ItemMaterial.MANGROVE_CHEST_BOAT,
    ItemMaterial.CHERRY_CHEST_BOAT,
    ItemMaterial.BAMBOO_CHEST_RAFT
}

SIGNS:set[ItemMaterial]={
    ItemMaterial.OAK_SIGN,
    ItemMaterial.SPRUCE_SIGN,
    ItemMaterial.BIRCH_SIGN,
    ItemMaterial.DARK_OAK_SIGN,
    ItemMaterial.ACACIA_SIGN,
    ItemMaterial.JUNGLE_SIGN,
    ItemMaterial.MANGROVE_SIGN,
    ItemMaterial.CHERRY_SIGN,
    ItemMaterial.BAMBOO_SIGN
}

HANGING_SIGNS:set[ItemMaterial]={
    ItemMaterial.OAK_HANGING_SIGN,
    ItemMaterial.SPRUCE_HANGING_SIGN,
    ItemMaterial.BIRCH_HANGING_SIGN,
    ItemMaterial.DARK_OAK_HANGING_SIGN,
    ItemMaterial.ACACIA_HANGING_SIGN,
    ItemMaterial.JUNGLE_HANGING_SIGN,
    ItemMaterial.MANGROVE_HANGING_SIGN,
    ItemMaterial.CHERRY_HANGING_SIGN,
    ItemMaterial.BAMBOO_HANGING_SIGN
}

TOOLS:set[ItemMaterial]={
    #wood
    ItemMaterial.WOODEN_PICKAXE,
    ItemMaterial.WOODEN_AXE,
    ItemMaterial.WOODEN_HOE,
    ItemMaterial.WOODEN_SHOVEL,
    ItemMaterial.WOODEN_SPEAR,
    ItemMaterial.WOODEN_SWORD,
    #stone
    ItemMaterial.STONE_PICKAXE,
    ItemMaterial.STONE_AXE,
    ItemMaterial.STONE_HOE,
    ItemMaterial.STONE_SHOVEL,
    ItemMaterial.STONE_SPEAR,
    ItemMaterial.STONE_SWORD,
    #gold
    ItemMaterial.GOLDEN_PICKAXE,
    ItemMaterial.GOLDEN_AXE,
    ItemMaterial.GOLDEN_HOE,
    ItemMaterial.GOLDEN_SHOVEL,
    ItemMaterial.GOLDEN_SPEAR,
    ItemMaterial.GOLDEN_SWORD,
    #copper
    ItemMaterial.COPPER_PICKAXE,
    ItemMaterial.COPPER_AXE,
    ItemMaterial.COPPER_HOE,
    ItemMaterial.COPPER_SHOVEL,
    ItemMaterial.COPPER_SPEAR,
    ItemMaterial.COPPER_SWORD,
    #iron
    ItemMaterial.IRON_PICKAXE,
    ItemMaterial.IRON_AXE,
    ItemMaterial.IRON_HOE,
    ItemMaterial.IRON_SHOVEL,
    ItemMaterial.IRON_SPEAR,
    ItemMaterial.IRON_SWORD,
    #diamond
    ItemMaterial.DIAMOND_PICKAXE,
    ItemMaterial.DIAMOND_AXE,
    ItemMaterial.DIAMOND_HOE,
    ItemMaterial.DIAMOND_SHOVEL,
    ItemMaterial.DIAMOND_SPEAR,
    ItemMaterial.DIAMOND_SWORD,
    #netherite
    ItemMaterial.NETHERITE_PICKAXE,
    ItemMaterial.NETHERITE_AXE,
    ItemMaterial.NETHERITE_HOE,
    ItemMaterial.NETHERITE_SHOVEL,
    ItemMaterial.NETHERITE_SPEAR,
    ItemMaterial.NETHERITE_SWORD,
}

HELMETS: set[ItemMaterial] = {m for m in ItemMaterial if m.name.endswith("_HELMET")}
CHESTPLATES: set[ItemMaterial] = {m for m in ItemMaterial if m.name.endswith("_CHESTPLATE")}
LEGGINGS: set[ItemMaterial] = {m for m in ItemMaterial if m.name.endswith("_LEGGINGS")}
BOOTS: set[ItemMaterial] = {m for m in ItemMaterial if m.name.endswith("_BOOTS")}

ARMOR: set[ItemMaterial] = HELMETS | CHESTPLATES | LEGGINGS | BOOTS

HELMET_SLOT: set[ItemMaterial] = HELMETS
CHEST_SLOT: set[ItemMaterial] = CHESTPLATES | {ItemMaterial.ELYTRA}
LEGGINGS_SLOT: set[ItemMaterial] = LEGGINGS
BOOTS_SLOT: set[ItemMaterial] = BOOTS

BUCKET: set[ItemMaterial]={
    ItemMaterial.BUCKET,
    ItemMaterial.WATER_BUCKET,
    ItemMaterial.LAVA_BUCKET,
    ItemMaterial.MILK_BUCKET,
    ItemMaterial.POWDER_SNOW_BUCKET,
    ItemMaterial.COD_BUCKET,
    ItemMaterial.SALMON_BUCKET,
    ItemMaterial.AXOLOTL_BUCKET,
    ItemMaterial.TADPOLE_BUCKET,
    ItemMaterial.PUFFERFISH_BUCKET,
    ItemMaterial.TROPICAL_FISH_BUCKET
}

POTIONS:set[ItemMaterial]={
    ItemMaterial.POTION,
    ItemMaterial.SPLASH_POTION,
    ItemMaterial.LINGERING_POTION
}

BOOKS: set[ItemMaterial] = {
    ItemMaterial.WRITTEN_BOOK,
    ItemMaterial.WRITABLE_BOOK,
    ItemMaterial.ENCHANTED_BOOK,
}

BOATS_ALL: set[ItemMaterial] = BOATS | {m for m in ItemMaterial if m.name.endswith("_CHEST_BOAT")}

MINECARTS: set[ItemMaterial] = {
    ItemMaterial.MINECART,
    ItemMaterial.CHEST_MINECART,
    ItemMaterial.FURNACE_MINECART,
    ItemMaterial.HOPPER_MINECART,
    ItemMaterial.TNT_MINECART,
    ItemMaterial.COMMAND_BLOCK_MINECART,
}

FILLED_BUCKETS: set[ItemMaterial] = {
    ItemMaterial.WATER_BUCKET,
    ItemMaterial.LAVA_BUCKET,
    ItemMaterial.MILK_BUCKET,
    ItemMaterial.POWDER_SNOW_BUCKET,
    ItemMaterial.PUFFERFISH_BUCKET,
    ItemMaterial.SALMON_BUCKET,
    ItemMaterial.COD_BUCKET,
    ItemMaterial.TROPICAL_FISH_BUCKET,
    ItemMaterial.AXOLOTL_BUCKET,
    ItemMaterial.TADPOLE_BUCKET,
}

SHULKER_BOXES: set[ItemMaterial] = {m for m in ItemMaterial if m.name.endswith("_SHULKER_BOX")} | {ItemMaterial.SHULKER_BOX}

HORSE_ARMOR: set[ItemMaterial] = {
    ItemMaterial.LEATHER_HORSE_ARMOR,
    ItemMaterial.IRON_HORSE_ARMOR,
    ItemMaterial.GOLDEN_HORSE_ARMOR,
    ItemMaterial.DIAMOND_HORSE_ARMOR,
}

MOB_ARMOR: set[ItemMaterial] = {ItemMaterial.WOLF_ARMOR} | HORSE_ARMOR

MISC_UNSTACKABLE: set[ItemMaterial] = {
    ItemMaterial.CAKE,
    ItemMaterial.TOTEM_OF_UNDYING,
    ItemMaterial.SADDLE,
}

FUEL_MATERIAL:set[ItemMaterial]=BOATS|CHEST_BOATS|WOOD|{
    ItemMaterial.LAVA_BUCKET,
    ItemMaterial.COAL_BLOCK,
    ItemMaterial.DRIED_KELP_BLOCK,
    ItemMaterial.BLAZE_ROD,
    ItemMaterial.COAL,
    ItemMaterial.CHARCOAL,
    ItemMaterial.BEE_NEST,
    ItemMaterial.BEEHIVE,
    ItemMaterial.CHISELED_BOOKSHELF,
    ItemMaterial.LADDER,
    ItemMaterial.CRAFTING_TABLE,
    ItemMaterial.CARTOGRAPHY_TABLE,
    ItemMaterial.FLETCHING_TABLE,
    ItemMaterial.SMITHING_TABLE,
    ItemMaterial.LOOM,
    ItemMaterial.BOOKSHELF,
    ItemMaterial.LECTERN,
    ItemMaterial.COMPOSTER,
    ItemMaterial.CHEST,
    ItemMaterial.TRAPPED_CHEST,
    ItemMaterial.BARREL,
    ItemMaterial.DAYLIGHT_DETECTOR,
    ItemMaterial.JUKEBOX,
    ItemMaterial.NOTE_BLOCK
}