import sys

mbti = sys.stdin.readline().strip()
n = int(sys.stdin.readline())
result = 0

for i in range(n):
    temp = sys.stdin.readline().strip()
    if temp == mbti:
        result += 1

print(result)