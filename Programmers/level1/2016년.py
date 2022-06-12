def solution(a, b):
    days = ['THU','FRI','SAT','SUN','MON','TUE','WED']
    dates = [0,31,29,31,30,31,30,31,31,30,31,30,31]
    for i in range(a):
        b += dates[i]
    ans = b%7
    return days[ans]

print(solution(5, 24))