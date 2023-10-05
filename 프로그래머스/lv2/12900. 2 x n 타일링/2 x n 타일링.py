def solution(n):
    one, two = 1, 2

    for i in range(3, n + 1):
        temp = one + two
        one, two = two, temp

    return two % 1000000007