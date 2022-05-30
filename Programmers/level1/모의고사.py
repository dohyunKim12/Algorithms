def solution(answers):
    length = len(answers)
    l = []
    sum1 = 0 
    sum2 = 0
    sum3 = 0

    supoza1 = [1,2,3,4,5]
    supoza2 = [2,1,2,3,2,4,2,5]
    supoza3 = [3,3,1,1,2,2,4,4,5,5]

    supoza1 = supoza1 * (length//5 + 1)
    supoza2 = supoza2 * (length//8 + 1)
    supoza3 = supoza3 * (length//10 + 1)

    for i in range(len(answers)):
        if supoza1[i] == answers[i]:
            sum1 += 1
        if supoza2[i] == answers[i]:
            sum2 += 1
        if supoza3[i] == answers[i]:
            sum3 += 1
    
    dic = {
        1: sum1,
        2: sum2,
        3: sum3
    }

    maximum = max(sum1, sum2, sum3) 

    if dic.get(1) >= maximum:
        l.append(1)
    if dic.get(2) >= maximum:
        l.append(2)
    if dic.get(3) >= maximum:
        l.append(3)

    return l