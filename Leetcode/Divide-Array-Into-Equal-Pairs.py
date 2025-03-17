from collections import Counter

class Solution:
    def divideArray(self, nums: list[int]) -> bool:
        count = Counter(nums)

        for num_count in count.values():
            if num_count %2!=0:
                return False
        return True
