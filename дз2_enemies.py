class Enemy:
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage

    def show_info(self):
        print(f"Ворог: {self.name} | Здоров'я: {self.health} | Шкода: {self.damage}")

enemy_1 = Enemy("Гоблін", 50, 10)
enemy_2 = Enemy("Орк", 120, 25)
enemy_3 = Enemy("Скелет", 70, 15)