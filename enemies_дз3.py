import random

class Enemy_дз3:
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage

    def show_info(self):
        print(f"Ворог: {self.name} | Здоров'я: {self.health} | Шкода: {self.damage}")

    def __repr__(self):
        return f"Enemy(name='{self.name}', health={self.health}, damage={self.damage})"