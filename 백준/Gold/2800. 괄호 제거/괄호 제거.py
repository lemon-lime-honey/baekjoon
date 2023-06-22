from itertools import combinations

ipt = input()
brackets = list()
result = set()
stack = list()

for index, letter in enumerate(ipt):
    if letter == '(':
        stack.append(index)
    elif letter == ')':
        idx = stack.pop()
        brackets.append((idx, index))

bracket_comb = list()

for i in range(1, len(brackets) + 1):
    bracket_comb = combinations(brackets, i)

    for bracket_set in bracket_comb:
        temp = list(ipt)
        for index in bracket_set:
            temp[index[0]] = ''
            temp[index[1]] = ''
        result.add(''.join(temp))

res = sorted(list(result))

print(*res, sep='\n')