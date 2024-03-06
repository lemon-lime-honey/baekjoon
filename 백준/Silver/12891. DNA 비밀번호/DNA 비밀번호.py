s, p = map(int, input().split())
password = input()
requirements = list(map(int, input().split()))
dna_string = 'ACGT'
cnt = [0, 0, 0, 0]
result = 0

for i in range(p):
    cnt[dna_string.index(password[i])] += 1

lo, hi = 0, p -1

while hi < s - 1:
    if (cnt[0] >= requirements[0] and
        cnt[1] >= requirements[1] and
        cnt[2] >= requirements[2] and
        cnt[3] >= requirements[3]):
        result += 1
    cnt[dna_string.index(password[lo])] -= 1
    cnt[dna_string.index(password[hi + 1])] += 1
    lo += 1
    hi += 1

if (cnt[0] >= requirements[0] and
    cnt[1] >= requirements[1] and
    cnt[2] >= requirements[2] and
    cnt[3] >= requirements[3]):
    result += 1

print(result)