equation = input()
result = int(equation[0]) + int(equation[4])
if result == int(equation[-1]):
    print('YES')
else:
    print('NO')