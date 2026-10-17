import math

from shapes import circle as shape_circle
from shapes import rectangle as shape_rectangle
from geometry import circle as geo_circle
from geometry import triangle as geo_triangle


def _num(message):
    while True:
        try:
            return float(input(message))
        except ValueError:
            print("Please enter a valid number.")


def factorial():
    try:
        n = int(input("Enter a number: "))
    except ValueError:
        print("Please enter a whole number.")
        return
    if n < 0:
        print("Negative number ka factorial nahi hota.")
        return
    print("Factorial:", math.factorial(n))


def compound_interest():
    """A = P * (1 + r/100) ** t"""
    p = _num("Enter principal amount: ")
    r = _num("Enter rate of interest (in %): ")
    t = _num("Enter time (in years): ")
    amount = p * math.pow(1 + r / 100, t)
    print(f"Compound Interest: {amount:.2f}")
    print(f"(Total amount = {amount:.2f}, Interest earned = {amount - p:.2f})")


def trigonometry():
    angle = _num("Enter angle in degrees: ")
    rad = math.radians(angle)
    print(f"sin({angle:g}) = {math.sin(rad):.4f}")
    print(f"cos({angle:g}) = {math.cos(rad):.4f}")
    if abs(math.cos(rad)) < 1e-12:
        print(f"tan({angle:g}) = undefined")
    else:
        print(f"tan({angle:g}) = {math.tan(rad):.4f}")


def area_menu():
    """Area of Geometric Shapes - shapes aur geometry packages use karta hai."""
    while True:
        print("\nArea of Geometric Shapes:")
        print("1. Circle (shapes package)")
        print("2. Rectangle (shapes package)")
        print("3. Triangle (geometry package)")
        print("4. Circle extras - arc & sector (geometry package)")
        print("5. Back")
        choice = input("Enter your choice: ").strip()
        print()
        if choice == "1":
            shape_circle.run()
        elif choice == "2":
            shape_rectangle.run()
        elif choice == "3":
            geo_triangle.run()
        elif choice == "4":
            geo_circle.run()
        elif choice == "5":
            break
        else:
            print("Invalid choice, try again.")


def menu():
    while True:
        print("\nMathematical Operations:")
        print("1. Calculate Factorial")
        print("2. Solve Compound Interest")
        print("3. Trigonometric Calculations")
        print("4. Area of Geometric Shapes")
        print("5. Back to Main Menu")
        choice = input("Enter your choice: ").strip()
        print()
        if choice == "1":
            factorial()
        elif choice == "2":
            compound_interest()
        elif choice == "3":
            trigonometry()
        elif choice == "4":
            area_menu()
        elif choice == "5":
            break
        else:
            print("Invalid choice, try again.")
        


if __name__ == "__main__":
    menu()