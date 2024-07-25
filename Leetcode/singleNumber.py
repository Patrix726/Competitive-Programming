def singleNumber(nums: list[int]) -> int:
    length = len(nums)
    mid = (length - 1) // 2
    for i in range(length):
        newlist = nums[:i] + nums[i + 1 :]
        if len(set(newlist)) == mid:
            return nums[i]

    return -1


print(
    singleNumber(
        [
            -336,
            513,
            -560,
            -481,
            -174,
            101,
            -997,
            40,
            -527,
            -784,
            -283,
            -336,
            513,
            -560,
            -481,
            -174,
            101,
            -997,
            40,
            -527,
            -784,
            -283,
            354,
        ]
    )
)
