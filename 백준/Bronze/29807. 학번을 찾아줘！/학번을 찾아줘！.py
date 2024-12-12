import sys

input = sys.stdin.readline

t = int(input())
score = list(map(int, input().split())) + [0 for i in range(5 - t)]

result = 0

if score[0] > score[2]:
    result += (score[0] - score[2]) * 508
else:
    result += (score[2] - score[0]) * 108

if score[1] > score[3]:
    result += (score[1] - score[3]) * 212
else:
    result += (score[3] - score[1]) * 305

result += score[4] * 707

result *= 4763

print(result)
