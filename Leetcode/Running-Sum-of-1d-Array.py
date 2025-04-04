class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        total = 0
        output = []
        for num in nums:
            total+=num
            output.append(total)
        return output
