
class Solution:
    def maximumDifference(self, nums: list[int]) -> int:
        left = float('inf')
        right = float('-inf')
        max_diff = -1
        for num in nums:
            if num < left:
                left = num
                right = float('-inf')
            if num > right and left < num:
                right = num
                max_diff = max(max_diff, right - left)
        return max_diff
            

