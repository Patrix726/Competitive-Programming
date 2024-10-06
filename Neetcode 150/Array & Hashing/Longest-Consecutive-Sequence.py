from collections import defaultdict


class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        count = defaultdict(lambda: 0)
        maxCount = 0
        for i in nums:
            if count[i] != 0:
                continue
            prev = count[i - 1]
            next = count[i + 1]
            count[i] = prev + 1 + next
            if prev > 0:
                count[i - prev] = count[i]
            if next > 0:
                count[i + next] = count[i]
            maxCount = max(maxCount, count[i])
        return maxCount


ans = Solution()
print(ans.longestConsecutive([]))
