class Solution:
    def countSubarrays(self, nums: list[int], k: int) -> int:
        count = 0
        max_ele = max(nums)
        left = 0
        right = 0
        cur = 0
        n = len(nums)
        while right < n:
            cur += 1 if nums[right]==max_ele else 0
            while cur >=k and left <= right:
                count+= n - right
                cur -= 1 if nums[left]==max_ele else 0
                left+=1
            right+=1
        return count
