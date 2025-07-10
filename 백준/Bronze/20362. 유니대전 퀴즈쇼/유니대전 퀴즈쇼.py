from collections import defaultdict

n, s = input().split()
n = int(n)

msg = defaultdict(int)

for i in range(n):
    ipt = input().split()
    if ipt[0] == s:
        for j in range(n - i - 1):
            input()
        print(msg[ipt[-1]])
        break
    else:
        msg[ipt[-1]] += 1
