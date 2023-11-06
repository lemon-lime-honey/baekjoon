def get_gcd(n1, n2):
    while True:
        if not n1 % n2: return n2
        n1, n2 = n2, n1 % n2


n = int(input())
nums = sorted(list(map(int, input().split())))
gcd = get_gcd(nums[1], nums[0])

for i in range(2, n):
    gcd = get_gcd(nums[i], gcd)

for i in range(1, gcd + 1):
    if not gcd % i: print(i)