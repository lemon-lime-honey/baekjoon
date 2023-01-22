from math import cbrt

n = int(input())
c = list(map(float, input().split()))
total = 0
for num in c:
    total += pow(num, 3)
print(cbrt(total))