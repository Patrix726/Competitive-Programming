class Solution:
    def fib(self, n: int) -> int:
        if n==0 or n==1:
            return n
        l,r = 0,1
        i = 1
        while i < n:
            r += l
            l = r - l
            i+=1
        return r

