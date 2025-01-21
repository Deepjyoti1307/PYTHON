#Write a Python program to handle a ZeroDivisionError exception when dividing a number by zero.

try:
    num = 10
    result = num / 0
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")



# Write a Python program that prompts the user to input an integer and raises a ValueError exception if the input is not a valid integer.


try:
    user_input = input("Please enter an integer: ")
    num = int(user_input)
except ValueError:
    print("Error: Invalid input. Please enter a valid integer.")


# Write a Python program that executes division and handles an ArithmeticError exception if there is an arithmetic error.

try:
    num1 = 10
    num2 = 0
    result = num1 / num2
except ArithmeticError:
    print("Error: An arithmetic error occurred.")
