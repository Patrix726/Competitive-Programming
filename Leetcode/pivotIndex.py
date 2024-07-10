def pivotIndex(nums: list[int]) -> int:
    lsum = li = 0
    rsum = sum(nums[1:])
    while lsum != rsum and li < len(nums) - 1:
        if lsum < rsum:
            lsum += nums[li]
            li += 1
            rsum -= nums[li]
        elif lsum == rsum:
            return li
        else:
            lsum += nums[li]
            li += 1
            rsum -= nums[li]
    return li if lsum == rsum else -1


# def pivotIndex(nums: list[int]) -> int:
#     for i in range(len(nums)):
#         if sum(nums[:i]) == sum(nums[i + 1 :]):
#             return i
#     return -1


print(pivotIndex([1, 7, 3, 6, 5, 6]))
