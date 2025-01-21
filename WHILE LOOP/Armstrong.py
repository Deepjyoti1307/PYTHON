# Input from user
number = int(input("Enter a number: "))
temp = number
sum_of_powers = 0
power = len(str(number))  # Number of digits in the number

# Calculate the sum of powers of digits
while temp > 0:
    digit = temp % 10  # Extract the last digit
    sum_of_powers += digit ** power
    temp //= 10  # Remove the last digit

# Check and display result
if sum_of_powers == number:
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is not an Armstrong number.")
