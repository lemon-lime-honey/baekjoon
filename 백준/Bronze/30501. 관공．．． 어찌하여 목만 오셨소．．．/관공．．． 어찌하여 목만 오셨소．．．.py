import sys

input = sys.stdin.readline

n = int(input())
flag = False

for i in range(n):
    name = input()
    if "S" in name:
        print(name)
        flag = True
    if flag:
        continue
