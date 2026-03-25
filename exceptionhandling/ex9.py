class NegativeNumberError(Exception):
    pass

try:
    num = int(input("Enter number: "))
    if num < 0:
        raise NegativeNumberError("Negative not allowed!")
except NegativeNumberError as e:
    print(e)