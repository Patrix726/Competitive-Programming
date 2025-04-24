
class Solution:
    def countCompleteSubarrays(self, nums: list[int]) -> int:
        nums_set = set(nums)

        left = 0
        right = 0
        n = len(nums)
        nums_count = {}
        total = 0
        while right < n:
            nums_count[nums[right]] = nums_count.get(nums[right],0) + 1
            if len(nums_count)==len(nums_set):
                total += n - right
            while len(nums_count) == len(nums_set):
                nums_count[nums[left]]-=1
                if nums_count[nums[left]] <= 0:
                    del nums_count[nums[left]]
                if len(nums_count)==len(nums_set):
                    total += n - right
                left+=1
            right+=1
        return total


