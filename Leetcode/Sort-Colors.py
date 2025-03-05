class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = [0] * 3
        for num in nums:
            count[num] += 1
        target = 0
        for index, value in enumerate(count):
            for i in range(value):
                nums[target] = index
                target += 1
