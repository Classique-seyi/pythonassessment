def pascal_rows(n):
    if n <= 0:
        return []

    triangle = []
    if n >= 1:
        triangle.append(1)
    for i in range(1, n):
        prev_row = triangle[i-1]
        current_row = [1]
        for j in range(1, i):
            above_left = prev_row[j-1]
            above_right = prev_row[j]
            current_row.append(above_left + above_right)

        current_row.append(1)
        triangle.append(current_row)
    return triangle




print(pascal_rows(5))