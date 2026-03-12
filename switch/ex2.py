def calculator():
    a=int(input("Enter a number a:"))
    b=int(input("Enter a number b:"))
    op=int(input("Select an operation:"))

match(op):
case 1:
if(op=='+'):
    add=a+b
    print("The sum of a and b is:",add)
case 2:
if(op=='-'):
    sub=a-b
    print("The difference of a and b is:",sub)
case 3:
if(op=='*'):
    mul=a*b
    print("The product of a and b is:",mul)
case 4:
if(op=='/'):
    if b!=0:
        div=a/b
        print("The quotient of a and b is:",div)
    else:
        print("Error: Division by zero is not allowed.")
case 5:
if(op=='%'):
    mod=a%b
    print("The modulus of a and b is:",mod)
case 6:
if(op=='**'):
    exp=a**b
    print("The result of a raised to the power of b is:",exp)
default:
print("Invalid choice. Please select a valid operation.")
calculator()