def solution(nums):
    l = []
    upper_bound = len(nums)//2
    for val in nums:
        if val not in l:
            l.append(val)

    return min(len(l), upper_bound)