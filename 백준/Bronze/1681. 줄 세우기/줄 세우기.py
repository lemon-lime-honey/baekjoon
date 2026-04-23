n, l = map(str, input().split())
n = int(n)
result = 0

while n:
    result += 1
    if l not in str(result):
        n -= 1

print(result)
