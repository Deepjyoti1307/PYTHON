#WAP in python to calculate the factorial of a number using for loop.

import math
x=int(input("Enter number: "))
fact=math.factorial(x)
print(f"The factorial of {x} is {fact}")


#WAP in python to print prime numbers within a given range .

lower = int(input("Enter Lower range: "))
upper = int(input("Enter Higher range: "))
print("Prime numbers between", lower, "and", upper, "are:")
for num in range(lower, upper + 1):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num, end=" ")


#8. WAP in python to calculate the sum of series 1/1+22/2+32/3+……+n2/n.[print the series also]

n = int(input("Enter Limit: "))
sum = 0
print("Series:")
for i in range(1, n + 1):
    term = (i ** 2) // i
    sum += term
    print(f"{i}^2/{i}", end=" + " if i < n else "\n")
print(f"Sum of the series: {sum}")


#10. WAP in python to calculate the sum of series 1/1! +2/2! 3/3!... [print the series also]

import math
n = int(input("Enter Limit: "))
sum = 0.0
for i in range(1, n + 1):
    term = i / math.factorial(i)
    sum += term
    print(f"{i}/{i}!", end=" + " if i < n else "\n")
print("Sum:", sum)


#12.WAP in python to calculate the sum of series 1/x+2/x2+3/x3+…[print the series also]

x = float(input("Enter the value of x: "))
n = int(input("Enter the number of terms: "))
sum = 0.0
for i in range(1, n + 1):
    term = i / x**i
    sum += term
    print(f"{i}/{x}^{i}", end=" + " if i < n else "\n")
print("Sum:", sum)