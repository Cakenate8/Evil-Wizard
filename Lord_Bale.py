from Character import Character
import random


class Lord_Bale(Character):
    def __init__(self, name):
        super().__init__(name, health=200, attack_power=25)
    
    
    def regenerate(self):
        self.health += 10
        print(f"{self.name} regenerates 10 health! Current health: {self.health}")

    def Special_Attack(self,opponent):
        Damage = random.randint(1,{self.attack_power})
        opponent.health -= Damage
        print(f"Lord Bale unleashes a special attack on {opponent.name} for {Damage} damage!")
