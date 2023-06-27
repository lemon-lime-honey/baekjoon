def sub(numbers, target, total, turn):
    global answer
    if turn == len(numbers) and total == target:
        answer += 1
        return True
    elif turn == len(numbers):
        return False

    total += numbers[turn]
    sub(numbers, target, total, turn + 1)
    total -= 2 * numbers[turn]
    sub(numbers, target, total, turn + 1)
    total += numbers[turn]


def solution(numbers, target):
    global answer
    answer = 0
    sub(numbers, target, 0, 0)
    return answer