class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        s = ""
        for row in self.matrix:
            s += ("   ".join(map(str, row))) + "\n"
        return s

    def __add__(self, other):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                self.matrix[i][j] = self.matrix[i][j] + other.matrix[i][j]
        return Matrix(self.matrix)


matrix_1 = Matrix([[1, 2], [3, 4], [5, 6]])
matrix_2 = Matrix([[7, 8], [9, 10], [11, 12]])

print(matrix_1)
print(matrix_2)
print(matrix_1 + matrix_2)

