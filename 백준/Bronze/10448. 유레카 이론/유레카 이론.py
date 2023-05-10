triangle = [i * (i + 1) // 2 for i in range(1, 46)]
eureka = [False for i in range(1001)]

for n1 in triangle:
    for n2 in triangle:
        for n3 in triangle:
            n = n1 + n2 + n3
            if n < 1001: eureka[n] = True

t = int(input())

for i in range(t):
    k = int(input())
    print(1 if eureka[k] else 0)