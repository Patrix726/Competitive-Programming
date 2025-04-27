class Solution:
    def countSubarrays(self, nums: list[int]) -> int:
        left = 0
        right = 2
        n = len(nums)
        count = 0
        while right < n:
            if (nums[right] + nums[left])*2 == nums[left+1]:
                count+=1
            left+=1
            right+=1
        return count
