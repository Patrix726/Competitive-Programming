
class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        min_length = len(nums) + 1
        left = 0
        right = 0
        cur_sum = 0
        while right < len(nums):
            cur_sum +=nums[right]
            right+=1
            while cur_sum >=target:
                min_length = min(min_length,right-left)
                cur_sum-=nums[left]
                left+=1
        return min_length % (len(nums)+1)
