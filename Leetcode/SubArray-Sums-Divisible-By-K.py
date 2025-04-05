from collections import defaultdict

class Solution:
    def subarraysDivByK(self, nums: list[int], k: int) -> int:
        rem_count = defaultdict(int)
        n = len(nums)
        prefix_sum = [0]*(n+1)
        rem_count[0]+=1
        total_count = 0
        for i in range(1,n+1):
            prefix_sum[i] = prefix_sum[i-1] + nums[i-1]
            rem = prefix_sum[i]%k
            total_count+=rem_count[rem]
            rem_count[rem]+=1
        return total_count
        
