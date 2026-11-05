
class Hero:
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage

    def show_info(self):
        print(f"Герой: {self.name} | Здоров'я: {self.health} | Шкода: {self.damage}")

# Імпортуємо ворогів із файлу enemies.py
from дз2_enemies import enemy_1, enemy_2, enemy_3

# Створюємо щонайменше 2 різних екземпляри героя
hero_1 = Hero("Артур", 100, 20)
hero_2 = Hero("Мерлін", 80, 30)

# Виводимо інформацію про всіх створених героїв і ворогів
print("=== ІНФОРМАЦІЯ ПРО ГЕРОЇВ ===")
hero_1.show_info()
hero_2.show_info()

print("\n=== ІНФОРМАЦІЯ ПРО ВОРОГІВ ===")
enemy_1.show_info()
enemy_2.show_info()
enemy_3.show_info()