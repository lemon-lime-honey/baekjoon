import sys
input = sys.stdin.readline

command = list()
result = list()

while True:
    ipt = input().rstrip()
    if ipt == 'QUIT':
        break

    if ipt.isdigit():
        for i in range(int(ipt)):
            stack = [int(input())]
            try:
                for cmd in command:
                    if cmd[0] == 'NUM':
                        stack.append(int(cmd[1]))
                    elif cmd[0] == 'POP':
                        stack.pop()
                    elif cmd[0] == 'INV':
                        stack[-1] *= -1
                    elif cmd[0] == 'DUP':
                        stack.append(stack[-1])
                    elif cmd[0] == 'SWP':
                        first, second = stack.pop(), stack.pop()
                        stack.append(first)
                        stack.append(second)
                    elif cmd[0] == 'ADD':
                        stack.append(stack.pop() + stack.pop())
                    elif cmd[0] == 'SUB':
                        stack.append(-stack.pop() + stack.pop())
                    elif cmd[0] == 'MUL':
                        stack.append(stack.pop() * stack.pop())
                    elif cmd[0] == 'DIV':
                        first, second = stack.pop(), stack.pop()
                        temp = abs(second) // abs(first)
                        if first * second < 0:
                            stack.append(-temp)
                        else:
                            stack.append(temp)
                    elif cmd[0] == 'MOD':
                        first, second = stack.pop(), stack.pop()
                        temp = abs(second) % abs(first)
                        if second < 0:
                            stack.append(-temp)
                        else:
                            stack.append(temp)
                if len(stack) != 1 or abs(stack[0]) > int(1e9):
                    result.append('ERROR')
                else:
                    result.append(str(stack[0]))
            except:
                result.append('ERROR')
        result.append('')
    elif ipt:
        cmd = ipt.split()
        if cmd[0] == 'END':
            continue
        command = [(ipt.split())]
        while True:
            cmd = input().rstrip().split()
            if cmd[0] == 'END':
                break
            command.append(tuple(cmd))

print(*result, sep='\n')
