num1 = float(input("Num1 :"))
num2 = float(input("Num2 :"))
operation = input("Enter the operation needs to be performed: (+,-,*,/): ")
if (operation == "+"):
    print("sum =", num1+num2)
elif(operation == "-"):
    print(num1-num2)
elif(operation == "*"):
    print(num1*num2)
elif(operation =="/"):
    if(num2==0):
        print("Zero division Error")
    else:
        print(num1/num2)
else:
    print("Uknown operation", operation)