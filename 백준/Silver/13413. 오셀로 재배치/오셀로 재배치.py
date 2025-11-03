import sys

input = sys.stdin.readline

t = int(input())

for i in range(t):
    n = int(input())
    initial = input().rstrip()
    final = input().rstrip()
    
    bw = 0
    wb = 0
    
    for j in range(n):
        if initial[j] == "B" and final[j] == "W":
            bw += 1
        elif initial[j] == "W" and final[j] == "B":
            wb += 1

    print(max(bw, wb))
