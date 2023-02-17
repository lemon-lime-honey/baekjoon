import sys

n = int(sys.stdin.readline())
number = list(map(int, sys.stdin.readline().split()))
x = int(sys.stdin.readline())

number.sort()
before = 0
after = n - 1
result = 0

while before < after:
    temp = number[before] + number[after]

    if temp == x:
        result += 1
        before += 1
    elif temp > x:
        after -= 1
    else:
        before += 1

print(result)