def solution(numbers):
    nums_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    ans = 0
    for val in nums_list:
        if (val not in numbers):
            ans += val

    return ans