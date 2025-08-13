n = int(input())
first = int(input())

if n >= 6:
    print("Love is open door")
else:
    for i in range(2, n + 1):
        first = (first + 1) % 2
        print(first)
