def solution(A, K):
    length = len(A)

    K = K % length

    return A[-K:] + A[:-K]