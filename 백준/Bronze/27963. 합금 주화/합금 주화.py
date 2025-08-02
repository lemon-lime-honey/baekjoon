d1, d2, chi = map(int, input().split())

if d1 < d2:
    d1, d2 = d2, d1

chi /= 100

print(1 / (chi / d1 + (1 -chi) / d2))