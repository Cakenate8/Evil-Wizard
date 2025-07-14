from character import Character

class Devastator(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=35)  # Boost attack power

    # Add your cast spell method here