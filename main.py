<<<<<<< HEAD
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
=======
from heroes import CLASSES, create_hero, show_hero

print("Ласкаво просимо до Dungeon Code!")
print("Доступні класи:", ", ".join(CLASSES))

name = input("Як звати твого героя? ")
hero_class = input("Обери клас: ")

if hero_class in CLASSES:
    hero = create_hero(name, hero_class)
    show_hero(hero)
else:
    print("Такого класу немає. Спробуй ще раз!")
>>>>>>> a98df0f10a725686a0a0a91f02d96a507ef22ed2
