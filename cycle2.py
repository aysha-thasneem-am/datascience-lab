import numpy as np 

def create_matrix():
    rows = int(input("Enter no of rows: "))
    cols = int(input("Enter no of cols: "))
    matrix = np.empty((rows,cols), dtype=float)
    print("Enter the matrix elements row by row: ")
    for i in range(rows):
        row_data = input(f"Enter values for row {i + 1} seperated by spaces: ").split()
        matrix[i, :] = [float(x) for x in row_data]
    return matrix


m1 = create_matrix()
m2 = create_matrix()

print("Dot product: \n", m1 @ m2)

print("Transpose of 1st matrix:\n", m1.T)
print()
print("Transpose of 2nd matrix:\n", m2.T)

print("Trace of 1st matrix:\n", np.trace(m1))
print()
print("Trace of 2nd matrix:\n", np.trace(m2))

print("Rank of 1st matrix:\n", np.linalg.matrix_rank(m1))
print()
print("Rank of 2nd matrix:\n", np.linalg.matrix_rank(m2))

print("Determinant of 1st matrix:\n", np.linalg.det(m1))
print()
print("Determinant of 2nd matrix:\n", np.linalg.det(m2))

print("Inverse of 1st matrix:\n", np.linalg.inv(m1))
print()
print("Inverse of 2nd matrix:\n", np.linalg.inv(m2))

print("Eigen of 1st matrix:\n", np.linalg.eig(m1))
print()
print("Eigen of 2nd matrix:\n", np.linalg.eig(m2))