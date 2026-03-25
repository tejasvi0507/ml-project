num = int(input("Enter a positive number: "))

if num < 0:
    raise ValueError("Number must be positive!")

print("You entered:", num)