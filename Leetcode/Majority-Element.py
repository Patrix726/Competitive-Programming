from collections import Counter


class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        numsCount = Counter(nums)
        return numsCount.most_common(1)[0][0]


ans = Solution()

print(ans.majorityElement([3, 2, 3]))
