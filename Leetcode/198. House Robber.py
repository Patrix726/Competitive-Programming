class Solution:
    def rob(self, nums: list[int]) -> int:
        length = len(nums)
        self.dp = [None for x in range(length)]
        self.nums = nums
        return max(self.maxStash(length - 1), self.maxStash(length - 2))

    def maxStash(self, x: int):
        if x < 0:
            return 0
        if x == 1 or x == 0:
            return self.nums[x]
        if self.dp[x] != None:
            return self.dp[x]
        self.dp[x] = self.nums[x] + max(self.maxStash(x - 2), self.maxStash(x - 3))
        return self.dp[x]


ans = Solution()

print(ans.rob([2, 7, 9, 3, 1]))
