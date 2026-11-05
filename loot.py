import random

from enemies import Enemy
from items import Weapon, Potion

LOOT_TABLE = [
    ("Rusty Sword", Weapon, 3, "common"),
    ("Steel Sword", Weapon, 8, "rare"),
    ("Dragon Sword", Weapon, 15, "epic"),
    ("Small Potion", Potion, 20, "common"),
    ("Large Potion", Potion, 60, "epic"),
]

ENEMY_NAMES = ["Goblin", "Skeleton", "Orc", "Spider", "Ghost"]


def loot_generator():
    """Нескінченний потік випадкового луту."""
    while True:
        name, kind, power, rarity = random.choice(LOOT_TABLE)
        yield kind(name, power, rarity)


def enemy_generator():
    """Нескінченний потік ворогів: кожен наступний сильніший."""
    level = 1
    while True:
        name = random.choice(ENEMY_NAMES)
        yield Enemy(f"{name} (level {level})", 40 + level * 10, 6 + level * 2)
        level += 1