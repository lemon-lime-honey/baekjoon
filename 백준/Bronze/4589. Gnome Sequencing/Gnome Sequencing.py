n = int(input())
print('Gnomes:')

for i in range(n):
    original = list(map(int, input().split()))
    asc = sorted(original)
    desc = sorted(original, reverse = True)
    if (original == asc) + (original == desc):
        print('Ordered')
    else:
        print('Unordered')