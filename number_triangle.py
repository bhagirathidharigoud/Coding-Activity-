rows = int(input("Enter the number of rows: "))

if rows <= 0:
    print("Please enter a positive number of rows.")
else:
    for row in range(1, rows + 1):
        for number in range(1, row + 1):
            print(number, end=" ")
        print()
