def solution(price, money, count):
    cost = price * count * (count + 1) // 2
    if money >= cost:
        return 0
    return (cost - money)