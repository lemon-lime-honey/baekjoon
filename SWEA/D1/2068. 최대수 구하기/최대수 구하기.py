#import sys
#sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    result = max(list(map(int, input().split())))
    print(f'#{test_case} {result}')