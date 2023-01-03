import sys

s = set()
n = int(sys.stdin.readline())

for i in range(n):
    command = list(map(str, sys.stdin.readline().strip().split()))
    if (len(command) == 2):
        command[1] = int(command[1])
    if command[0] == "add":
        s.add(command[1])
    elif command[0] == "remove":
        s.discard(command[1])
    elif command[0] == "check":
        if command[1] in s:
            print(1)
        else:
            print(0)
    elif command[0] == "toggle":
        if command[1] in s:
            s.remove(command[1])
        else:
            s.add(command[1])
    elif command[0] == "all":
        s = {x for x in range(1, 21)}
    elif command[0] == "empty":
        s = set()