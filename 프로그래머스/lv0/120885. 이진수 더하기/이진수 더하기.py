def solution(bin1, bin2):
    total = bin(int(bin1, 2) + int(bin2, 2))
    return total[2:]    