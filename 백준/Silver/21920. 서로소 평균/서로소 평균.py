def get_gcd(n1, n2):
    while True:
        if not n1 % n2:
            return n2
        n1, n2 = n2, n1 % n2


n = int(input())
a = list(map(int, input().split()))
x = int(input())
target = list()

for num in a:
    if get_gcd(max(x, num), min(x, num)) == 1:
        target.append(num)

print(sum(target) / len(target))