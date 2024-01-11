alphabet = [0 for i in range(26)]
a = input()
b = input()
result = 0

for letter in a:
    alphabet[ord(letter) - ord('a')] += 1

for letter in b:
    alphabet[ord(letter) - ord('a')] -= 1

for num in alphabet:
    if num > 0: result += num
    elif num < 0: result -= num

print(result)