import sys
input = sys.stdin.readline

k, l = map(int, input().split())
line = dict()

for i in range(l):
    ipt = input().rstrip()
    line[ipt] = i

for idx, num in enumerate(sorted(line.items(), key=lambda x: x[1])):
    if idx == k: break
    print(num[0])