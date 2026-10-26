
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
o = input("Enter the operator:")
if o == "+":
    Result= a + b
elif o == "-":
    Result= a - b
elif o == "*":
    Result= a * b
elif o == "/":
    if b == 0:
        print("Error: division by zero")
    else:
        Result= a / b
elif o == "//":
    if b == 0:
        print("Error: division by zero")
    else:
        Result= a // b
elif o == "%":
    if b == 0:
        print("Error: division by zero")
    else:
        Result= a % b
elif o == "**":
    Result= a ** b
else:
    print("Error: unknown operator")
