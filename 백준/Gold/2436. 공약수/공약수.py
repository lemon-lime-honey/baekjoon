def get_gcd(p, q):
    while True:
        if not q % p:
            return p
        q, p = p, q % p


gcd, lcm = map(int, input().split())
chk = lcm // gcd
result = [0, 0]

for i in range(1, int(chk ** 0.5) + 1):
    if not chk % i:
        a, b = i, chk // i
        if get_gcd(a, b) == 1:
            result[0] = a * gcd
            result[1] = b * gcd

print(*result)