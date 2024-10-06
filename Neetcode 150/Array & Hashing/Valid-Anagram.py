class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        d = {}

        for i in range(len(s)):
            if s[i] == t[i]:
                continue
            sVal = d.get(s[i], 0) + 1
            tVal = d.get(t[i], 0) - 1
            if sVal == 0:
                d.pop(s[i], 0)
            else:
                d[s[i]] = sVal
            if tVal == 0:
                d.pop(t[i], 0)
            else:
                d[t[i]] = tVal
        return len(d) == 0


ans = Solution()
print(ans.isAnagram("jra", "jbr"))
