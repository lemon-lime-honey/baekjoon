t = int(input())

for i in range(t):
    transmission = list(map(str, input().split()))
    if transmission[0] == transmission[1]:
        print('OK')
    else:
        print('ERROR')