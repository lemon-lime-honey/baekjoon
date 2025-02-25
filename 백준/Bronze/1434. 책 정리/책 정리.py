n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

idx = 0

for book in b:
    while a[idx] < book:
        idx += 1

    if book <= a[idx]:
        a[idx] -= book

print(sum(a))
