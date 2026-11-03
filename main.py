from heroes import Warrior, Mag
from enemies import Boss

CLASSES = {"1": Warrior, "2": Mag}

choice = input("Choose your hero: 1 - Warrior, 2 - Mag: ")
name = input("Name of the hero: ")
hero = CLASSES.get(choice, Mag)(name)

boss = Boss("King of Goblins", 120, 15)

round_no = 1

while hero.is_alive() and boss.is_alive():
    print(f"\n---- Round {round_no} ----")

    if round_no % 3 == 0:
        damage = hero.special(boss)
        print(f"{hero.name} special: -{damage} (hp of the enemy = {boss.hp})")
    else:
        damage = hero.hit(boss)
        print(f"{hero.name} hits: -{damage} (hp of the enemy = {boss.hp})")

    if boss.is_alive():
        damage = boss.hit(hero)
        print(f"{boss.name} hits {hero.name}: -{damage} (hp of the hero = {hero.hp})")

    round_no += 1

if hero.is_alive():
    print("Victory!!!")
else:
    print("Game over!!!")