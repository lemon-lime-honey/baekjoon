n = int(input())
num = list(map(int, input().split()))
result = 0

for number in num:
    if number <= n:
        result += number
    else:
        result += n

print(result)