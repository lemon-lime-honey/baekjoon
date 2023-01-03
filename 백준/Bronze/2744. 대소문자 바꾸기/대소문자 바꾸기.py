word = input()
result = ''

for letter in word:
    if letter.isupper():
        result += letter.lower()
    else:
        result += letter.upper()

print(result)