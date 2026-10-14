number = int(input("Enter a number: "))

digits = str(number)
power = len(digits)

if number >= 0 and sum(int(digit) ** power for digit in digits) == number:
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is not an Armstrong number.")
