import re

s = input()
k = input()

string = list()

for letter in s:
    if letter.isdigit(): continue
    string.append(letter)
  
print(1 if re.search(k, ''.join(string)) else 0)