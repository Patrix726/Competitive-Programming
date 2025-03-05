from collections import Counter


class Solution:
    def relativeSortArray(self, arr1: list[int], arr2: list[int]) -> list[int]:
        count = Counter(arr1)
        output = []
        for num in arr2:
            output.extend([num] * count[num])
        remaining = sorted([num for num in arr1 if num not in set(arr2)])
        return output + remaining
