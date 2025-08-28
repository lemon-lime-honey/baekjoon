t = int(input())

g_score = [1, 2, 3, 3, 4, 10]
s_score = [1, 2, 2, 2, 3, 5, 10]

for i in range(1, t + 1):
    g = list(map(int, input().split()))
    s = list(map(int, input().split()))

    g_result, s_result = 0, 0

    for j, k in zip(g_score, g):
        g_result += j * k

    for j, k in zip(s_score, s):
        s_result += j * k

    if g_result > s_result:
        print(f"Battle {i}: Good triumphs over Evil")
    elif g_result == s_result:
        print(f"Battle {i}: No victor on this battle field")
    else:
        print(f"Battle {i}: Evil eradicates all trace of Good")
