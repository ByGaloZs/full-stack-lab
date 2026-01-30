"""Program that adds two numbers and prints the result."""


def add(number1, number2):
    """Return the sum of two numbers."""
    return number1 + number2


def main():
    """Run the main logic."""
    num1 = 4
    num2 = 5

    total = add(num1, num2)

    print(f"The sum of {num1} and {num2} is {total}.")


if __name__ == "__main__":
    main()
