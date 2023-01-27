k = int(input())
result = list()

for i in range(k - 1, 2 * k - 1):
    result.append('1')

for i in range(k - 1):
    result.append('0')

print(''.join(result))