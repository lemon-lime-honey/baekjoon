def solution(n):
    target = 1234567
    nums = [0, 1]
    
    for i in range(2, n + 1):
        nums[0], nums[1] = nums[1] % target, (nums[0] + nums[1]) % target
        
    return nums[1]