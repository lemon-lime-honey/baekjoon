n = int(input())
s = list(map(int, input().split()))
s.sort()
result = 1

for num in s:
    if result < num:
        break
    result += num

print(result)
