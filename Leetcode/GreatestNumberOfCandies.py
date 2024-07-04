def kidsWithCandies(candies: list[int], extraCandies: int) -> list[bool]:
    maxNo = max(candies)
    return list(map(lambda x: x + extraCandies >= maxNo, candies))


print(kidsWithCandies([4, 2, 1, 1, 2], 1))
