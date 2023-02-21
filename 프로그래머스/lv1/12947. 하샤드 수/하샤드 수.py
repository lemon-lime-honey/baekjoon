def solution(x):
    temp = x
    num = 0

    while temp:
        num += temp % 10
        temp //= 10

    if x % num:
        return False
    else:
        return True