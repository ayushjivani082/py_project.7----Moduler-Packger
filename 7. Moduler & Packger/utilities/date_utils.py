import time
from datetime import datetime


def show_current_datetime():
    now = datetime.now()
    print("Current Date and Time:", now.strftime("%Y-%m-%d %H:%M:%S"))
    print("Friendly format      :", now.strftime("%A, %d %B %Y, %I:%M:%S %p"))


def _read_date(message):
    while True:
        text = input(message).strip()
        try:
            return datetime.strptime(text, "%Y-%m-%d")
        except ValueError:
            print("Invalid date! Format YYYY-MM-DD use karo (e.g. 2025-01-04).")


def date_difference():
    first = _read_date("Enter the first date (YYYY-MM-DD): ")
    second = _read_date("Enter the second date (YYYY-MM-DD): ")
    print("Difference:", abs((second - first).days), "days")


def format_date():
    date = _read_date("Enter a date (YYYY-MM-DD): ")
    print("Examples: %d/%m/%Y  |  %B %d, %Y  |  %A  |  %d-%b-%y")
    fmt = input("Enter your format: ").strip()
    if not fmt:
        fmt = "%d/%m/%Y"
        print("Kuch nahi diya, default format use kiya:", fmt)
    print("Formatted Date:", date.strftime(fmt))


def stopwatch():
    input("Press Enter to START the stopwatch...")
    start = time.time()
    input("Press Enter to STOP the stopwatch...")
    print(f"Elapsed time: {time.time() - start:.2f} seconds")


def countdown_timer():
    try:
        seconds = int(input("Enter time in seconds: "))
    except ValueError:
        print("Please enter a valid whole number.")
        return
    if seconds <= 0:
        print("Time 0 se bada hona chahiye.")
        return
    while seconds > 0:
        print("Time left:", seconds, "sec")
        time.sleep(1)
        seconds -= 1
    print("Time's up!")


def menu():
    while True:
        print("\nDatetime and Time Operations:")
        print("1. Display current date and time")
        print("2. Calculate difference between two dates/times")
        print("3. Format date into custom format")
        print("4. Stopwatch")
        print("5. Countdown Timer")
        print("6. Back to Main Menu")
        choice = input("Enter your choice: ").strip()
        print()
        if choice == "1":
            show_current_datetime()
        elif choice == "2":
            date_difference()
        elif choice == "3":
            format_date()
        elif choice == "4":
            stopwatch()
        elif choice == "5":
            countdown_timer()
        elif choice == "6":
            break
        else:
            print("Invalid choice, try again.")
        print("=" * 28)


if __name__ == "__main__":
    menu()