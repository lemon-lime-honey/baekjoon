n = int(input())

c = 0
nc = 0

for i in range(n):
    inp = int(input())
    if inp:
        c += 1
    else:
        nc += 1

if c < nc:
    print('Junhee is not cute!')
else:
    print('Junhee is cute!')