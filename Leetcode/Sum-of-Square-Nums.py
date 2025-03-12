from math import floor,sqrt

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        right = floor(sqrt(c))
        left = 0
        while left <=right:
            l_sqr = left**2
            r_sqr = right**2
            if l_sqr + r_sqr == c:
                return True
            elif l_sqr+r_sqr < c:
                left+=1
            else:
                right-=1
        return False
