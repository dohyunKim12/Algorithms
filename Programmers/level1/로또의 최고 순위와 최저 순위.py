def solution(lottos, win_nums):
    ans = []
    cnt = 0
    minimum = 6
    num_zero = 0

    for val in lottos:
        if not val :
            num_zero += 1
        if val in win_nums:
            cnt += 1
    minimum = 7-cnt
    if (minimum == 7): minimum = 6

    maximum = minimum - num_zero 

    ans.append(max(1,maximum))
    ans.append(minimum)

    return ans