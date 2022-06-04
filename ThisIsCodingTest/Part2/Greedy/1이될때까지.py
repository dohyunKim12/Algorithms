n, k = map(int, input().split())

# count = 0
# while(True):
#     if(n % k == 0):  # operation #2.
#         n /= k
#     else:
#         n -= 1  # operation #1.
#     count += 1

#     if n == 1:
#         break

# print(count)

res = 0
while True:
    target = (n // k) * k
    res += n - target
    n = target

    if n < k:
        break
    res += 1
    n //= k

res += (n-1)
print(res)
