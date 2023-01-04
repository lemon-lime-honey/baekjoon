from collections import Counter

day = int(input())
car = Counter(map(int, input().split()))

print(car[day])