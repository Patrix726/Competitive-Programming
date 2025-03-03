class Solution:
    def pivotArray(self, nums: list[int], pivot: int) -> list[int]:
        lt, gt, eq = [], [], []
        for num in nums:
            if num < pivot:
                lt.append(num)
            elif num > pivot:
                gt.append(num)
            else:
                eq.append(num)
        return lt + eq + gt
