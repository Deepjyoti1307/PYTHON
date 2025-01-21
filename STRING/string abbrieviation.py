#Write a python program to Create a new string as abbreviation of name taken as input
#Example 1: Input : Netaji Subhas Chandra Bose
#Output : N.S.C.Bose

name = input("Enter the full name: ")
parts = name.split()
abbreviation = ""
for part in parts[:-1]:
    abbreviation += part[0].upper() + "."
abbreviation += parts[-1]
print(abbreviation)
