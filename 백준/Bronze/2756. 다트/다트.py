t = int(input())

for i in range(t):
    nums = list(map(float, input().split()))
    result = [0, 0, 0]

    for j in range(0, 12, 2):
        if j < 6:
            target = 1
        else:
            target = 2

        dist = nums[j] ** 2 + nums[j + 1] ** 2

        if dist <= 3**2:
            result[target] += 100
        elif dist <= 6**2:
            result[target] += 80
        elif dist <= 9**2:
            result[target] += 60
        elif dist <= 12**2:
            result[target] += 40
        elif dist <= 15**2:
            result[target] += 20

    if result[1] < result[2]:
        print(f"SCORE: {result[1]} to {result[2]}, PLAYER 2 WINS.")
    elif result[1] > result[2]:
        print(f"SCORE: {result[1]} to {result[2]}, PLAYER 1 WINS.")
    else:
        print(f"SCORE: {result[1]} to {result[2]}, TIE.")
