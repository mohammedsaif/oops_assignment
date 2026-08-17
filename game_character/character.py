"""
Name

Health

Level

"""

class Character:

    def __init__(self,name,health,level):
        self.name = name;
        self.health = health;
        self.level = level;

    def take_advantage(self,damage):
        self.health -= damage;
        if self.health < 0:
           self.health = 0;
        print(f"{self.name} took {damage} damage! Remaining Health: {self.health}")

    def is_alive(self):
        if self.health >0:
            return True;
        else:
            return False;
    


        