import functools

# def singleNumber(nums: list[int]) -> int:
#     length = len(nums)
#     mid = (length - 1) // 2
#     for i in range(length):
#         newlist = nums[:i] + nums[i + 1 :]
#         if len(set(newlist)) == mid:
#             return nums[i]

#     return -1


def singleNumber(nums: list[int]) -> int:
    return functools.reduce(lambda x, y: x ^ y, nums, 0)


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
