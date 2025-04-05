class NumMatrix:

    def __init__(self, matrix: list[list[int]]):
        n = len(matrix)
        m = len(matrix[0])
        self.sum_matrix = [[0]*m for _ in matrix]
        for i in range(n):
            for j in range(m):
                if i==0 and j==0:
                    self.sum_matrix[i][j] = matrix[i][j]
                elif i==0:
                    self.sum_matrix[i][j] = self.sum_matrix[i][j-1] + matrix[i][j]
                elif j==0:
                    self.sum_matrix[i][j] = self.sum_matrix[i-1][j] + matrix[i][j]
                else:
                    self.sum_matrix[i][j] = self.sum_matrix[i-1][j] + self.sum_matrix[i][j-1] + matrix[i][j] - self.sum_matrix[i-1][j-1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        if row1==0 and col1==0:
            return self.sum_matrix[row2][col2]
        elif row1==0:
            return self.sum_matrix[row2][col2] - self.sum_matrix[row2][col1-1]
        elif col1==0:
            return self.sum_matrix[row2][col2] - self.sum_matrix[row1-1][col2]
        else:
            return self.sum_matrix[row2][col2] - self.sum_matrix[row1-1][col2] - self.sum_matrix[row2][col1-1] + self.sum_matrix[row1-1][col1-1]
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
