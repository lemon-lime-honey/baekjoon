from collections import Counter

a, b = map(Counter, input().split())
result = 0

for num1 in a:
    for num2 in b:
        result += int(num1) * int(num2) * a[num1] * b[num2]

print(result)