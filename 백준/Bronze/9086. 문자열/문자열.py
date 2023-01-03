import sys

num = int(sys.stdin.readline())

for i in range(num):
    temp = sys.stdin.readline().strip()
    print(temp[0] + temp[-1])