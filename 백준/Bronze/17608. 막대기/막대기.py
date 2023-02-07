import sys

n = int(sys.stdin.readline())
stick = list()

for i in range(n):
    stick.append(int(sys.stdin.readline()))

ref = stick.pop()
result = 1

while stick:
    chk = stick.pop()
    if chk > ref:
        ref = chk
        result += 1

print(result)