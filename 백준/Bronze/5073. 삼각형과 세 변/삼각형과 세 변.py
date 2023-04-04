while True:
    i, j, k = map(int, input().split())
    if i == j == k == 0: break

    if (max(i, j, k) >= (i + j + k - max(i, j, k))): print('Invalid')
    elif i == j == k: print('Equilateral')
    elif (i == j) or (j == k) or (k == i): print('Isosceles')
    elif (i != j) and (j != k) and (i != k): print('Scalene')