class Solution:
    def transpose(self, matrix: list[list[int]]) -> list[list[int]]:
        row = len(matrix)
        col = len(matrix[0])

        ans = [[0] * row for _ in range(col)]

        for i in range(row):
            for j in range(col):
                ans[j][i] = matrix[i][j]
        return ans
