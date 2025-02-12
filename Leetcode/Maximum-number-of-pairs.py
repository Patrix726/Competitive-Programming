from collections import Counter


class Solution:
    def numberOfPairs(self, nums: list[int]) -> list[int]:
        numsCount = Counter(nums)

        remainders = list(filter(lambda count: count % 2 != 0, numsCount.values()))
        numberOfpairs = int((len(nums) - len(remainders)) / 2)
        return [numberOfpairs, len(remainders)]


ans = Solution()
print(ans.numberOfPairs([1, 3, 2, 1, 3, 2, 2]))
