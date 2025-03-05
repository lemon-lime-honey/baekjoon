n, m = map(int, input().split())
key = input()

for _ in range(m):
    i, j = 0, 0
    target = input()
    while i < len(key) and j < len(target):
        if key[i] == target[j]:
            i += 1
        j += 1
    if i == len(key):
        print("true")
    else:
        print("false")
