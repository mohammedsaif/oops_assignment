""" Warrior → Sword Attack

Archer → Arrow Attack

Wizard → Magic Attack

"""
from character import Character

class Warrior(Character):
    def __init__(self, name, health, level,sword):
        super().__init__(name, health, level)
        self.sword = sword;
    def sword_attack(self,target:Character):
        if self.sword > 0:
           self.sword -= 1
           damage = 25 + self.level * 2
           print(f"\n{self.name} attack an sword at {target.name}! (swords left: {self.sword})") 
           target.take_advantage(damage)
        else:
            print(f"\n {self.name} is out of swords!")


    