n = int(input())
deg = [int(input()) for i in range(n)]

easiest = min(deg)
hardest = max(deg)

if deg[0] == easiest:
    print("ez")
elif deg[0] == hardest:
    print("hard")
else:
    print("?")
