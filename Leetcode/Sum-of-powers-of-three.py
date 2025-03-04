import math


class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        max_exp = math.floor(math.log(n, 3))

        remaining = n - (3**max_exp)

        for exp in range(max_exp - 1, -1, -1):
            cur = 3**exp
            if cur <= remaining:
                remaining -= cur

        return remaining == 0


ans = Solution()
print(ans.checkPowersOfThree(91))
