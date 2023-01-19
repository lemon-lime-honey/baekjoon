from statistics import mean
from collections import Counter

n = int(input())

try:
    log = list(map(int, input().split()))
    counter_log = Counter(log)
    avg = mean(log)
    exp = 0
    for item in counter_log.keys():
        exp += item * (counter_log[item] / len(log))
    result = avg / exp
    print(f'{result:.2f}')
except:
    print('divide by zero')