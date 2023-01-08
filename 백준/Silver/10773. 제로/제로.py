import sys

num = list()
k = int(sys.stdin.readline())

for i in range(k):
    temp = int(sys.stdin.readline())
    if temp == 0:
        num.pop()
    else:
        num.append(temp)

try:
    print(sum(num))
except:
    print(0)