def heap_sort(lst):
    global cnt
    build_min_heap(lst, n)
    for i in range(n, 1, -1):
        cnt += 1
        if cnt == target:
            print(min(lst[1], lst[i]), max(lst[1], lst[i]))
        lst[1], lst[i] = lst[i], lst[1]
        heapify(lst, 1, i - 1)

def build_min_heap(lst, n):
    for i in range(n // 2, 0, -1):
        heapify(lst, i, n)

def heapify(lst, k, n):
    global cnt
    left = 2 * k
    right = 2 * k + 1
    if right <= n:
        if lst[left] < lst[right]:
            smaller = left
        else:
            smaller = right
    elif left <= n:
        smaller = left
    else:
        return
    
    if lst[smaller] < lst[k]:
        cnt += 1
        if cnt == target:
            print(min(lst[k], lst[smaller]), max(lst[k], lst[smaller]))
        lst[k], lst[smaller] = lst[smaller], lst[k]
        heapify(lst, smaller, n)

n, target = map(int, input().split())
a = [0] + list(map(int, input().split()))
cnt = 0
heap_sort(a)
if cnt < target:
    print(-1)