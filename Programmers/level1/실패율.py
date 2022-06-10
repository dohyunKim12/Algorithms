def solution(n, stages):
    # Definite failure to dictionary
    failure = {}
    for i in range(1,n+1):
        left_val, right_val = 0, 0
        for j in stages:
            if j >= i:
                right_val += 1
            if j == i:
                left_val += 1
        if right_val == 0:
            failure[i] = 0
        else:
            failure[i] = left_val / right_val

    # Sort failure by values
    failure = sorted(failure.items(), key = lambda item:item[1], reverse=True)

    print(failure)
    # Return sorted keys in failure (stages)
    return list(map((lambda l:l[0]),failure))

# n = int(input())
# stages = list(map(int,input()))
# print(solution(5, [2,1,2,6,2,4,3,3]))
# print(solution(4, [4,4,4,4,4]))
print(solution(5,[2,2,2,2,2]))