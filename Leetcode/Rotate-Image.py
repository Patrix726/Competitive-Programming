class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row = len(matrix)
        col = len(matrix[0])
        for i in range(row):
            for j in range(i, col):
                matrix[i][j], matrix[j][i] = (matrix[j][i], matrix[i][j])
        print(matrix)
        for i in range(row):
            for j in range(col // 2):
                left_x, left_y = (i, j)
                right_x, right_y = (i, col - 1 - j)
                matrix[left_x][left_y], matrix[right_x][right_y] = (
                    matrix[right_x][right_y],
                    matrix[left_x][left_y],
                )
