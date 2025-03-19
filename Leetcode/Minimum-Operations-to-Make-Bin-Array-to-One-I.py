class Solution:
    def minOperations(self, nums: list[int]) -> int:
        def checkValid():
            return all(nums)
        count = 0
        for i in range(len(nums)-2):
            flip = [1,0]
            if nums[i]==0:
                nums[i:i+3] = [flip[i] for i in nums[i:i+3]]
                count+=1
        return count if checkValid() else -1
        
        
