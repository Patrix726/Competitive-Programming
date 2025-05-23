class Solution:
    def isZeroArray(self, nums: list[int], queries: list[list[int]]) -> bool:
        n = len(nums)
        diff = [0]*n

        for l,r in queries:
            diff[l] -= 1
            if r < n-1:
                diff[r+1] += 1
        prefix = 0
        for i in range(n):
            prefix += diff[i]
            nums[i] += prefix
            if nums[i] > 0:
                return False
        return True
