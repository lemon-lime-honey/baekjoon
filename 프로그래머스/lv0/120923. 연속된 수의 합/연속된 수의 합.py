def solution(num, total):
    answer = list()

    target = (2 * total // num - (num - 1)) // 2
    for i in range(target, target + num):
        answer.append(i)

    return answer