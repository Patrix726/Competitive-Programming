class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        ind = len(nums1)-1
        num1 = m-1
        num2 = n-1
        while ind >= 0:
            if num1 >= 0 and num2 >= 0:
                if nums1[num1] > nums2[num2]:
                    nums1[ind] = nums1[num1]
                    num1-=1
                else:
                    nums1[ind] = nums2[num2]
                    num2-=1
            elif num1 < 0:
                nums1[ind] = nums2[num2]
                num2-=1
            elif num2 < 0:
                nums1[ind] = nums1[num1]
                num1-=1
            ind-=1

