def findMaxAverage(nums: list[int], k: int) -> float:
    cumSum = 0.0
    average = 0.0
    maxAverage = 0.0
    if k == 1:
        return float(max(nums))
    elif k == len(nums):
        return sum(nums) / float(k)
    else:
        for i in range(len(nums)):
            if i < k - 1:
                cumSum += nums[i]
            else:
                cumSum = cumSum + nums[i] - nums[i - k] if i >= k else cumSum + nums[i]
                average = cumSum / k
                if average > maxAverage or i == k - 1:
                    maxAverage = average
        return maxAverage


print(
    findMaxAverage(
        [0, 1, 1, 3, 3],
        4,
    )
)
