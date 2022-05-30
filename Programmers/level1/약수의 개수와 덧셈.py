def getDivisor(val):
    cnt = 0
    for i in range(1, val+1):
        if val % i == 0:
            cnt += 1

    return cnt


def solution(left, right):
    res = 0
    for val in range(left, right+1):
        nums_of_divisor = getDivisor(val)
        if nums_of_divisor % 2 == 0:
            res += val
        else:
            res -= val
    return res


print(solution(13, 17))