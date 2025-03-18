class Solution:
    def longestNiceSubarray(self, nums: list[int]) -> int:
        max_count = 1
        for i in range(len(nums)):
            cur = nums[i]
            count = 1
            for j in range(i+1,len(nums)):
                if nums[j] & cur ==0:
                    count+=1
                    cur+=nums[j]
                else:
                    break
            max_count = max(max_count,count)
        return max_count
