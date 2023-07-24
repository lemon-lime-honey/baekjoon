n = int(input())
rec = int(input())
students = list(map(int, input().split()))
photos = dict()

for i in range(rec):
    if students[i] in photos:
        photos[students[i]][0] += 1
    else:
        if len(photos) >= n:
            target = sorted(photos.items(), key=lambda x: (x[1][0], x[1][1]))[0]
            photos.pop(target[0])
            photos[students[i]] = [1, i]
        else:
            photos[students[i]] = [1, i]

print(*sorted(photos.keys()))