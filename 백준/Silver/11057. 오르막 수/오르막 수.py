n = int(input())

number = [[0 for i in range(10)] for j in range(n)]

for i in range(10):
    number[0][i] = 1

for i in range(1, n):
    for j in range(10):
        number[i][j] = sum(number[i - 1][:j + 1])

print(sum(number[-1]) % 10007)