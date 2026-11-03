from characters import Character

class Enemy(Character):
    pass

class Boss(Enemy):
    def hit(self, target):
        damage = self.attack
        if self.hp < self.max_hp / 2:
            damage = int(self.attack * 1.5)
            print(f"{self.name} is furious!!!")
        target.take_damage(damage)
        return damage