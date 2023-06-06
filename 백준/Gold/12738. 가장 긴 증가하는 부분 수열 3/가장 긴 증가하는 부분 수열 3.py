n = int(input())
numbers = list(map(int, input().split()))
result = [numbers[0]]

for i in range(1, n):
    if result[-1] < numbers[i]:
        result.append(numbers[i])
    else:
        lo, hi = 0, len(result) - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if result[mid] < numbers[i]:
                lo = mid + 1
            else:
                hi = mid
        
        result[hi] = numbers[i]

print(len(result))