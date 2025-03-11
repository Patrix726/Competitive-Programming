from collections import defaultdict

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        char_count = defaultdict(int)
        output = 0
        n = len(s)
        start = end = 0
        while (start < n-2 and end < n) or len(char_count)==3:
            if len(char_count)==3:
                output+=1 + n - end
                char_count[s[start]]-=1
                if char_count[s[start]]==0:
                    del char_count[s[start]]
                start+=1
            elif end<n:
                char_count[s[end]]+=1
                end+=1
        return output

ans = Solution()
print(ans.numberOfSubstrings("abcabc"))
