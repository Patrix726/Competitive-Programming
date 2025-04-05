
class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        if len(nums)==1:
            return nums[0]
        total = 0
        min_amt = 0
        max_amt = float('-inf')
        for num in nums:
            total+=num
            max_amt = max(max_amt,total-min_amt)
            min_amt = min(min_amt, total)
        return int(max_amt)
