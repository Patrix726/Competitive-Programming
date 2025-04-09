class Solution:
    def minOperations(self, nums: list[int], k: int) -> int:
        if min(nums)<k:
            return -1
        nums_set = set(nums)
        if k in nums_set:
            return len(nums_set)-1
        else:
            return len(nums_set)
