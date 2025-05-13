from collections import Counter

class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        mod = 10 ** 9 + 7
        count = Counter([ord(char)-97 for char in s])
        for _ in range(t):
            last = count[25]
            for i in range(24,-1,-1):
                count[i+1] = count[i]
            count[0] = 0
            if last > 0:
                count[0] += last
                count[1] += last
        return sum(count.values()) % mod


