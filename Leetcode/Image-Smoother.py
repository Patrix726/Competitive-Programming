from copy import copy


class Solution:
    def imageSmoother(self, img: list[list[int]]) -> list[list[int]]:
        result = copy.deepcopy(img)
        m = len(img)
        n = len(img[0])

        for i in range(m):
            for j in range(n):

                indexes = [
                    (i, j - 1),
                    (i, j + 1),
                    (i - 1, j),
                    (i + 1, j),
                    (i + 1, j + 1),
                    (i + 1, j - 1),
                    (i - 1, j + 1),
                    (i - 1, j - 1),
                ]

                for x, y in indexes:
                    if x >= 0 and x < m and y >= 0 and y < n:
                        result[x][y] += img[i][j]

        for i in range(m):
            for j in range(n):
                hori_nums = 2 if j == 0 or j == n - 1 else 3
                ver_nums = 2 if i == 0 or i == m - 1 else 3
                if n == 1:
                    hori_nums = 1
                if m == 1:
                    ver_nums = 1
                filter_area = hori_nums * ver_nums
                result[i][j] //= filter_area

        return result
