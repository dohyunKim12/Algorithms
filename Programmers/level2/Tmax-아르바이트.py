from sre_parse import parse_template


def solution(part_times):
    # 그리디 알고리즘
    # 아르바이트 별 얻을 수 있는 수익을 계산하여 ((E - S) * C) part_times 배열 각 원소의 끝에 추가한다.
    for job in part_times:
        job.append((job[1]-job[0]) * job[2])

    # 얻을 수 있는 수익이 높은 순서대로 정렬
    part_times.sort(key=lambda x: x[3], reverse=True)

    # 일 할 수 있는 날짜를 1부터 100까지 리스트로 생성하고 내림차순 정렬된 part_times 배열에서 순차적으로 겹치지 않는 아르바이트만 res 배열에 추가.
    avail_days = list(range(1, 101))
    res = []
    for job in part_times:
        for i in range(job[0], job[1]):
            if i not in avail_days:
                break
            avail_days.remove(i)
            if i == job[1]-1:
                res.append(job)

    # 가장 많은 이익을 얻을 수 있도록 정리된 아르바이트 배열에서 금액들만 더하여 Return
    return sum(list(map(lambda x: x[3], res)))


part_times = [
    [1, 5, 1000],
    [4, 10, 400],
    [8, 50, 200],
    [5, 8, 900],
    [30, 80, 100]
]

print(solution(part_times))
