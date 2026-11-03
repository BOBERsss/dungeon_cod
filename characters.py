class Character:
    def __init__(self, name, max_hp, attack):
        self.name = name
        self.max_hp = max_hp
        self._hp = max_hp
        self.attack = attack
    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, value):
        self._hp = max(0, min(value, self.max_hp))

    def is_alive(self):
        return self._hp > 0

    def take_damage(self, amount):
        self.hp -= amount

    def hit(self, target):
        target.take_damage(self.attack)
        return self.attack

    def __str__(self):
        return f"{self.name} HP {self.hp} / {self.max_hp} ATK {self.attack}"