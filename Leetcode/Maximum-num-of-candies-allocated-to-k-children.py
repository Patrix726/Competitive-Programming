class Solution:
    def maximumCandies(self, candies: list[int], k: int) -> int:
        total = sum(candies)
        
        left = 1
        right = total//k
        max_candy = 0
        while left <=right:
            mid = left + (right-left)//2
            count = 0
            for candy in candies:
                count+=candy//mid
            if count >=k:
                max_candy = mid
                left = mid+1
            else:
                right = mid-1
        return max_candy
        
        
       
