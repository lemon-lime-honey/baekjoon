padovan = [1, 1, 1]

for i in range(100):
    padovan.append(padovan[-3] + padovan[-2])

t = int(input())

6
for i in range(t):
    n = int(input())
    print(padovan[n - 1])