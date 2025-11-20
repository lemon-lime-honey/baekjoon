a = list(map(int, input().split()))
b = list(map(int, input().split()))

while a[1] > 0 and b[1] > 0:
    a[1] -= b[0]
    b[1] -= a[0]

if a[1] > 0:
    print("PLAYER A")
elif b[1] > 0:
    print("PLAYER B")
else:
    print("DRAW")
