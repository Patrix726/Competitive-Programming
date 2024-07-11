def findDifference(nums1: list[int], nums2: list[int]) -> list[list[int]]:
    a = set(nums1)
    b = set(nums2)
    return [list(a.difference(b)), list(b.difference(a))]


print(findDifference([1, 2, 3], [2, 4, 6]))
