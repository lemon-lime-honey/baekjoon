def solution(numbers):
    numbers.sort()
    ansset = set()
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if i != j:
                ansset.add(numbers[i] + numbers[j])
    answer = list(ansset)
    answer.sort()
    return answer