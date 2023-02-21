def solution(arr):
    if len(arr) == 1:
        arr.pop()
        arr.append(-1)
    else:
        arr.pop(arr.index(min(arr)))
    return arr