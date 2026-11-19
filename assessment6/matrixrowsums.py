
matrix = [[2, 4, 6], [1, 3, 5], [10, 20, 30]]

for index, row in enumerate(matrix,1):
    total_row = 0
    average = 0
    for num in row:
        total_row += num
    average = total_row / len(row)
    print(f"Row {index} total: {total_row} | Row {index} average: {average}")

for i in range(len(matrix[0])):
    total_col = 0
    for j in range(len(matrix)):
        total_col += matrix[j][i]
    print(f"Column {index} total: {total_col}")


# matrix = [[2, 4, 6], [1, 3, 5], [10, 20, 30]]

# col_sum = [0] * len(matrix[0])
# for index, row in enumerate(matrix, 1):
#     row_sum = 0
#     average = 0
   
#     for i, num in enumerate(row):
#         row_sum += num
#         col_sum[i] += num
#         average = row_sum / len(row)
#     print(f"Row {index} total: {row_sum} | Row {index} average: {average} Column {index} total: {col_sum}")



