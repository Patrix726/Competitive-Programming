
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        n = len(prices)
        max_profit = 0
        max_val = 0
        for i in range(n-1,-1,-1):
            max_val = max(prices[i],max_val)
            max_profit = max(max_profit, max_val - prices[i])
        return max_profit
        

