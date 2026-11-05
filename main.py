from battle import fight
from heroes import Mag
from loot import enemy_generator, loot_generator
from items import Potion
from utils import BATTLE_LOG

hero = Mag("Nova")
hero.inventory.add(Potion("Small Potion", 30))
print(hero)

enemies = enemy_generator()
loot = loot_generator()
defeated = 0

for room in range(1, 4):
    enemy = next(enemies)
    print(f"\n=== Room {room}: {enemy} ===")
    if not fight(hero, enemy):
        print("The hero has died...")
        break
    defeated += 1
    drop = next(loot)
    hero.inventory.add(drop)
    print(f"Loot: {drop}")

print(f"\nEnemies defeated: {defeated}")
best = sorted(hero.inventory.items, key=lambda item: item.power, reverse=True)[:3]
print("Strongest items:", [item.name for item in best])
print("Attacks in the log:", len(BATTLE_LOG))
print("Last entry:", BATTLE_LOG[-1])