mk = input()
minimum = list()
maximum = list()
cnt = 0

for letter in mk:
    if letter == 'M':
        cnt += 1
    else:
        if cnt > 0:
            minimum.append(str(10 ** cnt + 5))
            maximum.append(str(5 * 10 ** cnt))
        else:
            minimum.append('5')
            maximum.append('5')
        cnt = 0

if cnt > 0:
    minimum.append(str(10 ** (cnt - 1)))
    maximum.append('1' * cnt)

print(''.join(maximum), ''.join(minimum), sep='\n')