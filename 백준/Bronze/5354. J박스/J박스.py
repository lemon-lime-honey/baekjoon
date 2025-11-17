n = int(input())

for i in range(n):
    size = int(input())
    if size < 3:
        for j in range(size):
            print("#" * size)
        print()
    else:
        print("#" * size)
        for j in range(size - 2):
            print("#" + "J" * (size - 2) + "#")
        print("#" * size)
        print()
