n = int(input())
x = list(map(int, input().split()))
prefix = sum(x)
result = 0

for num in x:
    prefix -= num
    result += num * prefix

print(result)