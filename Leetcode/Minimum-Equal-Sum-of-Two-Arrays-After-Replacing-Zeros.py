class Solution:
    def minSum(self, nums1: list[int], nums2: list[int]) -> int:
        suma = sum(nums1)
        sumb = sum(nums2)
        zerosa = nums1.count(0)
        zerosb = nums2.count(0)
        max_total = max(suma+zerosa, sumb + zerosb)
        if max_total != suma and zerosa == 0 or max_total != sumb and zerosb == 0:
            return -1
        return max_total


