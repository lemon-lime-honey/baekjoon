result = None

for i in range(15):
    ipt = input().split()
    if result: continue
    for j in range(15):
        if ipt[j] == 'w':
            result = 'chunbae'
        elif ipt[j] == 'b':
            result = 'nabi'
        elif ipt[j] == 'g':
            result = 'yeongcheol'

print(result)
