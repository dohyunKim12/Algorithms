def solution(s):
    answer = []
    cnt_a = 0
    cnt_b = 0

    while (True):
        if (s == "1") : break
        length = 0
        for idx, el in enumerate(s):
            if (el == '0'):
                cnt_b += 1
            else: length += 1
            
        
        cnt_a += 1
        s = bin(length)[2:]

    
    return [cnt_a, cnt_b]

# print(solution("110010101001"))
print(solution("01110"))