def solution(arr):
    r, c = len(arr), len(arr[0])
    if r < c:
        for i in range(c - r):
            arr.append([0 for j in range(c)])
    elif r > c:
        for i in range(r):
            arr[i].extend([0 for j in range(r - c)])
    return arr