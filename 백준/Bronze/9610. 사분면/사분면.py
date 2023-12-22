titles = ['Q1', 'Q2', 'Q3', 'Q4', 'AXIS']
cnt = dict.fromkeys(titles, 0)

n = int(input())
for i in range(n):
    x, y = map(int, input().split())
    if x > 0 and y > 0:
        cnt['Q1'] += 1
    elif x < 0 and y > 0:
        cnt['Q2'] += 1
    elif x < 0 and y < 0:
        cnt['Q3'] += 1
    elif x > 0 and y < 0:
        cnt['Q4'] += 1
    else:
        cnt['AXIS'] += 1

for title in titles:
    print(f'{title}: {cnt[title]}')