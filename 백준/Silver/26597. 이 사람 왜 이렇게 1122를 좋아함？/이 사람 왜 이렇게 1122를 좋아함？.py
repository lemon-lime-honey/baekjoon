import sys

input = sys.stdin.readline

q = int(input())
start, end = -int(1e18), int(1e18)
idx = -1

for i in range(q):
    ipt = input().split()
    num = int(ipt[0])

    if ipt[1] == "^":
        start = max(start, num + 1)
    else:
        end = min(end, num - 1)
 
    if start == end and idx == -1:
        idx = i + 1
    elif end < start:
        print("Paradox!")
        print(i + 1)
        for j in range(q - i - 1):
            input()
        break
else:
    if idx == -1:
        print("Hmm...")
    else:
        print("I got it!")
        print(idx)
