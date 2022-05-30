def solution(d, budget):
    d = sorted(d)
    res = 0

    for val in d:
        budget = budget - val
        if budget < 0:
            break
        else:
            res += 1

    return res


print(solution([1, 3, 2, 5, 4], 9))
print(solution([2, 2, 3, 3], 10))