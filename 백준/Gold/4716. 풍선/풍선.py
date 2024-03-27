import sys
input = sys.stdin.readline

while True:
    n, a, b = map(int, input().split())
    if n == a == b == 0:
        break

    data = sorted([list(map(int, input().split())) for i in range(n)],
                  key=lambda x: -abs(x[1] - x[2]))
    result = 0

    for k, da, db in data:
        if da < db:
            if a >= k:
                result += da * k
                a -= k
            else:
                result += da * a + db * (k - a)
                b -= k - a
                a = 0
        elif db < da:
            if b >= k:
                result += db * k
                b -= k
            else:
                result += db * b + da * (k - b)
                a -= k - b
                b = 0
        else:
            result += da * k

    print(result)