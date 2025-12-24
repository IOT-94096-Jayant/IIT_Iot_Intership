matrix1 = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]
matrix2 = (
    (12, 11, 10, 9),
    (8, 7, 6, 5),
    (4, 3, 2, 1)
)
def add_sub_matrices(m1, m2):
    add_result = []
    sub_result = []
    for i in range(len(m1)):    
        add_row = []
        sub_row = []
        for j in range(len(m1[0])):   # columns
            add_row.append(m1[i][j] + m2[i][j])
            sub_row.append(m1[i][j] - m2[i][j])
        add_result.append(add_row)
        sub_result.append(sub_row)
    return add_result, sub_result
addition, subtraction = add_sub_matrices(matrix1, matrix2)
print("Matrix Addition Result:")
for row in addition:
    print(row)
print("\nMatrix Subtraction Result:")
for row in subtraction:
    print(row)