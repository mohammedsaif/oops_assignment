from archer import Archer
from warrior import Warrior
from wizard import Wizard

if __name__ == "__main__":
    thorin = Warrior(name="Thorin", health=100, level=5, sword=25)
    legolas = Archer(name="Legolas", health=80, level=6, arrows=30)
    gandalf = Wizard(name="Gandalf", health=70, level=8, magic=50)

    # Show initial states
    print("--- Initial Game Setup ---")
    print(f"{thorin.name} HP: {thorin.health} | {legolas.name} HP: {legolas.health} | {gandalf.name} HP: {gandalf.health}")

    # Battle Interaction
    thorin.sword_attack(legolas)
    legolas.arrow_attack(gandalf)
    gandalf.magic_attack(thorin)



