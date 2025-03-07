class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        threeMax = []
        for num in set(nums):
            if len(threeMax)<3:
                threeMax.append(num)
            elif num > threeMax[0]:
                threeMax[0] = num
            threeMax.sort()
        return threeMax[0] if len(threeMax) ==3 else threeMax[-1]
