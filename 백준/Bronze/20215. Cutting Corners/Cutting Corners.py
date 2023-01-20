from math import sqrt

w, h = map(int, input().split())
diag = sqrt(pow(w, 2) + pow(h, 2))
rect = w + h

print(rect - diag)