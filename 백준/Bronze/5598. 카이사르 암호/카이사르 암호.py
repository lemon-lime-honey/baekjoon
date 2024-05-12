word = input()

for letter in word:
    target = ord(letter) - 3
    if target < 65:
        target += 26
    print(chr(target), end='')