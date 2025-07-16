from characters.character import character


class lord_bale(character):
    def __init__(self, name):
        super().__init__(name, health=200, attack_power=25)
    
    
    def regenerate(self):
        self.health += 10
        print(f"{self.name} regenerates 10 health! Current health: {self.health}")
