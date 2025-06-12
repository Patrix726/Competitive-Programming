
class Solution:
    def maxAdjacentDistance(self, nums: list[int]) -> int:
        n = len(nums)
        nums += [nums[0]]
        max_val = float('-inf')
        for i in range(n):
            max_val = max(max_val, abs(nums[i]-nums[i+1]))
        return max_val
