words = list(map(str, input().split()))
result = list()

for word in words:
    for letter in word:
        if (len(result) == 0) * (letter == 'U'):
            result.append(letter)
            continue
        if (len(result) == 1) * (letter == 'C'):
            result.append(letter)
            continue
        if (len(result) == 2) * (letter == 'P'):
            result.append(letter)
            continue
        if (len(result) == 3) * (letter == 'C'):
            result.append(letter)
            continue
        if len(result) == 4:
            break
    if len(result) == 4:
        break

if (''.join(result)) == 'UCPC':
    print('I love UCPC')
else:
    print('I hate UCPC')