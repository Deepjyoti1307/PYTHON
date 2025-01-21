#Write a Python program to remove duplicate values from dictionary.
# Input dictionary
data = {
    'a': 10,
    'b': 20,
    'c': 10,
    'd': 30,
    'e': 20
}

# Remove duplicates
unique_values = set()
result = {}

for key, value in data.items():
    if value not in unique_values:
        unique_values.add(value)
        result[key] = value

# Display the result
print("Original dictionary:", data)
print("Dictionary after removing duplicates:", result)
