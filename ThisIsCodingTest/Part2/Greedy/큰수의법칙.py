n, m, k = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()

max_first = arr[-1]
max_second = arr[-2]

print(max_first, max_second)

res = 0

count = (m//(k+1)) * k
count += m % (k + 1)
print(count)
