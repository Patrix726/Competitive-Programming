from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        p_count = Counter(p)
        output = []
        n = len(p)
        for i in range(len(s)-n+1):
            s_count =  Counter(s[i:i+n])
            if s_count == p_count:
                output.append(i)
        return output
