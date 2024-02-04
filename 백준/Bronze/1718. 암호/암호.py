original = input()
key = input()
result = list()
idx = 0

for letter in original:
    if letter == ' ':
        result.append(letter)
    else:
        target = ord(letter) - (ord(key[idx]) - ord('a') + 1)
        if target < ord('a'):
            target += ord('z') - ord('a') + 1
        result.append(chr(target))

    idx += 1

    if idx > len(key) - 1:
        idx = 0

print(''.join(result))