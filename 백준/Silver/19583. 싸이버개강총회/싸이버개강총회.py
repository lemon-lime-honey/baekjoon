import sys

input = sys.stdin.readline

s, e, q = input().split()
start = list(map(int, s.split(":")))
end = list(map(int, e.split(":")))
quit = list(map(int, q.split(":")))

record = dict()

while True:
    try:
        t, name = input().split()
        time = list(map(int, t.split(":")))

        if time[0] < start[0] or (time[0] == start[0] and time[1] <= start[1]):
            record[name] = False
        elif (
            (time[0] == end[0] and time[1] >= end[1])
            and (time[0] < quit[0] or (time[0] == quit[0] and time[1] <= quit[1]))
            or (
                time[0] > end[0]
                and (time[0] < quit[0] or time[0] == quit[0] and time[1] <= quit[1])
            )
        ):
            if name in record:
                record[name] = True
    except:
        break

result = 0

for key, value in record.items():
    if value:
        result += 1

print(result)
