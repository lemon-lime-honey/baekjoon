a, b, c, m = map(int, input().split())
fatigue = 0
work = 0
time = 0

while time < 24:
    if fatigue <= m - a:
        work += b
        fatigue += a
    else:
        fatigue = max(fatigue - c, 0)
    time += 1

print(work)