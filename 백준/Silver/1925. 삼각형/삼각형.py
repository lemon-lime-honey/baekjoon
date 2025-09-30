def ccw():
    target = (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])
    if target == 0:
        return True
    return False


def calc():
    if ccw():
        return "X"

    length = [
        (b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2,
        (c[0] - b[0]) ** 2 + (c[1] - b[1]) ** 2,
        (a[0] - c[0]) ** 2 + (a[1] - c[1]) ** 2,
    ]

    length.sort()

    if length[0] == length[1] == length[2]:
        return "JungTriangle"

    if length[0] + length[1] == length[2]:
        if length[0] == length[1]:
            return "Jikkak2Triangle"
        return "JikkakTriangle"

    if length[0] + length[1] < length[2]:
        if length[0] == length[1]:
            return "Dunkak2Triangle"
        return "DunkakTriangle"

    if length[0] == length[1] or length[1] == length[2]:
        return "Yeahkak2Triangle"

    return "YeahkakTriangle"


a = tuple(map(int, input().split()))
b = tuple(map(int, input().split()))
c = tuple(map(int, input().split()))

print(calc())
