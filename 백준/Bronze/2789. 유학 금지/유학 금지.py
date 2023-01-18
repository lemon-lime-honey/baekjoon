chk = 'CAMBRIDGE'
original = input()
result = list()

for letter in original:
    if letter not in chk:
        result.append(letter)

print(''.join(result))