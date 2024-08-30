import sys
input = sys.stdin.readline

for a in range(1, 10):
    print("? A", a, flush=True)

    resp = int(input())

    if resp == 1:
        flag = False
        for b in range(1, 10):
            print("? B", b, flush=True)
            if int(input()) == 1:
                print("!", a + b)
                flag = True
                break
        if flag:
            break
