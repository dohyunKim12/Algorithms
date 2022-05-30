def solution(numbers, hand):
    ans_list = []
    phone = {1: [0, 0], 2: [0, 1], 3: [0, 2], 4: [1, 0], 5: [1, 1], 6: [1, 2], 7: [
        2, 0], 8: [2, 1], 9: [2, 2], '*': [3, 0], 0: [3, 1], '#': [3, 2]}
    left_h = '*'
    right_h = '#'

    for i, val in enumerate(numbers):
        if val in [1, 4, 7, '*']:
            ans_list.append('L')
            left_h = val
        elif val in [3, 6, 9, '#']:
            ans_list.append('R')
            right_h = val
        else:
            #            phone[val] 과 phone[left_h] 거리,
            #            phone[val] 과 phoen[right_h] 거리 비교
            left_dist = abs(phone[val][0] - phone[left_h][0]) + \
                abs(phone[val][1] - phone[left_h][1])
            right_dist = abs(phone[val][0] - phone[right_h][0]) + \
                abs(phone[val][1] - phone[right_h][1])
            if left_dist > right_dist:
                ans_list.append('R')
                right_h = val
            elif left_dist < right_dist:
                ans_list.append('L')
                left_h = val
            else:
                if hand == "right":
                    ans_list.append('R')
                    right_h = val
                else:
                    ans_list.append('L')
                    left_h = val

    result = (''.join(ans_list))
    return result


print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))
print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left"))
print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "right"))