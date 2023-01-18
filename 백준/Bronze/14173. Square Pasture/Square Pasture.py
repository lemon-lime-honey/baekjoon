square1 = list(map(int, input().split()))
square2 = list(map(int, input().split()))

left = min(square1[0], square2[0])
bottom = min(square1[1], square2[1])
right = max(square1[2], square2[2])
top = max(square1[3], square2[3])

length = max(right - left, top - bottom)
print(length ** 2)