from collections import defaultdict

class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        n = len(nums)
        if n==1:
            return 1 if nums[0] == k else 0
        sum_count = defaultdict(int)
        sum_count[0] = 1
        sum = 0
        count = 0
        for num in nums:
            sum+=num
            diff = sum - k
            if sum_count[diff] > 0:
                count+=sum_count[diff]
            sum_count[sum] +=1
        return count

            

        
