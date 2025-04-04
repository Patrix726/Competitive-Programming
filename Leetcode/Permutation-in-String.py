from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window = len(s1)
        left = 0
        right = window
        n = len(s2)
        str_set = set(s1)
        count = Counter(s1)
        output = False
        while right <= n:
            if str_set.issubset(s2[left:right]):
                output = output or count == Counter(s2[left:right])
            left += 1
            right+=1
        return output

