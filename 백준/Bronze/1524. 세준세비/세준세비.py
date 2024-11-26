import sys

input = sys.stdin.readline

t = int(input())

for i in range(t):
    input()
    n, m = map(int, input().split())
    s = list(map(int, input().split()))
    b = list(map(int, input().split()))

    s.sort(reverse=True)
    b.sort(reverse=True)
    
    while s and b:
        if b[-1] <= s[-1]:
            b.pop()
        else:
            s.pop()
            
    if s:
        print("S")
    elif b:
        print("B")
    else:
        print("C")
