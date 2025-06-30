from collections import Counter

class Solution:
    def findlHS(self, nums: list[int]) -> int:
        count = Counter(nums)
        max_length = 0
        for k,v in count.items():
            if count[k+1] > 0:
                max_length = max(max_length, v + count[k+1])
        return max_length
