a, b = map(int, input().split())

large, small = max(a, b), min(a, b)

while True:
    if not (large % small):
        print('1' * small)
        break
    large, small = small, large % small