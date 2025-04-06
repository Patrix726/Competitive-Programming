
class Solution:
    def largestDivisibleSubset(self, nums: list[int]) -> list[int]:
        nums.sort()
        n = len(nums)
        dp = [1]*n
        prev = [-1]*n
        maxi = 0
        for i in range(1,n):
            for j in range(i):
                if nums[i]%nums[j]==0 and dp[j]+1 > dp[i]:
                    dp[i]= dp[j]+1
                    prev[i] = j
            maxi = i if dp[maxi] < dp[i] else maxi
        output = []
        while maxi >=0:
            output.append(nums[maxi])
            maxi = prev[maxi]
        output.reverse()
        return output
