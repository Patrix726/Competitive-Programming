class Solution:
    def coloredCells(self, n: int) -> int:
        center = (n-1)*2 + 1
        total = center + sum([2*val for val in range(1,center,2)])
        return total
        