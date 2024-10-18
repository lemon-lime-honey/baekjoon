from collections import deque


def find(ring, target):
    cnt = 0
    ipt = deque(ring)

    while True:
        if cnt >= len(ring):
            return False

        while ipt[0] != target[0]:
            ipt.rotate(-1)
            cnt += 1
            if cnt == len(ring):
                return False

        for i in range(1, len(target)):
            if ipt[i] != target[i]:
                ipt.rotate(-1)
                cnt += 1
                break
        else:
            return True


target = input()
n = int(input())
result = 0

for i in range(n):
    ring = input()

    if find(ring, target):
        result += 1

print(result)
