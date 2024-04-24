import random

# function to get random numbers when dice is rolled
def roll_dice(num_dice, num_sides):
    results = [random.randint(1, num_sides) for _ in range(num_dice)]
    return results  

if __name__ == "__main__":
    print("Welcome to the Dice Roller App.")

    while True:
        num_dice = int(input("Enter the number of dice to roll: "))
        num_sides = int(input("Enter the number of sides for each die: "))

        results = roll_dice(num_dice, num_sides)
        print("Result(s):", ", ".join(map(str, results)))

        choice = input("Do you want to roll again? (yes/no): ")

        if choice.lower() != "yes":
            print("Thank you for using the Dice Roller App.")
            break
