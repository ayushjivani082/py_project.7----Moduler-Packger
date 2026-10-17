import os
from datetime import datetime

LOG_FILE = "toolkit_log.txt"


def create_file():
    name = input("Enter file name: ").strip()
    if not name:
        print("File name khali nahi ho sakta.")
        return
    try:
        with open(name, "x"):
            pass
        print("File created successfully!")
    except FileExistsError:
        print("File already exists!")
    except OSError as e:
        print("Error:", e)


def write_file():
    name = input("Enter file name: ").strip()
    data = input("Enter data to write: ")
    try:
        with open(name, "w") as f:
            f.write(data)
        print("Data written successfully!")
    except OSError as e:
        print("Error:", e)


def read_file():
    name = input("Enter file name: ").strip()
    if not os.path.exists(name):
        print("File not found!")
        return
    try:
        with open(name, "r") as f:
            print("File Content:")
            print(f.read())
    except OSError as e:
        print("Error:", e)


def append_file():
    name = input("Enter file name: ").strip()
    if not os.path.exists(name):
        print("File not found! Pehle create karo.")
        return
    data = input("Enter data to append: ")
    try:
        with open(name, "a") as f:
            f.write("\n" + data)
        print("Data appended successfully!")
    except OSError as e:
        print("Error:", e)


def write_log(message):
    """Actions ko log file mein save karta hai."""
    try:
        stamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(LOG_FILE, "a") as f:
            f.write(f"[{stamp}] {message}\n")
    except OSError:
        pass


def menu():
    while True:
        print("\nFile Operations:")
        print("1. Create a new file")
        print("2. Write to a file")
        print("3. Read from a file")
        print("4. Append to a file")
        print("5. Back to Main Menu")
        choice = input("Enter your choice: ").strip()
        print()
        if choice == "1":
            create_file()
        elif choice == "2":
            write_file()
        elif choice == "3":
            read_file()
        elif choice == "4":
            append_file()
        elif choice == "5":
            break
        else:
            print("Invalid choice, try again.")
        print("=" * 28)


if __name__ == "__main__":
    menu()