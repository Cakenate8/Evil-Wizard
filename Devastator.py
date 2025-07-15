from Character import Character
import random

class Devastator(Character):
    def __init__(self, name):
        super().__init__(name, health=175, attack_power=50)

    def Chose_action(self):
        print("Select your Action:")
        print("1. Storm Bolter")
        print("2. Multi-melta")
        print("3. See_Apothecary")
        print("4.Throw Krak Grenade")

    def basic_attack(self, opponent):
        damage = self.attack_power * 2
        opponent.health -= damage
        print(f"{self.name} attacks {opponent.name} with a Storm Bolter for {damage} damage!")

    def special_attack(self, opponent):
        damage = self.attack_power * 3
        opponent.health -= damage
        print(f"{self.name} attacks {opponent.name} with a Multi-melta for {damage} damage!")  

    def see_apothecary(self):
        self.health = self.max_health
        print(f"{self.name} sees the Apothecary and heals for {self.max_health} health! Current health: {self.health}")

    def throw_krak_grenade(self, opponent):
        damage = random.randint(1, self.attack_power * 2)
        opponent.health -= damage
        print(f"{self.name} throws a Krak Grenade at {opponent.name} for {damage} damage!")