import sys
input = sys.stdin.readline

n = int(input())
relations = [[] for i in range(n + 1)]
chk = [0 for i in range(n + 1)]
white = list()
blue = list()

for i in range(1, n + 1):
    ipt = list(map(int, input().split()))
    relations[i].extend(ipt[1:])

for i in range(1, n + 1):
    if chk[i] == 0:
        blue.append(i)
        chk[i] = 1
        stack = [i]
        while stack:
            now = stack.pop()
            for next_one in relations[now]:
                if chk[next_one] != 0: continue
                if chk[now] == 1:
                    chk[next_one] = 2
                    white.append(next_one)
                else:
                    chk[next_one] = 1
                    blue.append(next_one)
                stack.append(next_one)

blue.sort()
white.sort()

print(len(blue))
print(*blue)
print(len(white))
print(*white)