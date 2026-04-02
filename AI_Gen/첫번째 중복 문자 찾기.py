s = "abcdb"
# return "b"

map = {}

for i in s:
    if i in map:
        map[i] += 1
    else :
        map[i] = 1
    if map[i] == 2:
        print(i)
        break

