import sys
input = sys.stdin.readline

n, m = map(int, input().split())
j = int(input())
left, right = 1, m
result = 0

for i in range(j):
    apple = int(input())
    if apple < left:
        result += left - apple
        right -= left - apple
        left = apple
    elif right < apple:
        result += apple - right
        left += apple - right
        right = apple

print(result)
