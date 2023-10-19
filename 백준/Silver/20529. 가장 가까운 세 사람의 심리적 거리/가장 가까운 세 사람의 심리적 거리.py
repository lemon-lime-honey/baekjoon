from itertools import combinations
import sys
input = sys.stdin.readline

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        types = input().rstrip().split()
        if n > 32:
            print(0)
        else:
            type_comb = combinations(types, 3)
            result = 16

            for type_set in type_comb:
                chk = 0
                for i in range(4):
                    for j in range(-1, 2):
                        if type_set[j][i] != type_set[j + 1][i]: chk += 1
                result = min(result, chk)

            print(result)