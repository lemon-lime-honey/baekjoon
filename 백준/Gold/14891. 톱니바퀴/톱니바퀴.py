from collections import deque
import sys
input = sys.stdin.readline


def chkLeft(idx, d):
    if idx == 1: return
    for i in range(idx - 1, 0, -1):
        if gears[i + 1][6] == gears[i][2]:
            return
        targets.append((i, d))
        d *= -1


def chkRight(idx, d):
    if idx == 4: return
    for i in range(idx, 4):
        if gears[i][2] == gears[i + 1][6]:
            return
        targets.append((i + 1, d))
        d *= -1


def rotate():
    for n, d in targets:
        gears[n].rotate(d)


one = deque(map(int, list(input().rstrip())))
two = deque(map(int, list(input().rstrip())))
three = deque(map(int, list(input().rstrip())))
four = deque(map(int, list(input().rstrip())))

k = int(input())

gears = {1: one, 2: two, 3: three, 4: four}
score = [0, 1, 2, 4, 8]

for i in range(k):
    number, direction = map(int, input().split())
    targets = [(number, direction)]
    chkLeft(number, -1 * direction)
    chkRight(number, -1 * direction)
    rotate()

result = 0

for i in range(1, 5):
    if gears[i][0] == 1:
        result += score[i]

print(result)
