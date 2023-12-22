v = int(input())
ipt = input()
a, b = 0, 0

for p in ipt:
    if p == 'A': a += 1
    else: b += 1

if a == b: print('Tie')
elif a > b: print('A')
else: print('B')