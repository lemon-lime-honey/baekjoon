def chk(n, charge):
    dist = 0
    for i in range(n):
        if dist < charge[i]:
            return False
        dist = charge[i] + 200

    dist = 1422 - (dist - 1422)

    for i in range(n - 1, -1, -1):
        if dist > charge[i]:
            return False
        dist = charge[i] - 200

    return True


while True:
    n = int(input())

    if n == 0:
        break

    charge = sorted([int(input()) for i in range(n)])
    if chk(n, charge):
        print("POSSIBLE")
    else:
        print("IMPOSSIBLE")
