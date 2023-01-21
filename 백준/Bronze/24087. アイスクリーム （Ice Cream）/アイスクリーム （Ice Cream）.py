from math import ceil

s = int(input())
a = int(input())
b = int(input())

if s <= a:
    result = 250
else:
    result = 250 + ceil((s - a) / b) * 100

print(result)