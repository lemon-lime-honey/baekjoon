import sys
input = sys.stdin.readline

n, m = map(int, input().split())
lamp = [0 for i in range(m + 1)]
sw = list()

for i in range(n):
    ipt = list(map(int, input().split()))
    sw.append(ipt[1:])
    for num in ipt[1:]:
        lamp[num] += 1

for i in range(n):
    for j in range(len(sw[i])):
        lamp[sw[i][j]] -= 1

    for j in range(1, m + 1):
        if not lamp[j]:
            break
    else:
        print(1)
        sys.exit()

    for j in range(len(sw[i])):
        lamp[sw[i][j]] += 1

print(0)