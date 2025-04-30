class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        value = n
        while value >1:
            value /= 3
        return value == 1
