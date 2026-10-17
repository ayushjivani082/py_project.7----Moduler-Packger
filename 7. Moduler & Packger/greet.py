from datetime import datetime


def get_greeting():
    hour = datetime.now().hour
    if hour < 12:
        return "Good Morning"
    elif hour < 17:
        return "Good Afternoon"
    return "Good Evening"


def welcome():
    print("Welcome to Multi-Utility Toolkit")
    


def goodbye():
    print("Thank you for using the Multi-Utility Toolkit!")
    


if __name__ == "__main__":
    welcome()
    goodbye()