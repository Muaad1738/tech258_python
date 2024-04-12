#Calculator

def add(num1,num2):
    return num1+num2

def subtract(num1,num2):
    return num1-num2

def multiply(num1,num2):
    return num1*num2

def divide(num1,num2):
    return num1/num2

print ("choose 1 for addition, 2 for subtraction, 3 for multiplication, 4 for division")
operation = input()

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if operation == "1":
    result = add(num1,num2)
    print(result)

elif operation == "2":
    result = subtract(num1,num2)
    print(result)

elif operation == "3":
    result = multiply(num1,num2)
    print(result)

elif operation == "4":
    if num2 !=0:
        result = divide(num1,num2)
        print(result)
    else:
        print("not possible")

else:
    print("Invalid input")
cdddd


