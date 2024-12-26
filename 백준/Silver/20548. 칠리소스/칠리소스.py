c = int(input())
num = 1
result = 0

while c:
    result += (c % 7) * num
    c //= 7
    num *= 3

print(result)
