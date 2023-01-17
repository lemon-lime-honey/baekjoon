import sys

n, m = map(int, sys.stdin.readline().split())
poke1 = dict()
poke2 = dict()

for i in range(n):
    name = sys.stdin.readline().strip()
    poke1[i + 1] = name
    poke2[name] = i + 1

for j in range(m):
    q = sys.stdin.readline().strip()
    try:
        q = int(q)
        print(poke1[q])
    except:
        print(poke2[q])
