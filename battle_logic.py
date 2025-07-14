from character import Character


# Function to create player character based on user input
def create_character():
    print("Choose your character class:")
    print("1. Intercessor")
    print("2. Devastator")
    print("3. Eliminator")  # Add Archer
    print("4. Primaris")  # Add Paladin
    
    class_choice = input("Enter the number of your class choice: ")
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
        print("Invalid choice. Defaulting to Warrior.")
        return Interseccor(name)

# Battle function with user menu for actions
def battle(player, wizard):
    while wizard.health > 0 and player.health > 0:
        print("\n--- Your Turn ---")
        print("1. Attack")
        print("2. Use Special Ability")
        print("3. Heal")
        print("4. View Stats")
        
        choice = input("Choose an action: ")

        if choice == '1':
            player.attack(wizard)
        elif choice == '2':
            # Call the special ability here
            pass  # Implement this
        elif choice == '3':
            # Call the heal method here
            pass  # Implement this
        elif choice == '4':
            player.display_stats()
        else:
            print("Invalid choice, try again.")
            continue

        # Evil Wizard's turn to attack and regenerate
        if wizard.health > 0:
            wizard.regenerate()
            wizard.attack(player)

        if player.health <= 0:
            print(f"{player.name} has been defeated!")
            break

    if wizard.health <= 0:
        print(f"The wizard {wizard.name} has been defeated by {player.name}!")

# Main function to handle the flow of the game
def main():
    # Character creation phase
    player = create_character()

    # Evil Wizard is created
    wizard = Lord_Bale("The Chaos Wizard")

    # Start the battle
    battle(player, wizard)

if __name__ == "__main__":
    main()