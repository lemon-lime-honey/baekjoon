def solution(arr, k):
    answer = list()
    num_set = set()
    for num in arr:
        if num not in num_set:
            answer.append(num)
            num_set.add(num)
    if len(answer) < k: answer.extend([-1 for i in range(k - len(answer))])
    return answer[:k]