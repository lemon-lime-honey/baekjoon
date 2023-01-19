n, h, v = map(int, input().split())
side = list()

side.append(max(h, n - h))
side.append(max(v, n - v))

print(4 * side[0] * side[1])