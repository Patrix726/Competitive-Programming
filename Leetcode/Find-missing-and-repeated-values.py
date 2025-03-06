from collections import Counter


class Solution:
    def findMissingAndRepeatedValues(self, grid: list[list[int]]) -> list[int]:
        flat_grid = []
        n = len(grid)
        for lane in grid:
            flat_grid += lane
        count = Counter(flat_grid)
        repeated = count.most_common(1)[0][0]
        missing = [num for num in range(1, n * n + 1) if num not in count][0]
        return [repeated, missing]
