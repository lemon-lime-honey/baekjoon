n = int(input())
order = [0 for i in range(n)]
flip = list()
num = n - 1
idx = 0
d = True

while True:
    flip.append(idx + 1)
    if num == 0:
        order[idx] = n
        break
    order[idx] = num
    if d:
        idx += num
    else:
        idx -= num
    d = not d
    num -= 1

print("YES")
print(*order)
print(*flip)