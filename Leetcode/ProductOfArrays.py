class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        left_arr = [1]*(n+1)
        right_arr = [1]*(n+1)
        for i in range(1,n+1):
            left_arr[i] = left_arr[i-1]*nums[i-1]
        for i in range(n-1,-1,-1):
            right_arr[i] = right_arr[i+1]*nums[i]
        return [left_arr[i] * right_arr[i+1] for i in range(n)]
        
