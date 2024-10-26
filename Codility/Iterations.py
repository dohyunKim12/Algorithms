def solution(N):
    binary = ""
    while N != 0:
        if N % 2 == 0:
            binary = "0" + binary
        else :
            binary = "1" + binary
        N = N // 2

    cnt = 0

    cntAry = []

    for digit in str(binary) :
        digit = int(digit)
        if digit == 0 :
            cnt += 1
        else :
            cntAry.append(cnt)
            cnt = 0
    maxCnt = max(cntAry)

    return maxCnt
