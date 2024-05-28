from collections import deque
import sys
input = sys.stdin.readline


def rotate():
    belt.rotate(1)
    robots.rotate(1)
    for i in range(n, 2 * n):
        if robots[i] == 1: robots[i] = 0


def move():
    for i in range(n - 1, - 1, -1):
        if i == n - 1:
            robots[i] = 0
        else:
            if robots[i] == 1 and robots[i + 1] == 0 and belt[i + 1] >= 1:
                belt[i + 1] -= 1
                robots[i + 1], robots[i] = robots[i], robots[i + 1]


def put():
    if belt[0] != 0:
        belt[0] -= 1
        robots[0] = 1


def chk():
    result = 0
    for i in range(2 * n):
        if belt[i] == 0:
            result += 1
    return result


def run():
    result = 0

    while True:
        result += 1
        rotate()
        move()
        put()
        if k <= chk(): break

    return result


n, k = map(int, input().split())
belt = deque(map(int, input().split()))
robots = deque([0 for i in range(2 * n)])
print(run())
