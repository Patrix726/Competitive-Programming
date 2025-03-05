class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        output = []
        for num in nums:
            count = 0
            for num2 in nums:
                if num2 < num:
                    count += 1
            output.append(count)
        return output
