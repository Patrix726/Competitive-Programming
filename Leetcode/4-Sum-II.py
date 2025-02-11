from collections import defaultdict


class Solution:
    def fourSumCount(
        self, nums1: list[int], nums2: list[int], nums3: list[int], nums4: list[int]
    ) -> int:
        coll1 = defaultdict(int)
        coll2 = defaultdict(int)
        count = 0
        for i in nums1:
            for j in nums2:
                coll1[i + j] += 1
        for i in nums3:
            for j in nums4:
                coll2[i + j] += 1
        for num in coll1.keys():
            if coll2[-1 * num] > 0:
                count += coll1[num] * coll2[-1 * num]
        return count


ans = Solution()

print(ans.fourSumCount([1, 2], [-2, -1], [-1, 2], [0, 2]))
