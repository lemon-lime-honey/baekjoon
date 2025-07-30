prime = [True for i in range(119)]
prime[0] = False
prime[1] = False

for i in range(2, int(119 ** 0.5) + 1):
    if prime[i]:
        for j in range(2 * i, 119, i):
            prime[j] = False

n = int(input())

for i in range(n):
    target = int(input())
    for j in range(2, target):
        if prime[j] and prime[target - j]:
            print("Yes")
            break
    else:
        print("No")
