from collections import Counter

class Solution:
    def countGood(self, nums: list[int], k: int) -> int:
        count = Counter()
        ans = 0
        pairs = 0
        left = 0
        n = len(nums)

        for right, num in enumerate(nums):
            pairs+= count[num]
            count[num]+=1

            while pairs >= k:
                ans+= n-right
                count[nums[left]]-=1
                pairs-=count[nums[left]]
                left+=1
        return ans
                
