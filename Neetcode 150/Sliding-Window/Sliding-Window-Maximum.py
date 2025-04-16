import heapq
from collections import Counter

class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        count = Counter(nums[:k])
        window = list(map(lambda x: -x, nums[:k]))
        heapq.heapify(window)
        output = [-1*min(window)]
        left = 0
        right = k
        n = len(nums)
        while right < n:
            count[nums[left]] -= 1
            count[nums[right]]+=1
            heapq.heappush(window,-1 * nums[right])
            min_val = heapq.heappop(window)
            while count[-1 * min_val] <= 0:
                min_val = heapq.heappop(window)
            heapq.heappush(window,min_val)
            output.append(-1*min_val)
            right+=1
            left+=1
        return output

 
