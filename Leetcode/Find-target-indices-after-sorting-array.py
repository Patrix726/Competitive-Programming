class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        oth_count = 0
        target_count = nums.count(target)

        for num in nums:
            oth_count += 1 if num < target else 0

        return [oth_count + ind for ind in range(target_count)]
