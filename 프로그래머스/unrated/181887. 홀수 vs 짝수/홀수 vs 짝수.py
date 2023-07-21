def solution(num_list):
    odd, even = 0, 0
    for index, number in enumerate(num_list):
        if index % 2:
            even += number
        else:
            odd += number
    return max(even, odd)