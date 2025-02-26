class Solution:
    def maxAbsoluteSum(self, nums: list[int]) -> int:
        sums = [(0, 0)] * len(nums)
        sums[0] = (nums[0], nums[0])
        minSum = nums[0]
        maxSum = nums[0]
        for i in range(1, len(nums)):
            prev = sums[i - 1]
            cur_min = min(prev[0], 0) + nums[i]
            cur_max = max(prev[1], 0) + nums[i]
            sums[i] = (cur_min, cur_max)
            minSum = min(cur_min, minSum)
            maxSum = max(cur_max, maxSum)
        return max(abs(minSum), maxSum)
