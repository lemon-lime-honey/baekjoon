import sys

n, m = map(int, sys.stdin.readline().split())
number = list(map(int, sys.stdin.readline().split()))
num_sum = [0]
temp = 0

for num in number:
    temp += num
    num_sum.append(temp)

for k in range(m):
    i, j = map(int, sys.stdin.readline().split())
    print(num_sum[j] - num_sum[i - 1])