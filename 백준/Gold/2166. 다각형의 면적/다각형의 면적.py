import sys
input = sys.stdin.readline

n = int(input())
x_list = list()
y_list = list()

for i in range(n):
    x, y = map(int, input().split())
    x_list.append(x)
    y_list.append(y)

x_list.append(x_list[0])
y_list.append(y_list[0])

one, two = 0, 0

for i in range(n):
    one += x_list[i] * y_list[i + 1]
    two += y_list[i] * x_list[i + 1]

print(round(abs(one - two) / 2, 1))