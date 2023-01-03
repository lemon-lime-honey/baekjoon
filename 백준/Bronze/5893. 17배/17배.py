n = input()
n = n[::-1]
result = 0

for i in range(len(n)):
    result += int(n[i]) * (2 ** i)

result *= 17
result = format(result, 'b')

print(result)