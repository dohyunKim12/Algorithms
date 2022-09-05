import collections

def solution(queue1, queue2):
    queue1 = collections.deque(queue1)
    queue2 = collections.deque(queue2)
    queue_len = len(queue1)
    cnt = 0
    
    sum_1 = sum(queue1)
    sum_2 = sum(queue2)

    if((sum_1 + sum_2) %2 != 0): return -1
    while(sum_1 != sum_2 and (cnt < queue_len * 3)):
        if (sum_1 > sum_2):
            el = queue1.popleft()
            queue2.append(el)
            sum_1 -= el
            sum_2 += el
        else :
            el = queue2.popleft()
            queue1.append(el)
            sum_1 += el
            sum_2 -= el
        cnt += 1
    if(sum_1 == sum_2):
        return cnt
    return -1
    
# solution([3,2,7,2], [4,6,5,1])
print(solution([1,1,1,1,1],[1,1,1,9,1]))