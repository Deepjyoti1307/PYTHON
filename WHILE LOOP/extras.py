#WAP in python to enter a decimal number. Calculate and display the binary equivalent of this number .

# Program to convert decimal to binary
decimal_number = int(input("Enter a decimal number: "))
binary_number = bin(decimal_number)[2:]  # Use bin() and strip the "0b" prefix
print(f"The binary equivalent of {decimal_number} is {binary_number}.")




# WAP in python to binary number to equivalent decimal number .


# Program to convert binary to decimal
binary_number = input("Enter a binary number: ")
decimal_number = int(binary_number, 2)  # Use int() with base 2
print(f"The decimal equivalent of {binary_number} is {decimal_number}.")



#WAP in python to calculate GCD & LCM of two numbers .


# Program to calculate GCD and LCM
import math

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

gcd = math.gcd(num1, num2)  # Using math.gcd() for GCD
lcm = abs(num1 * num2) // gcd  # Formula for LCM

print(f"GCD of {num1} and {num2} is {gcd}.")
print(f"LCM of {num1} and {num2} is {lcm}.")



#WAP in python to read the numbers until -1 is encountered. Find the average of positive and negative numbers entered by the user .

# Program to calculate averages of positive and negative numbers
positive_sum = 0
positive_count = 0
negative_sum = 0
negative_count = 0

while True:
    num = int(input("Enter a number (-1 to stop): "))
    if num == -1:
        break
    if num > 0:
        positive_sum += num
        positive_count += 1
    elif num < 0:
        negative_sum += num
        negative_count += 1

if positive_count > 0:
    positive_avg = positive_sum / positive_count
    print(f"Average of positive numbers: {positive_avg}")
else:
    print("No positive numbers entered.")

if negative_count > 0:
    negative_avg = negative_sum / negative_count
    print(f"Average of negative numbers: {negative_avg}")
else:
    print("No negative numbers entered.")

