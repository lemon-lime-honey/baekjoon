alphabet = 'abcdefghijklmnopqrstuvwxyz'
alpha = [0] * 26
s = input()

for letter in s:
    alpha[alphabet.index(letter)] += 1

for num in alpha:
    print(num, end = ' ')