class Solution:
    def lenLongestFibSubseq(self, arr: list[int]) -> int:
        n = len(arr)
        if n <= 2:
            return 0
        numSet = set(arr)
        maxLength = 0
        i = 0
        j = 1
        while i < n:
            j = i + 1
            while j < n:
                cur_sum = arr[j] + arr[i]
                cur_len = 2
                prev = arr[j]
                while cur_sum in numSet:
                    cur_len += 1
                    cur_sum += prev
                    prev = cur_sum - prev
                maxLength = max(cur_len, maxLength)
                j += 1
            i += 1
        return maxLength if maxLength > 2 else 0
