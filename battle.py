from utils import timer

@timer
def fight(hero, enemy):
    """Проводить бій. Повертає True, якщо герой переміг."""
    round_no = 1
    while hero.is_alive() and enemy.is_alive():
        if round_no % 3 == 0:
            damage = hero.special(enemy)
        else:
            damage = hero.hit(enemy)
        print(f"  Round {round_no}: {hero.name} -> {enemy.name}: -{damage} ({enemy.hp} HP)")

        if enemy.is_alive():
            damage = enemy.hit(hero)
            print(f"           {enemy.name} -> {hero.name}: -{damage} ({hero.hp} HP)")

        if hero.is_alive() and hero.hp < hero.max_hp * 0.4:
            potion = hero.inventory.use_potion(hero)
            if potion:
                print(f"           {hero.name} drinks «{potion.name}»: HP {hero.hp}")
        round_no += 1
    return hero.is_alive()