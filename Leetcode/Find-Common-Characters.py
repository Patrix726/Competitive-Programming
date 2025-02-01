from collections import Counter


class Solution:
    def commonChars(self, words: list[str]) -> list[str]:

        entire = ""
        respectiveCounter = []
        for word in words:
            uniqueChars = "".join(set(word))
            respectiveCounter.append(Counter(word))
            entire += uniqueChars

        count = Counter(entire)
        common = []
        for key, value in count.items():
            if value >= len(words):
                common.append(key)
        result = []
        for char in common:
            duplicates = None
            for counter in respectiveCounter:
                duplicates = (
                    counter[char]
                    if duplicates is None
                    else min(duplicates, counter[char])
                )
            for j in range(duplicates):
                result.append(char)

        return result


ans = Solution()
print(ans.commonChars(["bella", "label", "roller"]))
