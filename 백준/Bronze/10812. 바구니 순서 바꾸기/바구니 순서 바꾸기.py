from collections import deque

n, m = map(int, input().split())
basket = list(range(1, n + 1))

for i in range(m):
    begin, end, mid = map(int, input().split())
    temp = deque(basket[begin - 1:end])
    temp.rotate(begin - mid)
    basket[begin - 1:end] = temp

print(*basket)