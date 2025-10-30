from math import factorial

c = int(input())

for i in range(c):
    ipt = input().split()
    n, t, l = map(int, ipt[1:])
    l *= int(1e8)
    res = 0

    match ipt[0]:
        case "O(N)":
            res = n * t
        case "O(N^2)":
            res = t * n**2
        case "O(N^3)":
            res = t * n**3
        case "O(2^N)":
            res = t * 2**n
        case "O(N!)":
            res = t * factorial(n)

    if res <= l:
        print("May Pass.")
    else:
        print("TLE!")
