t = int(input())

for i in range(t):
    width, length = map(int, input().split())
    for j in range(length):
        print('X' * width)
    print()