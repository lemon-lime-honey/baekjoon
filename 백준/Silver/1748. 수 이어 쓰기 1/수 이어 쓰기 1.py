n = int(input())
result = 0
ref = 1

while ref < n + 1:
    result += n - ref + 1
    ref *= 10

print(result)