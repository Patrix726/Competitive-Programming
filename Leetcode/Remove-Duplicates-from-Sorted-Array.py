class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        unique = len(nums)
        offset = 0
        i = 1
        while i < len(nums):
            if nums[i]==nums[i-1-offset]:
                unique-=1
                offset+=1
            elif offset > 0:
                nums[i-offset] = nums[i]
            i+=1
        return unique

