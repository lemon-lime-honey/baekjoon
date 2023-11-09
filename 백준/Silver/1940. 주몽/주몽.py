n = int(input())
m = int(input())
materials = sorted(list(map(int, input().split())))

lo, hi = 0, n - 1
result = 0

while lo < hi:
    if materials[lo] + materials[hi] < m:
        lo += 1
    else:
        if materials[lo] + materials[hi] == m:
            result += 1
        hi -= 1

print(result)