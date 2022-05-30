def solution(n):
    maxpos = 0
    while True:
        if n < 3 ** maxpos:
            break
        maxpos += 1
    maxpos -= 1

    res = ''
    for i in range(maxpos, -1, -1):
        a, n = divmod(n, 3**i)
        res += str(a)

    res = res[::-1]

    return int(res, 3)


print(solution(45))