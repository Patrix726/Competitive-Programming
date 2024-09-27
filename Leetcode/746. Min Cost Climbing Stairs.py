class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        self.cost = cost
        length = len(cost)
        self.dp = [None for x in range(length)]
        return min(self.minCost(length - 1), self.minCost(length - 2))

    def minCost(self, x: int):
        if x == 1 or x == 0:
            return self.cost[x]
        if self.dp[x] != None:
            return self.dp[x]
        self.dp[x] = self.cost[x] + min(self.minCost(x - 1), self.minCost(x - 2))
        return self.dp[x]


ans = Solution()
print(ans.minCostClimbingStairs([2, 2, 1, 0]))
