def solution(numbers):
    numbers = list(map(str, numbers))
    stack = []
    tmp = []
    for number in numbers:
        tmp.append([(number*4)[:4], number])

    tmp.sort(reverse=True)
    for i in tmp:
        stack.append(i.pop())
    stack = ''.join(stack)
    return str(0) if not int(stack) else stack