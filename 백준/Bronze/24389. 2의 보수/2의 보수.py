n = int(input())

ref = 0

for i in range(32):
    ref |= 1 << i

complement = (ref ^ n) + 1
result = 0

for i in range(32):
    if complement & (1 << i) != n & (1 << i):
        result += 1

print(result)