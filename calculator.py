# Python Programming 
# Task 1: Create a Simple Calculator

operations = input("Enter an operator (+, -, *, /): ")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if operations == '+':
    print(num1 + num2)
elif operations == '-':
    print(num1 - num2)
elif operations == '*':
    print(num1 * num2)
elif operations == '/':
    print(num1 / num2)
else:
    print(f"{operations} is not a valid operator.")