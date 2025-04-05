from itertools import combinations

class Solution:
    def subsetXORSum(self, nums: list[int]) -> int:
        total = 0
        for i in range(1,len(nums)+1):
            subsets = list(combinations(nums,i))
            for subset in subsets:
                subset_total = 0
                for num in subset:
                    subset_total^=num
                total +=subset_total
        return total 
ans = Solution()
print(ans.subsetXORSum([1,3]))
