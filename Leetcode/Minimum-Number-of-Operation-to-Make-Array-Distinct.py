import math
from collections import defaultdict

class Solution:
    def minimumOperations(self, nums: list[int]) -> int:
        num_count = defaultdict(int)
        for i in range(len(nums)-1,-1,-1):
            if num_count[nums[i]] == 0:
                num_count[nums[i]] = 1
            else:
                return math.ceil((i+1)/3)
        return 0
