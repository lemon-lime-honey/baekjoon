def get_gcd(n1, n2):
    while True:
        if not (n1 % n2):
            return n2
        n1, n2 = n2, n1 % n2

n = int(input())
ring = list(map(int, input().split()))

for i in range(1, n):
    big = max(ring[i], ring[0])
    small = min(ring[i], ring[0])
    gcd = get_gcd(big, small)
    print(f'{ring[0] // gcd}/{ring[i] // gcd}')