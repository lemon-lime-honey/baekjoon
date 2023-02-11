string = input()
bomb = input()
stack = list()
bomb_len = len(bomb)
ref = 0

while ref < len(string):
    stack.append(string[ref])
    if stack[-1] == bomb[-1] and (''.join(stack[-1 * bomb_len:])) == bomb:
        for i in range(bomb_len):
            stack.pop()
    ref += 1

if stack:
    print(''.join(stack))
else:
    print('FRULA')