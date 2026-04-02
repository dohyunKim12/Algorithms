nums = [2, 7, 11, 15]
target = 9

map = {}

for i in range(len(nums)):
    diff = target - nums[i]
    if diff in map:
        print(sorted([map[diff], i]))
        break
    map[nums[i]] = i



    # map = {
    # 2:0,
    # 7:1,
    # 11:2,
    # 15:3
    # }

for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] + nums[j] == target:
            print(sorted([i, j]))
            break