n, m = map(int, input().split())

if n > 0:
    books = list(map(int, input().split()))
    box = list()

    for i in range(n - 1, -1, -1):
        if not box:
            box.append(books[i])
        else:
            if box[-1] + books[i] <= m:
                box[-1] += books[i]
            else:
                box.append(books[i])

    print(len(box))
else:
    print(0)