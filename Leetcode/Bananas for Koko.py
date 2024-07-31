import math


def minEatingSpeed(piles: list[int], h: int) -> int:
    l = 1
    r = max(piles)
    speed = 0
    if len(piles) == 1:
        return math.ceil(piles[0] / h)
    while l <= r:
        mid = (l + r) // 2
        hrs = 0
        for i in piles:
            if i < mid:
                hrs += 1
            else:
                hrs += math.ceil(i / mid)
        if hrs <= h:
            speed = mid
            r = mid - 1
        else:
            l = mid + 1
    return speed


print(minEatingSpeed([30, 11, 23, 4, 20], 6))
