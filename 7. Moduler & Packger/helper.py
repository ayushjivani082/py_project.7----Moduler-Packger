import random
import importlib

import string_utils   


def _read_int(message):
    try:
        value = int(input(message))
    except ValueError:
        print("Please enter a whole number.")
        return None
    if value <= 0:
        print("Number 0 se bada hona chahiye.")
        return None
    return value


def random_number():
    try:
        low = int(input("Enter minimum value: "))
        high = int(input("Enter maximum value: "))
    except ValueError:
        print("Please enter whole numbers.")
        return
    if low > high:
        low, high = high, low
    print("Random Number:", random.randint(low, high))


def random_list():
    count = _read_int("How many numbers? ")
    if count is None:
        return
    print("Random List:", [random.randint(1, 100) for _ in range(count)])


def random_sampling():
    data = ["Amit", "Riya", "Karan", "Neha", "Raj", "Pooja", "Dev", "Sana"]
    print("Dataset:", data)
    k = _read_int("How many items to pick? ")
    if k is None:
        return
    if k > len(data):
        print("Dataset mein sirf", len(data), "items hain.")
        return
    print("Random Sample:", random.sample(data, k))


def dice_game():
    you, comp = random.randint(1, 6), random.randint(1, 6)
    print("You:", you, "| Computer:", comp)
    if you > comp:
        print("You win!")
    elif you < comp:
        print("Computer wins!")
    else:
        print("It's a tie!")


def random_menu():
    while True:
        print("\nRandom Data Generation:")
        print("1. Generate Random Number")
        print("2. Generate Random List")
        print("3. Create Random Password")
        print("4. Generate Random OTP")
        print("5. Random Sampling from Dataset")
        print("6. Dice Game Simulation")
        print("7. Back to Main Menu")
        choice = input("Enter your choice: ").strip()
        print()
        if choice == "1":
            random_number()
        elif choice == "2":
            random_list()
        elif choice == "3":
            string_utils.random_password()
        elif choice == "4":
            string_utils.random_otp()
        elif choice == "5":
            random_sampling()
        elif choice == "6":
            dice_game()
        elif choice == "7":
            break
        else:
            print("Invalid choice, try again.")
        print("=" * 28)


def explore_module():
    """dir() se kisi bhi built-in ya custom module ke attributes dikhata hai."""
    print("Explore Module Attributes:")
    print("(Examples: math, random, uuid, string_utils, shapes.circle)")
    name = input("Enter module name to explore: ").strip()
    if not name:
        print("Module name khali hai.")
        return
    try:
        module = importlib.import_module(name)
    except ImportError:
        print(f"Module '{name}' nahi mila.")
        return
    attributes = [a for a in dir(module) if not a.startswith("_")]
    print(f"Available Attributes in {name} module:")
    print(attributes)
    print("Total:", len(attributes))


if __name__ == "__main__":
    random_menu()