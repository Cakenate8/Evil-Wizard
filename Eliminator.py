from Character import Character
import random

class Eliminator(Character):
    def __init__(self, name):
        super().__init__(name, health=140, attack_power=25)  # Boost health and attack power

    print("Select your Action:")
    print("1. Sniper Rifle")
    print("2. Pistol")
    print("3. See_Apothecary")
    print("4. Throw Krak Grenade")

    def sniper_rifle(self, opponent):
        damage = self.attack_power * 2
        opponent.health -= damage
        print(f"{self.name} attacks {opponent.name} with a Sniper Rifle for {damage} damage!")

    def pistol(self, opponent):
        opponent.health -= 20
        print(f"{self.name} shoots {opponent.name} with a Pistol for 20 damage!")
    
    def See_Apothecary(self):
        self.health = self.max_health
        print(f"{self.name} sees the Apothecary and heals for {self.max_health} health! Current health: {self.health}")
    
    def throw_krak_grenade(self, opponent):
        damage = random.randint(1, self.attack_power * 2)
        opponent.health -= damage
        print(f"{self.name} throws a Krak Grenade at {opponent.name} for {damage} damage!")