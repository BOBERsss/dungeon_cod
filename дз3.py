import random

from enemies_дз3 import Enemy_дз3

battle_log = []


class Hero_дз3:
    total_hits = 0

    def __init__(self, name, health, damage):
        self.name = name
        self._health = health
        self.damage = damage

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, value):
        self._health = max(0, value)

    def hit(self, target):
        #
        Hero_дз3.total_hits += 1


        is_crit = random.random() < 0.20
        current_damage = self.damage * 2 if is_crit else self.damage

        target.health -= current_damage


        crit_str = " (КРИТИЧНИЙ УДАР!)" if is_crit else ""
        log_message = f"{self.name} завдає {current_damage} шкоди ворогу {target.name}{crit_str}. У ворога залишилось {target.health} HP."
        battle_log.append(log_message)

        return is_crit



enemy_1 = Enemy_дз3("Гоблін", 60, 10)
print("Перевірка __repr__ для ворога:", repr(enemy_1))

hero_1 = Hero_дз3("Артур", 120, 25)


rounds = 0
crit_count = 0

print("\n--- БІЙ ПОЧАВСЯ ---")
while hero_1.health > 0 and enemy_1.health > 0:
    rounds += 1

    is_critical = hero_1.hit(enemy_1)
    if is_critical:
        crit_count += 1


    if enemy_1.health > 0:
        hero_1.health -= enemy_1.damage
        battle_log.append(
            f"Ворог {enemy_1.name} контратакує і завдає {enemy_1.damage} шкоди герою {hero_1.name}. У героя залишилось {hero_1.health} HP.")

print("--- БІЙ ЗАВЕРШЕНО ---\n")


print("=== ЖУРНАЛ БОЮ ===")
for entry in battle_log:
    print(entry)

print("\n=== СТАТИСТИКА БОЮ ===")
print(f"Кількість раундів: {rounds}")
print(f"Кількість критичних ударів: {crit_count}")
print(f"Загальна кількість ударів героїв (total_hits): {Hero_дз3.total_hits}")

