import sys

n, m = map(int, sys.stdin.readline().split())
pair = dict()

for i in range(n):
    address, password = map(str, sys.stdin.readline().split())
    pair[address] = password

for i in range(m):
    target = sys.stdin.readline().strip()
    print(pair[target])
