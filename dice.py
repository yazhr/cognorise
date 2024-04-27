import random

def roll_dice(sides):
    return random.randint(1, sides)

def main():
    print("Welcome to the Dice Rolling Simulator!")

    while True:
        try:
            sides = int(input("Enter the number of sides on the dice: "))
            if sides <= 0:
                raise ValueError
            break
        except ValueError:
            print("Invalid input. Please enter a positive integer.")

    while True:
        try:
            num_rolls = int(input("Enter the number of rolls: "))
            if num_rolls <= 0:
                raise ValueError
            break
        except ValueError:
            print("Invalid input. Please enter a positive integer.")

    print(f"\nRolling a {sides}-sided dice {num_rolls} times...\n")

    for roll in range(1, num_rolls + 1):
        result = roll_dice(sides)
        print(f"Roll {roll}: {result}")

    print("\nThanks for using the Dice Rolling Simulator!")

if _name_ == "_main_":
    main()
