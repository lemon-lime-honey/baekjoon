money = 1000 - int(input())
answer = 0

if money >= 500:
    answer += money // 500
    money %= 500
if money >= 100:
    answer += money // 100
    money %= 100
if money >= 50:
    answer += money // 50
    money %= 50
if money >= 10:
    answer += money // 10
    money %= 10
if money >= 5:
    answer += money // 5
    money %= 5
if money >= 1:
    answer += money // 1
    money %= 1

print(answer)