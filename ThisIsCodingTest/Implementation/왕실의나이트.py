[col_str, row_str] = list(input())

col = ord(col_str) - ord('a') + 1
row = int(row_str)

cases = [[-1, -2], [1, -2], [2, -1], [2, 1],
         [1, 2], [-1, 2], [-2, 1], [-2, -1]]

count = 0

for case in cases:
    new_col = col + case[0]
    new_row = row + case[1]

    if new_col > 0 and new_row > 0 and new_col < 9 and new_row < 9:
        count += 1

print(count)
