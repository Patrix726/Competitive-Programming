class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zero_rows = set()
        zero_cols = set()
        m = len(matrix)
        n = len(matrix[0])
        for row in range(m):
            for col in range(n):
                if matrix[row][col] == 0:
                    zero_rows.add(row)
                    zero_cols.add(col)
        for row in range(m):
            for col in range(n):
                if row in zero_rows or col in zero_cols:
                    matrix[row][col] = 0
        
