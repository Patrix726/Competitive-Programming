import heapq


def findKthLargest(nums: list[int], k: int) -> int:
    return min(heapq.nlargest(k, nums))


print(findKthLargest([2, 1], 2))
