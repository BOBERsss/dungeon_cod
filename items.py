class Item:
    def __init__(self, name, power=0, rarity="common"):
        self.name = name
        self.power = power
        self.rarity = rarity

    def __str__(self):
        return f"{self.name} ({self.rarity}, power {self.power})"


class Weapon(Item):
    def equip(self, hero):
        hero.attack += self.power


class Potion(Item):
    def use(self, hero):
        hero.hp += self.power


class Inventory:
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

    def use_potion(self, hero):
        for item in self.items:
            if isinstance(item, Potion):
                self.items.remove(item)
                item.use(hero)
                return item
        return None

    def __len__(self):
        return len(self.items)