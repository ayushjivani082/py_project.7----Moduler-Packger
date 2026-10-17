import os
import sys

# Kahin se bhi run karo, saare modules/packages mil jayein
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import greet
import math_utils
import string_utils
import helper
from utilities import date_utils, file_utils


def show_menu():
    print("Choose an option:")
    print("1. Datetime and Time Operations")
    print("2. Mathematical Operations")
    print("3. Random Data Generation")
    print("4. Generate Unique Identifiers (UUID)")
    print("5. File Operations (Custom Module)")
    print("6. Explore Module Attributes (dir())")
    print("7. Exit")


def main():
    actions = {
        "1": ("Datetime and Time Operations", date_utils.menu),
        "2": ("Mathematical Operations", math_utils.menu),
        "3": ("Random Data Generation", helper.random_menu),
        "4": ("Generate Unique Identifiers", string_utils.uuid_menu),
        "5": ("File Operations", file_utils.menu),
        "6": ("Explore Module Attributes", helper.explore_module),
    }

    file_utils.write_log("Toolkit started")
    greet.welcome()

    while True:
        show_menu()
        choice = input("Enter your choice: ").strip()
        print()

        if choice in actions:
            name, func = actions[choice]
            file_utils.write_log("Opened: " + name)
            func()
        elif choice == "7":
            file_utils.write_log("Toolkit closed")
            greet.goodbye()
            break
        else:
            print("Invalid choice! Please enter a number from 1 to 7.\n")


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\nProgram stopped. Bye!")