import time
import random

# Utility function for adding pauses between texts
def pause(text, delay=2):
    print(text)
    time.sleep(delay)

# Start the game and create the player character
def start_game():
    pause("Welcome, brave soul! You've been mysteriously transmigrated into an ancient world of martial arts and mystical cultivation.")
    pause("The air is filled with the scent of blooming lotus, and you feel a powerful energy coursing through your veins...", 2)

    # Gender selection
    while True:
        gender = input("Choose your gender (Male/Female): ").strip().lower()
        if gender in ['male', 'female']:
            break
        print("Invalid choice. Please enter 'Male' or 'Female'.")

    # Name entry
    name = input("Enter your new name in this world: ").strip()
    pause(f"\nWelcome, {name} the {gender.capitalize()} Cultivator!")
    pause("Your journey begins in a small village surrounded by misty mountains and hidden secrets...", 2)

    # Initialize player stats
    player = {
        "name": name,
        "gender": gender.capitalize(),
        "hp": 100,
        "attack": 15,
        "defense": 10,
        "skill_damage": 25,
    }

    training_phase(player)

# Training phase to boost stats
def training_phase(player):
    pause("Before embarking on your journey, you must undergo training to hone your skills.")
    pause("You spend days learning combat techniques, meditating, and sparring with other beginners.")

    for i in range(3):
        pause(f"Training session {i + 1}: Choose an activity:")
        print("1. Practice combat to improve attack.")
        print("2. Defensive drills to strengthen defense.")
        print("3. Energy cultivation to boost HP.")

        choice = input("What will you train? (1-3): ").strip()

        if choice == '1':
            player["attack"] += random.randint(2, 4)
            pause("Your attacks become sharper and more powerful!")
        elif choice == '2':
            player["defense"] += random.randint(2, 4)
            pause("Your defenses become sturdier, able to withstand greater attacks!")
        elif choice == '3':
            player["hp"] += random.randint(10, 20)
            pause("You feel your vitality surge as your energy cultivation improves!")
        else:
            pause("Invalid choice. You meditate quietly, gaining clarity but no stat improvements.")

    pause(f"Training complete! Your stats are now: HP: {player['hp']}, Attack: {player['attack']}, Defense: {player['defense']}.", 2)
    first_choice(player)

# First choice: path selection
def first_choice(player):
    pause("You see two paths ahead, both shrouded in mystery:")
    print("1. A winding path leading into the dense, dark forest.")
    print("2. A steep mountain trail with the sound of ancient bells echoing from above.")

    while True:
        choice = input("Which path will you take? (1 or 2): ").strip()

        if choice == '1':
            forest_path(player)
            break
        elif choice == '2':
            mountain_path(player)
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")

# Forest path scenario
def forest_path(player):
    pause("\nYou venture into the forest, surrounded by towering trees and the distant call of mysterious creatures.")

    pause("A ferocious beast suddenly blocks your path! Its eyes glow with a menacing red light.")
    battle(player, "Beast", 80, 10)

    pause("After defeating the beast, you find an ancient artifact hidden in the roots of a giant tree.")
    pause("The artifact grants you increased skill damage.")
    player["skill_damage"] += 10

    pause("As you move deeper into the forest, you encounter a wise hermit who tests your resolve in battle.")
    battle(player, "Forest Hermit", 100, 12)

    end_game(player["name"], "With the forest's secrets uncovered, you emerge stronger and wiser.")

# Mountain path scenario
def mountain_path(player):
    pause("\nYou climb the rugged mountain trail, feeling a strange pull towards an ancient temple hidden above.")

    pause("As you approach the temple, a rogue cultivator challenges you, seeking to test your strength.")
    battle(player, "Rogue Cultivator", 90, 12)

    pause("Inside the temple, you discover a scroll containing forgotten martial arts techniques.")
    pause("The scroll increases your attack power.")
    player["attack"] += 10

    pause("A storm brews around the temple, and a powerful guardian steps forward to challenge you.")
    battle(player, "Temple Guardian", 120, 15)

    end_game(player["name"], "Having conquered the mountain, you return as a legendary cultivator.")

# Battle system
def battle(player, opponent_name, opponent_hp, opponent_attack):
    pause(f"\nBattle begins! You are facing a {opponent_name}.")

    opponent = {"name": opponent_name, "hp": opponent_hp, "attack": opponent_attack}

    while player["hp"] > 0 and opponent["hp"] > 0:
        print(f"\nYour HP: {player['hp']} | {opponent['name']} HP: {opponent['hp']}")
        print("1. Attack")
        print("2. Defend")
        print("3. Use Skill")

        choice = input("What will you do? (1, 2, or 3): ").strip()

        if choice == '1':
            damage = max(player["attack"] - random.randint(0, 5), 5)
            opponent["hp"] -= damage
            pause(f"You attack the {opponent['name']} and deal {damage} damage!")
        elif choice == '2':
            reduced_damage = max(opponent["attack"] - player["defense"] - random.randint(5, 10), 0)
            player["hp"] -= reduced_damage
            pause(f"You defend against the attack, reducing the damage to {reduced_damage}!")
        elif choice == '3':
            skill_damage = max(player["skill_damage"] - random.randint(0, 5), 15)
            opponent["hp"] -= skill_damage
            pause(f"You unleash a powerful skill, dealing {skill_damage} damage!")
        else:
            print("Invalid choice. Please choose 1, 2, or 3.")
            continue

        if opponent["hp"] > 0:
            damage = max(opponent["attack"] - random.randint(0, 5), 5)
            player["hp"] -= damage
            pause(f"The {opponent['name']} strikes back, dealing {damage} damage!")

    if player["hp"] > 0:
        pause(f"\nYou have defeated the {opponent['name']}! Victory is yours!")
    else:
        pause(f"\nYou have been defeated by the {opponent['name']}.")
        end_game(player["name"], "Your journey ends here...")

# End game function
def end_game(name, message):
    pause("\n" + message)
    pause(f"Thank you for playing, {name}! The adventure ends here.")

# Main game loop
def main():
    while True:
        try:
            start_game()
            
            # Ask if the player wants to play again or exit
            while True:
                restart = input("Would you like to start a new game? (yes or no): ").strip().lower()
                if restart == 'yes':
                    print("\nStarting a new adventure...\n")
                    break  # Break inner loop to start a new game
                elif restart == 'no':
                    print("Exiting the game. See you next time!")
                    return  # Exit the function and program
                else:
                    print("Invalid input. Please enter 'yes' or 'no'.")
        
        except KeyboardInterrupt:
            print("\nGame interrupted. Goodbye!")
            break
        finally:
            print("Thank you for trying out this text-based adventure game! I hope you enjoyed your journey.\n")

# Run the main game loop
main()