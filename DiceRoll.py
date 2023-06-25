import random

def roll_dice():
    print("Welcome to the Dice Roller!")
    while True:
        input("Press enter to roll the dice...")
        dice_value = random.randint(1, 6)
        print(f"You rolled a {dice_value}!")

        play_again = input("Do you want to roll again? (yes/no): ")
        if play_again.lower() != "yes":
            break

    print("Thank you for using the Dice Roller!")

roll_dice()
