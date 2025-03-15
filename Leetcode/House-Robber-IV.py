class Solution:
    def minCapability(self, nums: list[int], k: int) -> int:
        def checkPossible(min_cap):
            i = 0
            count = 0
            while i < len(nums):
                if nums[i]<=min_cap:
                    count+=1
                    i +=2
                else:
                    i+=1
            return count>=k
        left = 1
        right = max(nums)
        min_capable = right
        while left<=right:
            mid = (right+left)//2
            
            if checkPossible(mid):
                right = mid-1
                min_capable = mid
            else:
                left = mid+1
        return min_capable
