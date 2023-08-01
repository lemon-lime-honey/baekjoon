from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
trains = [deque([False for i in range(20)]) for j in range(n)]
seat_set = set()

for i in range(m):
    command = list(map(int, input().split()))
    if command[0] == 1:
        if not trains[command[1] - 1][command[2] - 1]:
            trains[command[1] - 1][command[2] - 1] = True
    elif command[0] == 2:
        if trains[command[1] - 1][command[2] - 1]:
            trains[command[1] - 1][command[2] - 1] = False
    elif command[0] == 3:
        trains[command[1] - 1].pop()
        trains[command[1] - 1].appendleft(False)
    elif command[0] == 4:
        trains[command[1] - 1].popleft()
        trains[command[1] - 1].append(False)

for train in trains:
    seat_set.add(tuple(train))

print(len(seat_set))