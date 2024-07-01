ax, ay, bx, by, cx, cy = map(int, input().split())

if (by - ay) * (cx - bx) == (cy - by) * (bx - ax): print(-1.0)
else:
    lines = [((by - ay) ** 2 + (bx - ax) ** 2) ** 0.5, 
             ((cy - ay) ** 2 + (cx - ax) ** 2) ** 0.5,
             ((cy - by) ** 2 + (cx - bx) ** 2) ** 0.5]
    lines.sort()
    print((lines[-1] - lines[0]) * 2)
