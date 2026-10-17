def area(l, b):
    return l * b


def perimeter(l, b):
    return 2 * (l + b)


def run():
    try:
        l = float(input("Enter length: "))
        b = float(input("Enter breadth: "))
    except ValueError:
        print("Please enter valid numbers.")
        return
    print(f"Area of Rectangle: {area(l, b):.2f}")
    print(f"Perimeter        : {perimeter(l, b):.2f}")


if __name__ == "__main__":
    run()