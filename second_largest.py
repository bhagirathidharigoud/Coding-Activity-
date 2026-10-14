numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

unique_numbers = sorted(set(numbers), reverse=True)

if len(unique_numbers) < 2:
    print("There is no second largest element.")
else:
    print(f"The second largest element is {unique_numbers[1]}.")
