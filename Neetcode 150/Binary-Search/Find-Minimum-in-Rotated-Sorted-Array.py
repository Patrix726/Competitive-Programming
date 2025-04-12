
class Solution:
    def findMin(self, nums: list[int]) -> int:
        n = len(nums)
        left = 0
        right = n-1
        mid = (left+right)//2
        minimum = nums[mid]
        while left<=right:
            mid = (left+right)//2
            if nums[mid] <= minimum:
                minimum = nums[mid]
            if nums[right] < nums[mid]:
                left = mid + 1
            elif nums[left] < nums[mid]:
                right = mid - 1
            else:
                left+=1
                right-=1
        return minimum
            

