class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        index = {}
        anagram = []
        for i in strs:
            sortedStr = "".join(sorted(i))
            if sortedStr in index:
                ind = index.get(sortedStr)
                anagram[ind].append(i)
            else:
                anagram.append([i])
                index[sortedStr] = len(anagram) - 1
        return anagram


ans = Solution()
print(ans.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
