from collections import defaultdict

class Solution:
    def countPairs(self, nums: list[int], k: int) -> int:
        res = 0
        count = defaultdict(list)

        for idx, num in enumerate(nums):
            if num not in count:
                count[num] = [idx]
                continue
            for index in count[num]:
                if (index * idx) % k==0:
                    res+=1
            count[num]+=[idx]
        return res
            
