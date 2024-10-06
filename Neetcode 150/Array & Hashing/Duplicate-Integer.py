class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
        s = set(nums)
        return len(s) != len(nums)


ans = Solution()
print(ans.hasDuplicate([1, 2, 3, 3]))
