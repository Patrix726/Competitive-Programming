class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        divisible = sum([ m * i for i in range(1,(n//m)+1)])
        total = sum(range(1,n+1))
        return total - 2 * divisible
