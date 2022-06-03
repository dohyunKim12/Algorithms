n = int(input())

sec_min_max = 60
count = 0 

for hr in range(n+1):
    for minuate in range(sec_min_max):
        for second in range(sec_min_max):
            # if '3' in str(hr) or '3' in str(minuate) or '3' in str(second):
            if '3' in str(hr) + str(minuate) + str(second):
                count += 1

print(count)