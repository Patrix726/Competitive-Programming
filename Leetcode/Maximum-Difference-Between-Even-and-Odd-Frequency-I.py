from collections import Counter

class Solution:
    def maxDifference(self, s: str) -> int:
        count = Counter(s)
        min_freq = float('inf')
        max_freq = float('-inf')
        for freq in count.values():
            if freq % 2 == 0:
                min_freq = min(min_freq, freq)
            else:
                max_freq = max(max_freq, freq)
        return max_freq - min_freq
