from collections import defaultdict


class Solution:
    def mergeArrays(
        self, nums1: list[list[int]], nums2: list[list[int]]
    ) -> list[list[int]]:
        hashmap = defaultdict(int)

        for id, num in nums1 + nums2:
            hashmap[id] += num
        return list(sorted(hashmap.items(), key=lambda x: x[0]))
