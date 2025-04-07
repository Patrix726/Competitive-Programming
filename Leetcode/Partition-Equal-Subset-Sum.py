class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        total = sum(nums)
        if total % 2!=0:
            return False
        targetSum = total//2
        dp = [False]* (targetSum+1)
        dp[0] = True
        for num in nums:
            for curSum in range(targetSum, num-1, -1):
                dp[curSum] = dp[curSum] or dp[curSum-num]
        return dp[targetSum]
