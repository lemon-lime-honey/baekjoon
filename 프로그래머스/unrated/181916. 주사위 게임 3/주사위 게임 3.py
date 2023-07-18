from collections import Counter

def solution(a, b, c, d):
    numbers = Counter([a, b, c, d]).most_common()
    if len(numbers) == 1:
        return 1111 * numbers[0][0]
    elif len(numbers) == 2:
        if numbers[0][1] == 3:
            return (10 * numbers[0][0] + numbers[1][0]) ** 2
        else:
            return (numbers[0][0] + numbers[1][0]) * abs(numbers[0][0] - numbers[1][0])
    elif len(numbers) == 3:
            return numbers[1][0] * numbers[2][0]
    else:
        return min(a, b, c, d)