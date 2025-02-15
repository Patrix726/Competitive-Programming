class Solution:
    def getSneakyNumbers(self, nums: list[int]) -> list[int]:
        ideal = [0] * (len(nums) - 2)
        troubleMakers = []
        for num in nums:
            if ideal[num] == 1:
                troubleMakers.append(num)
            ideal[num] += 1
        return troubleMakers
