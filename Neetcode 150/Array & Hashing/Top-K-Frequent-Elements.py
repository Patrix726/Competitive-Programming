from collections import Counter


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count = Counter(nums)
        return sorted(count.keys(), key=lambda x: count[x], reverse=True)[:k]


ans = Solution()
print(ans.topKFrequent([1, 1, 1, 2, 2, 3], 2))
