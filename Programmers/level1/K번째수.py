def solution(array, commands):
    ans = []
    length= len(commands)

    for i in range(length):
        new_array = []
        start_index = commands[i][0]
        end_index = commands[i][1]
        extract_index = commands[i][2]
        new_array = array[start_index-1:end_index]
        new_array.sort()
        ans.append(new_array[extract_index-1])
    return ans