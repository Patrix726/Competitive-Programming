class Solution:
    def search(self, nums: list[int], target: int) -> int:
        n = len(nums)
        left = 0
        right = n-1

        while left<=right:
            mid = (left+right)//2
            if nums[mid]==target:
                return mid
            elif nums[left] <= nums[mid]:
                if nums[left]<=target and target <nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid]<target and target<= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1
