
class Solution:
    def triangleType(self, nums: list[int]) -> str:
        temp = set(nums)
        total = sum(nums)
        if len(temp) == 1:
            return "equilateral"
        for num in nums:
            if total - num <= num:
                return "none"
        return "isosceles" if len(temp) == 2 else "scalene"
