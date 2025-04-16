from collections import Counter, defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        s_count = Counter(s)
        t_count = Counter(t)

        for key, val in t_count.items():
            if s_count[key] < val:
                return ""
        left = 0
        right = 0
        n = len(s)
        m = len(t)
        new_count = defaultdict(int)
        rem = len(t_count)
        min_window = float('inf')
        output = ""
        while right < n:
            if s[right] in t_count:
                new_count[s[right]] += 1
                if new_count[s[right]] == t_count[s[right]]:
                    rem -= 1

            while rem == 0 and left <= right:
                min_window = min(min_window,right-left)
                output = s[left:right+1] if min_window == right-left else output
                if s[left] in t_count:
                    new_count[s[left]]-=1
                    if new_count[s[left]] < t_count[s[left]]:
                        rem+=1
                left+=1
            right+=1
        return output
