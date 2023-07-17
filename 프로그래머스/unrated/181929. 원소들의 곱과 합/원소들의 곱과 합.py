def solution(num_list):
    mul = 1
    square = 0

    for num in num_list:
        mul *= num
        square += num

    return 1 if mul < square ** 2 else 0