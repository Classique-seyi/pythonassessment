matrix = [[2, 4, 6], [1, 3, 5], [10, 20, 30]]


for i, rows in enumerate(matrix, start = 1):
    total = 0
    for number in rows:
        total += number
    print(f"Row {i} total: {total}")