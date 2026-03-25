try:
    x = int(input("Enter number: "))
    print(10 / x)
except ValueError:
    print("Invalid input!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
    