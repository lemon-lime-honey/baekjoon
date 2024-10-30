d, h, w = map(int, input().split())
diag = (h ** 2 + w ** 2) ** 0.5

print(
   f"{int(d * h/diag)} {int(d * w/diag)}"
)
