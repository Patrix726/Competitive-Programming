class Solution:
    def countGoodTriplets(self, arr: list[int], a: int, b: int, c: int) -> int:
        n = len(arr)
        count = 0
        valid = []

        for i in range(n-2):
            for j in range(i+1,n-1):
                if abs(arr[j]-arr[i])<=a:
                    valid.append((i,j))
        
        for i, j in valid:
            for k in range(j+1,n):
                if abs(arr[k]-arr[j])<=b and abs(arr[k]-arr[i])<=c:
                    count+=1
        return count
