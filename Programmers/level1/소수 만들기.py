def solution(nums):
    num_of_prime = 0
    for i in range(0, len(nums)-2):
        for j in range(i+1, len(nums)-1):
            for k in range(j+1, len(nums)):                   # 세가지 무작위 숫자를 i,j,k로 설정
                isPrime = True
                number = nums[i]+nums[j]+nums[k]
                for x in range(2, number):                  # 소수인지 판별
                    if number % x == 0 : isPrime = False    # 0으로 나누어 떨어지면, 소수가 아님.
                if isPrime:
                    num_of_prime += 1
    
    return num_of_prime