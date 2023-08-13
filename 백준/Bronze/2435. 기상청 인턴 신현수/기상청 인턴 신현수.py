n, k = map(int, input().split())
temp = list(map(int, input().split()))
addi = [0 for i in range(n)]
addi[0] = temp[0]

for i in range(1, n):
    addi[i] = addi[i - 1] + temp[i]
    if i > k - 1:
        addi[i] -= temp[i - k]

print(max(addi[k - 1:]))