class Solution:
    def findWords(self, words: list[str]) -> list[str]:
        keyRows = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
        rowWords = []
        for word in words:
            wordSet = set(word.lower())

            for row in keyRows:
                intersection = wordSet.intersection(row)
                if len(intersection) != 0 and len(intersection) != len(wordSet):
                    break
                elif len(intersection) == len(wordSet):
                    rowWords.append(word)

        return rowWords


ans = Solution()

print(ans.findWords(["Hello", "Alaska", "Dad", "Peace"]))
