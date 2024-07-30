def findPeakElement(nums: list[int]) -> int:
    l = 0
    r = len(nums) - 1
    if r - l <= 1:
        return l if nums[0] >= nums[-1] else 1
    while l < r:
        mid = (l + r) // 2
        print(mid)
        if nums[mid] > nums[mid + 1] and nums[mid] > nums[mid - 1]:
            return mid
        elif nums[mid] < nums[mid + 1]:
            l = mid + 1
        else:
            r = mid - 1
    return l
