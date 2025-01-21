#Write a python program to Write a program to count occurrences of all characters within a string
#Input = Apple
#Output :A: 1, p: 2,l: 1, e: 1
def count(str1):
  dict = {}
  for n in str1:
    keys = dict.keys()
    if n in keys:
      dict[n] += 1
    else:
      dict[n] = 1
  return dict
print(count('Apple'))