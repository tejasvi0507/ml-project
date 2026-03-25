try:
    num = int(input("Enter number: "))
except ValueError:
    print("Wrong input!")
else:
    print("Square is:", num * num)