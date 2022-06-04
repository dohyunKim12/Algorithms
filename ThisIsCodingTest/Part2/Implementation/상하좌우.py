n = int(input())
plan = input().split()

# person = [1,1]

# for idx, el in enumerate(plan):
#     if(el == 'L') :
#         person[1] -= 1
#     elif(el == 'R'):
#         person[1] += 1
#     elif(el == 'U'):
#         person[0] -= 1
#     elif(el == 'D'):
#         person[0] += 1
    
#     if(person[0] == 0) :
#         person[0] = 1
#     if(person[1] == 0) :
#         person[1] = 1

# print(person)

x = 1
y = 1

dx = [0,0,-1,1]
dy = [-1,1,0,0]

move_types = ['L','R','U','D']

for el in plan:
    for idx, moveType in  enumerate(move_types):
        if el == moveType:
            new_x = x + dx[idx]
            new_y = y + dy[idx]
    if(new_x == 0 or new_y == 0 or new_x > n or new_y > n):
        continue
    x = new_x
    y = new_y

print(x,y)

