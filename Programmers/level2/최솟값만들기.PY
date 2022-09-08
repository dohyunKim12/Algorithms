def solution(A,B):
    acc = 0
    A = sorted(A)
    B = sorted(B, reverse = True)

    for i in range(len(A)):
        acc += A[i] * B[i]
    return acc

print(solution([1,4,2],[5,4,4]))