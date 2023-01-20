score = 0

for i in range(1, 4):
    score += i * int(input())

if score >= 10:
    print('happy')
else:
    print('sad')