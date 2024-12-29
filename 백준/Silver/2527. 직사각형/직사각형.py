for i in range(4):
    lx1, ly1, rx1, ry1, lx2, ly2, rx2, ry2 = map(int, input().split())

    if rx2 < lx1 or ry2 < ly1 or rx1 < lx2 or ry1 < ly2:
        print("d")
        continue

    if ((lx1 == rx2 and ly1 == ry2) or
        (lx1 == rx2 and ly2 == ry1) or
        (lx2 == rx1 and ly2 == ry1) or
        (lx2 == rx1 and ly1 == ry2)):
        print("c")
        continue

    if rx1 == lx2 or rx2 == lx1 or ry1 == ly2 or ry2 == ly1:
        print("b")
        continue

    print("a")
