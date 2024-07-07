import sys
input = sys.stdin.readline

n = int(input())

for i in range(n):
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    star, circle, square, triangle = 0, 0, 0, 0
    
    for s in a[1:]:
        if s == 4: star += 1
        elif s == 3: circle += 1
        elif s == 2: square += 1
        else: triangle += 1

    for s in b[1:]:
        if s == 4: star -= 1
        elif s == 3: circle -= 1
        elif s == 2: square -= 1
        else: triangle -= 1

    if star < 0: print("B")
    elif star > 0: print("A")
    elif circle < 0: print("B")
    elif circle > 0: print("A")
    elif square < 0: print("B")
    elif square > 0: print("A")
    elif triangle < 0: print("B")
    elif triangle > 0: print("A")
    else: print("D")
