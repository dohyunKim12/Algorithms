def recursive_combinations(n, m, start=0, depth=0, combination=[]):
    if depth == m:
        print("".join(map(str, combination)))  # 숫자를 이어붙여 출력
        return

    for i in range(start, n):
        recursive_combinations(n, m, i + 1, depth + 1, combination + [i])

# 사용 예시
n = 6  # 범위 (0부터 n-1까지 숫자)
m = 3  # 원하는 숫자 조합의 길이
recursive_combinations(n, m)