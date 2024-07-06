def moveZeroes(nums: list[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    cur = 0
    for i in range(len(nums)):
        if nums[cur] == 0:
            nums.pop(cur)
            nums.append(0)
        else:
            cur += 1

    return nums


print(moveZeroes([0, 1, 0, 3, 12]))
