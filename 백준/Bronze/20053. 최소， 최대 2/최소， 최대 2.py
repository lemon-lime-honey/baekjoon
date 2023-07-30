t = int(input())

for i in range(t):
    n = int(input())
    numbers = list(map(int, input().split()))
    print(min(numbers), max(numbers))