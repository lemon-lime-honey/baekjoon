import sys

file_type = dict()
n = int(sys.stdin.readline())

for i in range(n):
    file = sys.stdin.readline().strip().split('.')
    if file[1] not in file_type:
        file_type[file[1]] = 1
    else:
        file_type[file[1]] += 1

result = sorted(file_type.items(), key = lambda x: x[0])

for element in result:
    print(*element)