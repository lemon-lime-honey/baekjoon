from collections import deque

n, w, l = map(int, input().split())
trucks = deque(map(int, input().split()))
bridge = deque([0 for i in range(w)])
time = 0

while bridge:
    time += 1
    bridge.popleft()

    if trucks:
        if sum(bridge) + trucks[0] > l:
            bridge.append(0)
        else:
            bridge.append(trucks.popleft())

print(time)