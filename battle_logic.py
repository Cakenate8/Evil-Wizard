from characters.lord_bale import lord_bale
from characters.intercessor import intercessor
from characters.devastator import devastator
from characters.eliminator import eliminator
from characters.primaris import primaris

def create_character():
    print("Choose your character class:")
    print("1. Intercessor")
    print("2. Devastator")
    print("3. Eliminator")
    print("4. Primaris")
    
    class_choice = input("Enter the class of your choice: ")
    name = input("Enter your character's name: ")

    if class_choice == '1':
        return intercessor(name)
    elif class_choice == '2':
        return devastator(name)
    elif class_choice == '3':
        return eliminator(name)
    elif class_choice == '4':
        return primaris(name)
    else:
        print("Invalid choice, try again.")
     


def battle(player, wizard):
    while wizard.health > 0 and player.health > 0:
        print("\n--- Your Turn ---")
        player.Chose_action()
        
        choice = input("Choose an action: ")

        if choice == '1':
            player.basic_attack(wizard)
        elif choice == '2':
            player.special_attack(wizard)   
        elif choice == '3':
            player.see_apothecary()    
        elif choice == '4':
            player.throw_krak_grenade(wizard)
        else:
            print("Invalid choice, try again.")
            continue

        
        if wizard.health > 0:
            wizard.regenerate()
            wizard.attack(player)
            continue

        if player.health <= 0:
            print(f"{player.name} has been defeated!")
            break

        if wizard.health <= 0:
            print(f"{wizard.name} has been defeated by {player.name}!")
            break

def main():
    
    player = create_character()

    
    wizard = lord_bale("The Chaos Wizard")

    
    battle(player, wizard)

if __name__ == "__main__":
    main()

