def solution(l, r):
    answer = list()
    for i in range(l, r + 1):
        number = i
        chk = set()
        while number:
            chk.add(number % 10)
            number //= 10
        if not chk - {5, 0}: answer.append(i)
    return answer if answer else [-1]