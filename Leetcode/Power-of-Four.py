from math import log
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        power = log(n,4)
        return int(power) == power
