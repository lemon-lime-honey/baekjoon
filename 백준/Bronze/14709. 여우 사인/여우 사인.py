n = int(input())

if n != 3:
    for i in range(n):
        input()
    print("Woof-meow-tweet-squeek")
else:
    target = {(1, 3), (1, 4), (3, 4)}
    for i in range(n):
        chk = tuple(sorted(list(map(int, input().split()))))
        if chk not in target:
            print("Woof-meow-tweet-squeek")
            break
    else:
        print("Wa-pa-pa-pa-pa-pa-pow!")