from collections import Counter

class Solution:
    def minimumIndex(self, nums: list[int]) -> int:
        n = len(nums)
        target = Counter(nums).most_common(1)[0]
        count = 0
        for i in range(n):
            count += 1 if nums[i]==target[0] else 0
            remaining = target[1] - count
            if count > (i+1)//2 and remaining > (n-(i+1))//2:
                return i
        return -1

