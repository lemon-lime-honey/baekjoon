from collections import deque
import sys
input = sys.stdin.readline


def round45(num) :
    return int(num) + [0, 1][num - int(num) >= 0.5]


n = int(input())

if not n: print(0)
else:
    difficulty = [int(input()) for i in range(n)]
    difficulty.sort()
    difficulty = deque(difficulty)

    for i in range(round45(n * 0.15)):
        difficulty.popleft()
        difficulty.pop()

    print(round45(sum(difficulty) / len(difficulty)))