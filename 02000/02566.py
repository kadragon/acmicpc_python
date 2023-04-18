import sys

max_value = -1
max_index_row = 0
max_index_col = 0

for row_index in range(9):
    line = sys.stdin.readline().strip()
    data = list(map(int, line.split()))

    for col_index, value in enumerate(data):
        if value > max_value:
            max_value = value
            max_index_row = row_index+1
            max_index_col = col_index+1

print(f'{max_value}\n{max_index_row} {max_index_col}')
