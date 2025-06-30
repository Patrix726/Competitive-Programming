
class Solution:
    def maxSubsequence(self, nums: list[int], k: int) -> list[int]:
        sorted_nums = sorted(enumerate(nums),key=lambda x: x[1])
        return [x for _, x in sorted(sorted_nums[-k:])]
