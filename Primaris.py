from Character import Character
import random

class Primaris(Character):
    def __init__(self, name):
        super().__init__(name, health=250, attack_power=40)

    def Chose_action(self):
        print("Select your Action:")
        print("1. Thunder Hammer")
        print("2. Heavy Bolter")
        print("3. See_Apothecary")
        print("4. Pistol")

    def thunder_hammer(self, opponent):
        damage = self.attack_power * 3
        opponent.health -= damage
        print(f"{self.name} attacks {opponent.name} with a Thunder Hammer for {damage} damage!")
    
    def heavy_bolter(self, opponent):
        damage = self.attack_power * random.randint(1,3)
        opponent.health -= damage
        print(f"{self.name} attacks {opponent.name} with a Heavy Bolter for {damage} damage!")
    
    def see_apothecary(self):
        self.health = self.max_health
        print(f"{self.name} sees the Apothecary and heals for {self.max_health} health! Current health: {self.health}")
    
    def pistol(self, opponent):
        opponent.health -= 20
        print(f"{self.name} shoots {opponent.name} with a Pistol for 20 damage!")