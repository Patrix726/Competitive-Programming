def maxOperations(nums: list[int], k: int) -> int:
    l = 0
    r = len(nums) - 1
    count = 0
    nums.sort()
    while l < r:
        sum = nums[l] + nums[r]
        if sum == k:
            count += 1
            r -= 1
            l += 1
        elif sum < k:
            l += 1
        else:
            r -= 1
    return count


print(maxOperations([1, 2, 3, 4], 5))
