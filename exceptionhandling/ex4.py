try:
    num = int(input("Enter a number: "))
    print(num * 2)
except ValueError:
    print("Please enter a valid integer!")