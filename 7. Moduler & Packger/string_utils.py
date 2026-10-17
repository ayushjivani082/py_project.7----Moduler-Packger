import random
import string
import uuid


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


def make_password(length):
    symbols = "@#$%&!"
    chars = [
        random.choice(string.ascii_uppercase),
        random.choice(string.ascii_lowercase),
        random.choice(string.digits),
        random.choice(symbols),
    ]
    pool = string.ascii_letters + string.digits + symbols
    chars += [random.choice(pool) for _ in range(length - 4)]
    random.shuffle(chars)
    return "".join(chars)


def make_otp(digits=6):
    """Random OTP string."""
    return "".join(random.choice(string.digits) for _ in range(digits))


def random_password():
    length = _read_int("Enter password length: ")
    if length is None:
        return
    if length < 4:
        print("Password kam se kam 4 characters ka rakho.")
        return
    print("Generated Password:", make_password(length))


def random_otp():
    print("Generated OTP:", make_otp())

def generate_uuid():
    print("Generated UUID:", uuid.uuid4())


def generate_invoice_id():
    name = input("Enter invoice/record name (e.g. INV): ").strip().upper()
    if not name:
        name = "ID"
    print(f"Generated ID: {name}-{uuid.uuid4()}")


def generate_multiple():
    try:
        count = int(input("How many UUIDs? "))
    except ValueError:
        print("Please enter a whole number.")
        return
    for i in range(1, max(count, 0) + 1):
        print(f"{i}. {uuid.uuid4()}")


def uuid_menu():
    while True:
        print("\nGenerate Unique Identifiers:")
        print("1. Generate a UUID")
        print("2. Generate invoice / record ID")
        print("3. Generate multiple UUIDs")
        print("4. Back to Main Menu")
        choice = input("Enter your choice: ").strip()
        print()
        if choice == "1":
            generate_uuid()
        elif choice == "2":
            generate_invoice_id()
        elif choice == "3":
            generate_multiple()
        elif choice == "4":
            break
        else:
            print("Invalid choice, try again.")
        print("=" * 28)


if __name__ == "__main__":
    uuid_menu()