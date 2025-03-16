from math import floor, sqrt

class Solution:
    def repairCars(self, ranks: list[int], cars: int) -> int:
        def checkPossible(time:int):
            total = 0
            for rank in ranks:
                total+=floor(sqrt(time/rank))
            return total >= cars
        min_rank = min(ranks)
        right = min_rank * cars*cars
        left = 1
        output = right
        while left <=right:
            mid = (left+right)//2 
            if checkPossible(mid):
                right = mid-1
                output = mid
            else:
                left = mid + 1
        return output
