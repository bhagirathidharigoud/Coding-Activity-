# -------------------- Factorial Using a Function --------------------
def factorial(number: int) -> int:
    """Return the factorial of a non-negative integer."""
    if number < 0:
        raise ValueError("Factorial is not defined for negative numbers.")

    result = 1
    for value in range(1, number + 1):
        result *= value
    return result


# -------------------- Get Input and Display Result --------------------
if __name__ == "__main__":
    try:
        number = int(input("Enter a non-negative integer: "))
        print(f"{number}! = {factorial(number)}")
    except ValueError as error:
        print(error)
