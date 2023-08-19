from collections import defaultdict
import datetime, sys
input = sys.stdin.readline

note = defaultdict(dict)

ipt = input().split()

n = int(ipt[0])
day = int(ipt[1][:3])
hour = int(ipt[1][4:6])
minute = int(ipt[1][7:9])
f = int(ipt[-1])

limit = datetime.timedelta(days=day, hours=hour, minutes=minute)

for i in range(n):
    data = input().split()
    time = datetime.datetime(
        year=int(data[0][:4]),
        month=int(data[0][5:7]),
        day=int(data[0][8:10]),
        hour=int(data[1][:2]),
        minute=int(data[1][3:])
    )
    if data[-2] in note[data[-1]]:
        note[data[-1]][data[-2]].append(time)
    else:
        note[data[-1]][data[-2]] = [time]

penalty = defaultdict(int)

for name, record in note.items():
    for key, value in record.items():
        for i in range(0, len(value), 2):
          chk = value[i + 1] - value[i]
          if chk > limit:
              penalty[name] += ((chk - limit).total_seconds() // 60) * f

result = list()

for name, cost in penalty.items():
    if cost:
        result.append((name, int(cost)))

result.sort()

if result:
    for i in range(len(result)):
        print(*result[i])
else:
    print(-1)