from collections import Counter


class Solution:
    def countCharacters(self, words: list[str], chars: str) -> int:
        charSet = set(chars)
        charCount = Counter(chars)
        result = ""
        for word in words:
            wordSet = set(word)

            if not wordSet.issubset(charSet):
                continue
            if len(wordSet) == len(word):
                result += word
            else:
                wordCount = Counter(word)
                wordCount.subtract(charCount)
                temp = wordCount.most_common(1)
                if temp[0][1] <= 0:
                    result += word
        return len(result)


ans = Solution()

print(ans.countCharacters(["hello", "world", "leetcode"], "welldonehoneyr"))
