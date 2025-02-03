import sys

input = sys.stdin.readline

n = int(input())
interest = list(map(int, input().split()))
view = list(map(int, input().split()))

result = [0, 0]

for i in range(n):
    result[0] += interest[i]
    result[1] += interest[i] * (1 - view[i])

print(*result, sep="\n")
