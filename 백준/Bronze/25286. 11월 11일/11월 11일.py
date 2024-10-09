import sys
from calendar import isleap

input = sys.stdin.readline

t = int(input())

for i in range(t):
    year, month = map(int, input().split())
    match month:
        case 1:
            print(year - 1, 12, 31)
        case 2 | 4 | 6 | 8 | 9 | 11:
            print(year, month - 1, 31)
        case 3:
            if isleap(year):
                print(year, month - 1, 29)
            else:
                print(year, month - 1, 28)
        case 5 | 7 | 10 | 12:
            print(year, month - 1, 30)
