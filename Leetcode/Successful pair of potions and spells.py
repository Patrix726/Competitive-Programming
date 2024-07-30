import math


def successfulPairs(spells: list[int], potions: list[int], success: int) -> list[int]:
    m, n = (
        spells,
        potions if min(len(spells), len(potions)) == len(spells) else potions,
        spells,
    )
    count = []
    for i in m:
        v = math.ceil(success / i)
        count.append(0)
        for j in n:
            if j >= v:
                count[-1] += 1
    return count


# Another possible solution
# class Solution:
#     def successfulPairs(
#         self, spells: List[int], potions: List[int], success: int
#     ) -> List[int]:
#         count = []
#         potions.sort()
#         for i in spells:
#             v = math.ceil(success / i)
#             l = 0
#             r = len(potions) - 1
#             mid = (l + r) // 2
#             while l != r:
#                 if potions[mid] >= v:
#                     r = mid
#                 else:
#                     l = mid + 1
#                 mid = (l + r) // 2

#             if l == len(potions) - 1 and potions[-1] < v:
#                 count.append(len(potions) - l - 1)
#             else:
#                 count.append(len(potions[l:]))

#         return count
