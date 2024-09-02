n, l, h = map(int, input().split())
scores = sorted(list(map(int, input().split())))
print(sum(scores[l:n-h])/(n - l - h))
