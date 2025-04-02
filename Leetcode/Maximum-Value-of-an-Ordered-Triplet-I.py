
class Solution:
    def maximumTripletValue(self, nums: list[int]) -> int:
        diffs = []
        left = 0
        right = 1
        n = len(nums)
        while right < n-1:
            diff = nums[left] - nums[right]
            if diff <0:
                left = right
                right +=1
            else:
                diffs.append((diff,right+1))
                right+=1
        max_vals = [0]*n
        max_vals[-1] = nums[-1]
        for i in range(n-2,-1,-1):
            max_vals[i] = max(max_vals[i+1],nums[i])
        output = 0
        for diff, i in diffs:
            output= max(output, diff*max_vals[i])
        return output
