""" Warrior → Sword Attack

Archer → Arrow Attack

Wizard → Magic Attack

"""
from character import Character

class Wizard(Character):
    def __init__(self, name, health, level,magic):
        super().__init__(name, health, level)
        self.magic = magic

    def magic_attack(self,target:Character):
         if self.magic > 0:
            self.magic -= 1
            damage = 22 + self.level * 4
            print(f"\n{self.name} wands an magic at {target.name}! (magic left: {self.magic})") 
            target.take_advantage(damage)
         else:
            print(f"\n {self.name} is out of magic!")
        


    