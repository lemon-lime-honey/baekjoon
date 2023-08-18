from collections import defaultdict
import sys
input = sys.stdin.readline

trees = defaultdict(int)
total = 0

while True:
    ipt = input().rstrip()
    if not ipt: break
    trees[ipt] += 1
    total += 1

name = sorted(list(trees))

for i in range(len(name)):
    print(f'{name[i]} {trees[name[i]] * 100 / total:.4f}')