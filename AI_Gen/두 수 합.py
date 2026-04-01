nums = [2, 7, 11, 15]
target = 9

map = {}

for i in range(len(nums)):
    diff = target - nums[i]
    if diff in map:
        print(sorted([map[diff], i]))
        break
    map[nums[i]] = i