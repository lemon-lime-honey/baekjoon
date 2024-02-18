import sys
input = sys.stdin.readline

n = int(input())
a = list()
b = list()
c = list()
d = list()

for i in range(n):
    ipt = list(map(int, input().split()))
    a.append(ipt[0])
    b.append(ipt[1])
    c.append(ipt[2])
    d.append(ipt[3])

calc = dict()
result = 0

for n1 in a:
    for n2 in b:
        if n1 + n2 in calc:
            calc[n1 + n2] += 1
        else:
            calc[n1 + n2] = 1

for n1 in c:
    for n2 in d:
        if -(n1 + n2) in calc:
            result += calc[-(n1 + n2)]

print(result)