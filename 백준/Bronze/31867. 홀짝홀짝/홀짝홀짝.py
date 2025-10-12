n = int(input())
k = input()

odd, even = 0, 0

for i in range(n):
    if int(k[i]) % 2:
        odd += 1
    else:
        even += 1

if odd < even:
    print(0)
elif odd > even:
    print(1)
else:
    print(-1)
