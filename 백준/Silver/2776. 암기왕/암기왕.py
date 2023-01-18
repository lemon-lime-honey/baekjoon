t = int(input())

for i in range(t):
    n = int(input())
    one = set(map(int, input().split()))
    m = int(input())
    two = list(map(int, input().split()))

    for num in two:
        if num in one:
            print(1)
        else:
            print(0)