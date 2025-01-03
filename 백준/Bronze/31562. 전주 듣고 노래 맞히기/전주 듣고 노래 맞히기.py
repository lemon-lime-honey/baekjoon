from collections import defaultdict

n, m = map(int, input().split())
song = defaultdict(list)

for i in range(n):
    ipt = input().split()
    song[tuple(ipt[2:5])].append(ipt[1])

for i in range(m):
    melody = tuple(input().split())
    if melody not in song:
        print("!")
    elif len(song[melody]) > 1:
        print("?")
    else:
        print(song[melody][0])
