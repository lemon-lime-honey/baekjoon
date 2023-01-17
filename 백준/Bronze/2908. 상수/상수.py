a, b = map(int, input().split())

aRev = int(str(a)[::-1])
bRev = int(str(b)[::-1])

print(max(aRev, bRev))
