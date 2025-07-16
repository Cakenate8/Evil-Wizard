from characters.character import character
import random

class primaris(character):
    def __init__(self, name):
        super().__init__(name, health=250, attack_power=40)

    def chose_action(self):
        print("Select your Action:")
        print("1. Thunder Hammer")
        print("2. Heavy Bolter")
        print("3. See_Apothecary")
        print("4. Throw Krak Grenade")

    def basic_attack(self, opponent):
        damage = self.attack_power * 3
        opponent.health -= damage
        print(f"{self.name} attacks {opponent.name} with a Thunder Hammer for {damage} damage!")
    
    def special_attack(self, opponent):
        damage = self.attack_power * random.randint(1,3)
        opponent.health -= damage
        print(f"{self.name} attacks {opponent.name} with a Heavy Bolter for {damage} damage!")
    
    def see_apothecary(self):
        self.health = self.max_health
        print(f"{self.name} sees the Apothecary and heals for {self.max_health} health! Current health: {self.health}")
    
    def throw_krak_grenade(self, opponent):
        damage = random.randint(1, self.attack_power * 2)
        opponent.health -= damage
        print(f"{self.name} throws a Krak Grenade at {opponent.name} for {damage} damage!")