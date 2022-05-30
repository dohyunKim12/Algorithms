def solution(n, lost, reserve):
    lost = list(set(lost) - set(reserve))
    reserve = list(set(reserve) - set(lost))

    cnt = n - len(lost)

    for value in lost:
        if (value-1) in reserve or (value+1) in reserve:
            reserve.pop(0)
            cnt += 1

    return cnt