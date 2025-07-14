

def create_character():
    print("Choose your character class:")
    print("1. Intercessor")
    print("2. Devastator")
    print("3. Eliminator")
    print("4. Primaris")
    
    class_choice = input("Enter the class of your choice: ")
    name = input("Enter your character's name: ")

    if class_choice == '1':
        return Intercessor(name)
    elif class_choice == '2':
        return Devastator(name)
    elif class_choice == '3':
        return Eliminator(name)
    elif class_choice == '4':
        return Primaris(name)
    else:
        print("Invalid choice, try again.")
     

# Battle function with user menu for actions
def battle(player, wizard):
    while wizard.health > 0 and player.health > 0:
        print("\n--- Your Turn ---")
        print("1. Attack")
        print("2. Use Special Ability")
        print("3. Heal")
        print("4. Attack")
        
        choice = input("Choose an action: ")

        if choice == '1':
            player.attack(wizard)
        elif choice == '2':
            player.special_ability(wizard)   
        elif choice == '3':
            player.heal(player)      
        elif choice == '4':
            player.attack(wizard)
        else:
            print("Invalid choice, try again.")
            continue

        # Evil Wizard's turn to attack and regenerate
        if wizard.health > 0:
            wizard.regenerate()
            wizard.attack(player)
            continue

        if player.health <= 0:
            print(f"{player.name} has been defeated!")
            break

        if wizard.health <= 0:
            print(f"The wizard {wizard.name} has been defeated by {player.name}!")
            break

def main():
    
    player = create_character()

    
    wizard = Lord_Bale("The Chaos Wizard")

    
    battle(player, wizard)

if __name__ == "__main__":
    main()

    from Lord_Bale import Lord_Bale
    from Intercessor import Intercessor
    from Devastator import Devastator
    from Eliminator import Eliminator
    from Primaris import Primaris