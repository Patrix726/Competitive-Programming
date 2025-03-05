class Solution:
    def maxCoins(self, piles: list[int]) -> int:
        piles.sort()
        n = len(piles)
        left, mid, last = 0, n - 2, n - 1
        total = 0
        while left < mid:
            total += piles[mid]
            left += 1
            mid -= 2
            last -= 2
        return total
