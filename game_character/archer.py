""" 
Warrior → Sword Attack

Archer → Arrow Attack

Wizard → Magic Attack

"""
from character import Character

class Archer(Character):
    def __init__(self, name, health, level,arrows):
        super().__init__(name, health, level)
        self.arrows = arrows

    def arrow_attack(self,target:Character):
        if self.arrows > 0:
            self.arrows -= 1
            damage = 15 + self.level * 3
            print(f"\n{self.name} fires an arrow at {target.name}! (Arrows left: {self.arrows})")
            target.take_advantage(damage)
        else:
            print(f"\n {self.name} is out of arrows!")

    