rows = int(input("Enter the number of rows: "))

if rows <= 0:
    print("Please enter a positive number of rows.")
else:
    for row in range(rows, 0, -1):
        print("*" * row)
