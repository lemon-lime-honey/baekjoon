n = int(input())
result, cnt = 0, 0

while n > 0:
    length = 0
    cnt += 1
    num = cnt

    while num > 0:
        length += 1
        num //= 10

    n -= length

for i in range(abs(n) + 1):
    result = cnt % 10
    cnt //= 10

print(result)