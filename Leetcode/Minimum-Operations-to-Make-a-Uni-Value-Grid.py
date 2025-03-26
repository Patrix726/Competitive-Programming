class Solution:
    def minOperations(self, grid: list[list[int]], x: int) -> int:
        n = len(grid)
        m = len(grid[0])
        combined = [grid[i][j] for i in range(n) for j in range(m)]
        combined.sort()
        mod= combined[0] % x
        target = combined[((len(combined)-1)//2)]
        print(target)
        count = 0
        for num in combined:
            if num % x != mod:
                return -1
            count+= abs(target-num)//x
        return count
        
