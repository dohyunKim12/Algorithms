def solution(numbers):

    l = list()

    for i in range(len(numbers)):
        for j in range(i+1,len(numbers)):
            l.append(numbers[i] + numbers[j])

    l = set(l)
    l = list(l)
    l.sort()

    return l