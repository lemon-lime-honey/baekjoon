alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

n, b = map(int, input().split())
result = list()
while n > 0:
    temp = n % b
    if temp > 9:
        result.append(alpha[temp - 10])
    else:
        result.append(str(temp))
    n = n // b
print(''.join(result[::-1]))