t = int(input())

for i in range(t):
    nums = list(map(int, input().split()))
    hp = nums[0] + nums[4]
    mp = nums[1] + nums[5]
    attack = nums[2] + nums[6]
    defense = nums[3] + nums[7]
    
    if hp < 1:
        hp = 1
    if mp < 1:
        mp = 1
    if attack < 0:
        attack = 0

    print(hp + 5 * mp + 2 * attack + 2 * defense)
