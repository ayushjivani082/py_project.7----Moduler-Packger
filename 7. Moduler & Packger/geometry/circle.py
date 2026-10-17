import math


def arc_length(r, angle):
    return 2 * math.pi * r * (angle / 360)


def sector_area(r, angle):
    return math.pi * r ** 2 * (angle / 360)


def run():
    try:
        r = float(input("Enter radius: "))
        angle = float(input("Enter angle in degrees: "))
    except ValueError:
        print("Please enter valid numbers.")
        return
    print(f"Arc Length : {arc_length(r, angle):.2f}")
    print(f"Sector Area: {sector_area(r, angle):.2f}")


if __name__ == "__main__":
    run()