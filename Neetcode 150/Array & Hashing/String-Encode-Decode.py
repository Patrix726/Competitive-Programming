class Solution:

    def encode(self, strs: list[str]) -> str:
        finalStr = ""
        for j in range(len(strs)):
            i = strs[j]
            newStr = i.split("..")
            newStr = "/..".join(newStr) if len(newStr) > 1 else newStr[0]
            finalStr = "..".join([finalStr, newStr])
        return finalStr

    def decode(self, s: str) -> list[str]:
        curStr = ""
        strs = []
        i = 0
        if s == "":
            return []
        if s == "..":
            return [""]
        s = s[2:] if s.startswith("..") else s
        while i < len(s):
            if s[i] == "/" and i < len(s) - 2 and s[i + 1] == s[i + 2] == ".":
                curStr += ".."
                i += 3
            elif i < len(s) - 1 and s[i] == s[i + 1] == "." or i == len(s) - 1:
                curStr += s[i] if i == len(s) - 1 else ""
                strs.append(curStr)
                curStr = ""
                i += 2
            else:
                curStr += s[i]
                i += 1
        return strs if len(strs) > 0 else [""]


ans = Solution()
encoded = ans.encode(["neet", "code", "love", "you"])
print(encoded, ans.decode(encoded))
