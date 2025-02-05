from heapq import heapify, heappush, heappop, heappushpop


class Solution:
    def maximumProduct(self, nums: list[int]) -> int:
        if len(nums) == 3:
            return nums[0] * nums[1] * nums[2]
        maxNums = nums[:3]
        minNums = [-1 * num for num in nums[:3]]
        heapify(maxNums)
        heapify(minNums)
        for num in nums[3:]:
            heappushpop(maxNums, num)
            heappushpop(minNums, -1 * num)
        maxNum = max(maxNums)
        postiveProd = heappop(maxNums) * heappop(maxNums) * heappop(maxNums)
        heappop(minNums)
        negativeProd = heappop(minNums) * heappop(minNums) * maxNum

        return max(postiveProd, negativeProd)


ans = Solution()
print(ans.maximumProduct([-1, -2, -3]))
