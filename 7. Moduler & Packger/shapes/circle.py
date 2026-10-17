import math


def area(r):
    return math.pi * r ** 2


def circumference(r):
    return 2 * math.pi * r


def run():
    try:
        r = float(input("Enter radius: "))
    except ValueError:
        print("Please enter a valid number.")
        return
    print(f"Area of Circle: {area(r):.2f}")
    print(f"Circumference : {circumference(r):.2f}")


if __name__ == "__main__":
    run()