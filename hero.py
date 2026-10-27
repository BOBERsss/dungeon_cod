import random

CLASSES = {
    "Warrior": {"hp": (110, 140), "attack": (10, 16)},
    "Mag": {"hp": (70, 90), "attack": (16, 24)},
}


# def create_hero(name, hero_class):
#     stats = CLASSES[hero_class]
#     return {
#         "name": name,
#         "class": hero_class,
#         "hp": random.randint(*stats["hp"]),
#         "attack": random.randint(*stats["attack"]),
#     }
#
#
# def show_hero(hero):
#     print(f"  {hero['name']} — {hero['class']}")
#     print(f"  HP:     {hero['hp']}")
#     print(f"  Attack:  {hero['attack']}")
#
class Hero:
    game ="dungeon"
    count = 0
    def __init__(self,name,hero_class,hp,attack):
            Hero.count +=1
            self.name = name
            self.hero_class = hero_class
            self.hp =hp
            self.attack = attack
    def show(self):
         print(f"I am {self.name},{self.hero_class},{self.hp},{self.attack}")


nova = Hero("nova","warrior",00,14)

nova.show()
print(Hero.count)