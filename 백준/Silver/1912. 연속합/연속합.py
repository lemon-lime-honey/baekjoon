n = int(input())
number = list(map(int, input().split()))

for i in range(1, n):
    number[i] = max(number[i - 1] + number[i], number[i])

print(max(number))