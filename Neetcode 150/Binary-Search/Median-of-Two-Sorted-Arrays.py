class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        merged = nums1 + nums2
        merged.sort()
        n = len(merged)
        if n % 2 == 0:
            return (merged[n//2] + merged[(n//2)-1])/2
        else:
            return merged[n//2]
