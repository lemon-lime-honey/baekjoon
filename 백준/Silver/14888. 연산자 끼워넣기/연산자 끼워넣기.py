from itertools import permutations

n = int(input())
numbers = list(map(int, input().split()))
operator_nums = list(map(int, input().split()))
op_dict = {0: '+', 1: '-', 2: '*', 3: '//'}
max_res, min_res = -1 * int(1e10), int(1e10)
operators = list()

for i in range(4):
    for j in range(operator_nums[i]):
        operators.append(op_dict[i])

operator_perm = permutations(operators, n - 1)

for operator_set in operator_perm:
    temp = 0
    operator = ''
    for i in range(n):
        if operator == '-':
            temp -= numbers[i]
        elif operator == '*':
            temp *= numbers[i]
        elif operator == '//':
            if temp < 0:
                temp = -1 * (-1 * temp // numbers[i])
            else:
                temp //= numbers[i]
        else:
            temp += numbers[i]
        if i != n - 1:
            operator = operator_set[i]
    max_res = max(max_res, temp)
    min_res = min(min_res, temp)

print(max_res, min_res, sep='\n')