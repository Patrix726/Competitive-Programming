from collections import Counter


class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        count = Counter(nums)
        mark = len(nums) // 3
        return list(filter(lambda x: count[x] > mark, count))
