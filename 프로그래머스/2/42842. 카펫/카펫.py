def solution(brown, yellow):
    size = brown + yellow
    
    for i in range(size - 1, 0, -1):
        if size % i: continue
        j = size // i
        if (i - 2) * (j - 2) == yellow and (size - (i - 2) * (j - 2)) == brown:
            return [max(i, j), min(i, j)]

    return [0, 0]